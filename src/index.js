import panzoom from 'panzoom';
import flicking from '@egjs/flicking';
import createModule from './pyjs_runtime_browser.js';
// console.log(panzoom);
// console.log(flicking);


// just grab a DOM element
var element = document.querySelector('#scene')

// And pass it to panzoom
// panzoom(element)

// (async function(){
//     console.log("in async main")
// })()


const asyncMain = async () => {
    console.log("in async main")

    var pyjs = await createModule()
    globalThis.Module = pyjs
    pyjs.empackSetStatus = function(status, packageName, downloaded,total){
        var str = `Downloading data: ${downloaded} / ${total}`
        console.log(str)
    }
    console.log("Download data ...")
    const { default: load_all }  = await import('./sample_webpack_example.js')
    console.log("load_all",load_all)
    await load_all()
    await pyjs.init()


};

asyncMain()