
import * as monaco_api from 'monaco-editor/esm/vs/editor/editor.api';
import * as monaco from 'monaco-editor';

import css from 'xterm/css/xterm.css'
import { Terminal } from 'xterm';
import { FitAddon } from 'xterm-addon-fit';
import {createModule} from './pyjs_runtime_browser.js';


import css5 from '@fortawesome/fontawesome-free/css/all.min.css'

// import css2 from 'bootstrap/dist/css/bootstrap.min.css';
// import css3 from 'bootstrap/dist/css/bootstrap.min.css';
// import css4 from './css/pushbutton.css';
// import * as bootstrap from 'bootstrap'

// Import our custom CSS
import './scss/main.scss'

// Import all of Bootstrap's JS
import * as bootstrap from 'bootstrap'




// The Monaco Editor can be easily created, given an
// empty container and an options literal.
// Two members of the literal are "value" and "language".
// The editor takes the full size of its container.
(function () {
    // create div to avoid needing a HtmlWebpackPlugin template
    const div = document.createElement('div');
    div.id = 'root1';
    div.style = 'height:600px; border:1px solid #ccc;';
    document.body.appendChild(div);


    const div2 = document.createElement('div');
    div2.id = 'xterm-container';
    div2.style = 'height:400px; border:1px solid #ccc;';
    document.body.appendChild(div2);
})();


let editor = monaco.editor.create(document.getElementById('editor-container'), {
    value: `import numpy\nprint(numpy.ones(4,5))`,
    language: 'python',
    theme: 'vs-dark',
    contextmenu: true,
    automaticLayout: true
});
console.log("the editor", editor)

const terminal = new Terminal();
terminal.open(document.getElementById('terminal-container'));
const fitAddon = new FitAddon();
terminal.loadAddon(fitAddon);
fitAddon.fit();





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

    pyjs.eval("print('hello world')")

};


asyncMain()