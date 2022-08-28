

import {EditorView, basicSetup} from "codemirror"
import { python } from '@codemirror/lang-python'
import { oneDark, oneDarkTheme  } from '@codemirror/theme-one-dark'

function createEditor(){


    var inputtext = document.getElementById("inputtext")
    // inputtext.parentNode.insertBefore(editor.dom, inputtext)

    let editor = new EditorView({
      doc: "no code loaded yet - probably an error, check the \"Log\" tab",
      extensions: [
        basicSetup,
        python(),
        oneDarkTheme,
      ],
      parent: inputtext.parentNode
    })

    inputtext.style.display = "none"
    if (inputtext.form) inputtext.form.addEventListener("submit", () => {
        inputtext.value = editor.state.doc.toString()
    })

    // EditorView.theme(materialDarker)

    return editor

}

export {createEditor}