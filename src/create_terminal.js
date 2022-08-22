import css from 'xterm/css/xterm.css'
import { Terminal } from 'xterm';
import { FitAddon } from 'xterm-addon-fit';


function createTerminal(){
    var terminal = new Terminal();
    terminal.open(document.getElementById('terminal-container'));
    const fitAddon = new FitAddon();
    terminal.loadAddon(fitAddon);
    fitAddon.fit();
    return terminal
}

export {createTerminal}