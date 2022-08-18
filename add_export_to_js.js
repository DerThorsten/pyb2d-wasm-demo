const fs = require('fs');
const filepath = './src/pyjs_runtime_browser.js';
const out_filepath =  './src/patched_pyjs_runtime_browser.js';
const data = fs.readFileSync(filepath);
if(! data.includes("export {createModule}")){
    fs.writeFileSync(filepath, data + "\nexport {createModule}\n");
}