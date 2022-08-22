import {createModule} from './pyjs_runtime_browser.js';
import {CanvasDebugDraw} from "./canvas_debug_draw.js"

var pyjs_init_promise = null
var pyjs = null
var editor = null

async function load_pycode(loc){
    console.log("fetching pycode")
    return await (await fetch(loc)).text();
}

function db_load_example(context, name){
    let db_key = `examples/${name}`
    return localStorage.getItem(db_key);
}
function db_store_example(context, name, code){
    let db_key = `examples/${name}`
    localStorage.setItem(db_key, code)
}

async function load_pyb2_example(context, name){

    let saved_exampled = db_load_example(context, name)
    if(!saved_exampled || saved_exampled==="")
    {
        let fname = context.examples.examples_dict[name]
        let p =  load_pycode(`./python/examples/${fname}`)
        p.then((code)=>{
            db_store_example(context, name, code)
        });
        return p;
    }
    else{
        return Promise.resolve(saved_exampled);
    }
}

async function set_current_example(context, name){
    var load_code_promise = load_pyb2_example(context, name)
    load_code_promise.then((code)=>{
        context.terminal.writeln("loaded code")
        context.editor.dispatch({
          changes: {from: 0, to: context.editor.state.doc.length, insert: code}
        })
        context.examples.curret_example = name
    })
    return load_code_promise
}


async function init_pybd(context){

    const canvas_debug_draw_code = await load_pycode('./python/canvas_debug_draw.py')
    const canvas_backend_code = await load_pycode('./python/canvas_backend.py')
    globalThis.canvas_debug_draw = new CanvasDebugDraw(context.canvas)
    await pyjs_init_promise
    globalThis.pyjs.exec(canvas_debug_draw_code)
    globalThis.pyjs.exec(canvas_backend_code)
}


const print = (terminal,text) => {
  terminal.writeln(text)

}
const printErr = (terminal, text) => {
  // these can be ignored
  if(!text.startWith("Could not find platform dependent libraries") && ! text.startWith("Consider setting $PYTHONHOME")){
    terminal.writeln("ERROR: "+text)
  }
}



async function init_pyjs(context){
    var terminal = context.terminal;
    pyjs = await createModule({
        print: (txt)=>{
            print(terminal, txt)
        },
        printErr: (txt)=>{
            printErr(terminal, txt)
        }
    })
    // globalThis.Module = pyjs
    globalThis.pyjs = pyjs
    pyjs.empackSetStatus = function(status, packageName, downloaded,total){
        var str = `Downloading data: ${downloaded} / ${total}`
        // console.log(str)
        terminal.writeln(str);

    }
    terminal.writeln("Download data ...")
    const { default: load_all }  = await import('./sample_webpack_example.js')
    await load_all()
    pyjs_init_promise =  pyjs.init()
    pyjs_init_promise.then(()=>{
        terminal.writeln("pyjs is initialized")
    })

    return pyjs_init_promise
}

async function fetch_examples_list(context){
    let examples_list = await (await fetch('./python/examples/examples.json')).json();
    context.examples.examples_list =  examples_list
    context.examples.examples_dict = {}
    for(let i=0; i<examples_list.length; ++i){
        context.examples.examples_dict[examples_list[i][0]] = examples_list[i][1]
    }
    return examples_list
}



async function init_py(context){


    await Promise.all([
        init_pyjs(context),
        fetch_examples_list(context)
    ])

 
    await Promise.all([
        init_pybd(context), 
        set_current_example(context, context.examples.examples_list[0][0])
    ])
    return globalThis.pyjs
}


async function run(context){
    var text = context.editor.state.doc.toString()
    db_store_example(context, context.examples.curret_example, text)
    try{
        pyjs.exec(text)
        var async_main =  pyjs.eval("async_main")
        context.state.running = true

        context.ctrl.play_button.disabled = true
        context.ctrl.pause_button.disabled = false
        context.ctrl.forward_button.disabled = true
        context.ctrl.stop_button.disabled = false
                  
        context.state.run_promise =  async_main.py_call_async(context)
        await context.state.run_promise
        context.state.running = false
    }
    catch (e) {
        console.error(e)
        // terminal.writeln("catched error:",e)
        context.terminal.writeln(JSON.stringify(e.message));
    }
}

function schedule_run(context){
    context.terminal.writeln("schedule_run")
    setTimeout(()=>{run(context)},0)
}

export {init_py,schedule_run,set_current_example}