


import css5 from '@fortawesome/fontawesome-free/css/all.min.css'



import './scss/main.scss'

// Import all of Bootstrap's JS
import * as bootstrap from 'bootstrap'

import css4 from './css/mycss.css';

import {createTerminal} from './create_terminal.js'
import {createEditor} from './create_editor.js'
import {init_py,schedule_run} from './py_utils.js'
import {init_ui_pre,init_ui_post} from './ui.js'



const asyncMain = async () => {


    let resolution = [800, 500];

    var terminal = createTerminal()
    var editor = createEditor()
    var canvas =document.getElementById('myCanvas')
    var context = {
        terminal:terminal,
        editor:editor,
        canvas:canvas,
        examples : {
            examples_list : null,
            examples_dict : null,
            current_example : null
        },
        ctrl : {
            level_dropdown : document.getElementById("level_dropdown"),
            play_button : document.getElementById("play_button"),
            stop_button : document.getElementById("stop_button"),
            pause_button : document.getElementById("pause_button"),
            forward_button : document.getElementById("forward_button")
        },
        state : {
            running : false,
            paused : false,
            run_promise : null
        },
        gui_settings : {
            resolution : resolution,
            scale : 15,
            translate : [0, -1 * resolution[1] / 2],
            fps:24
        }

    }
    init_ui_pre(context)
    var pyjs = await init_py(context)
    init_ui_post(context)
    document.getElementById('level_toggle_button').disabled = false
    schedule_run(context)
};


asyncMain()