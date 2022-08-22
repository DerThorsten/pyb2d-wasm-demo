import {schedule_run,set_current_example} from './py_utils.js'

function openTab(evt, tabName) {
  // Declare all variables
  var i, tabcontent, tablinks;

  // Get all elements with class="tabcontent" and hide them
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }

  // Get all elements with class="tablinks" and remove the class "active"
  tablinks = document.getElementsByClassName("nav-link");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }

  // Show the current tab, and add an "active" class to the button that opened the tab
  document.getElementById(tabName).style.display = "block";
  evt.currentTarget.className += " active";
}


async function stop_running(context){

    if(context.state.running){
        let backend = pyjs.eval("backends[0]");
        let fstop = backend.stop
        fstop.py_call()
        await context.state.run_promise
        context.state.running = false
        context.state.paused = false


        context.ctrl.play_button.disabled = false
        context.ctrl.pause_button.disabled = true
        context.ctrl.forward_button.disabled = true
        context.ctrl.stop_button.disabled = true
        backend.delete()
        fstop.delete()
        }
    else{
        console.error("internal error..cannot stop when not running")
    }
}

async function start_running(context){
    if(context.state.running){
        if(context.state.paused){
            var backend = pyjs.eval("backends[0]");
            var fpause = backend.set_pause
            context.state.paused = false
            fpause.py_call(false)

            backend.delete()
            fpause.delete()

            play_button.disabled = true
            pause_button.disabled = false
            forward_button.disabled = true
            stop_button.disabled = false
        }
        else{
            console.error("play button should not be enabled")
        }
    }
    else{
        context.state.running = true
        context.state.paused = false
        schedule_run(context)

        play_button.disabled = true
        pause_button.disabled = false
        forward_button.disabled = true
        stop_button.disabled = false

    }
}

function add_level_to_dropdown(context, text){
    let list = context.ctrl.level_dropdown
    var li = document.createElement("li");
    var link = document.createElement("a");             
    var text_node = document.createTextNode(text);
    link.appendChild(text_node);
    link.href = "#";
    link.classList.add("dropdown-item")
    li.appendChild(link);
    console.log(link)
    link.onclick = async function(evt){

        if(context.state.running){

            await stop_running(context)
            

            console.log(`selected level: ${text}`)
            var level_toggle_button = document.getElementById("level_toggle_button")
            level_toggle_button.innerHTML = text
            console.log(level_toggle_button)
            set_current_example(context, text)
            await start_running(context)
        }
    }
    list.appendChild(li);
}



function setup_controlls(context)
{

    let play_button = context.ctrl.play_button;
    let stop_button = context.ctrl.stop_button;
    let pause_button = context.ctrl.pause_button;
    let forward_button = context.ctrl.forward_button;

    play_button.onclick = async function(){
        await start_running(context)
    }
    stop_button.onclick = async function(){
        await stop_running(context)
    }

    pause_button.onclick = async function(){
        if(context.state.running){
            var backend = pyjs.eval("backends[0]");
            var fpause = backend.set_pause
            if(context.state.paused){
                context.state.paused = false
                fpause.py_call(context.state.paused)

                play_button.disabled = true
                pause_button.disabled = false
                forward_button.disabled = true
                stop_button.disabled = false
            }
            else{
                context.state.paused = true
                fpause.py_call(context.state.paused)

                play_button.disabled = false
                pause_button.disabled = true
                forward_button.disabled = false
                stop_button.disabled = false
            }
            backend.delete()
            fpause.delete()
        }
        else{
            console.error("internal error..cannot pause when not running")
        }
    }

    forward_button.onclick = async function(){
        if(context.state.running){
            var backend = pyjs.eval("backends[0]");
            var fsingle_step = backend._single_step
            if(context.state.paused){

                fsingle_step.py_call()
            }
            else{
                console.error("internal error, cannot forward when not paused")
            }
            backend.delete()
            fsingle_step.delete()

        }
        else{
            console.error("internal error..cannot forward when not running")
        }
    }
}

function init_ui_pre(context){
    globalThis.openTab = openTab
    document.getElementById("openLog").click();

    setup_controlls(context)

   
}

function init_ui_post(context){
    document.getElementById("openCanvas").click();
    let examples = context.examples.examples_list
    document.getElementById("level_toggle_button").innerHTML = examples[0][0]
    for(let i=0; i<examples.length; ++i)
    {
        add_level_to_dropdown(context, examples[i][0])
    }
}
export {init_ui_pre,init_ui_post}