(self.webpackChunkpyb2d_wasm_demo=self.webpackChunkpyb2d_wasm_demo||[]).push([[455],{6455:()=>{var e=void 0!==globalThis.pyjs?globalThis.pyjs:{};e.expectedDataFileDownloads||(e.expectedDataFileDownloads=0),e.expectedDataFileDownloads++,e.ENVIRONMENT_IS_PTHREAD||function(a){"object"==typeof window?window.encodeURIComponent(window.location.pathname.toString().substring(0,window.location.pathname.toString().lastIndexOf("/"))+"/"):"undefined"==typeof process&&"undefined"!=typeof location&&encodeURIComponent(location.pathname.toString().substring(0,location.pathname.toString().lastIndexOf("/"))+"/");var t="dataclasses-0.8-pyhc8e2a94_3.data",o="dataclasses-0.8-pyhc8e2a94_3.data";"function"!=typeof e.locateFilePackage||e.locateFile||(e.locateFile=e.locateFilePackage,err("warning: you defined Module.locateFilePackage, that has been renamed to Module.locateFile (using your locateFilePackage for now)"));var n,s,l,r,d=e.locateFile?e.locateFile(o,""):o,i=a.remote_package_size,c=null,u=e.getPreloadedPackage?e.getPreloadedPackage(d,i):null;function p(){function o(e,a){if(!e)throw a+(new Error).stack}function n(t){o(t,"Loading data file failed."),o(t instanceof ArrayBuffer,"bad input to processPackageData");var n=new Uint8Array(t),s={data:null,cachedOffset:107,cachedIndexes:[-1,-1],cachedChunks:[null,null],offsets:[0],sizes:[107],successes:[0]};s.data=n,o("object"==typeof e.LZ4,"LZ4 not present - was your app build with -sLZ4?"),e.LZ4.loadPackage({metadata:a,compressedData:s},!0),e.removeRunDependency("datafile_dataclasses-0.8-pyhc8e2a94_3.data")}e.FS_createPath("/","home",!0,!0),e.FS_createPath("/home","runner",!0,!0),e.FS_createPath("/home/runner","micromamba-root",!0,!0),e.FS_createPath("/home/runner/micromamba-root","envs",!0,!0),e.FS_createPath("/home/runner/micromamba-root/envs","pyjs-wasm-env",!0,!0),e.FS_createPath("/home/runner/micromamba-root/envs/pyjs-wasm-env","lib",!0,!0),e.FS_createPath("/home/runner/micromamba-root/envs/pyjs-wasm-env/lib","python3.10",!0,!0),e.FS_createPath("/home/runner/micromamba-root/envs/pyjs-wasm-env/lib/python3.10","site-packages",!0,!0),e.FS_createPath("/home/runner/micromamba-root/envs/pyjs-wasm-env/lib/python3.10/site-packages","dataclasses-0.8.dist-info",!0,!0),e.addRunDependency("datafile_dataclasses-0.8-pyhc8e2a94_3.data"),e.preloadResults||(e.preloadResults={}),e.preloadResults[t]={fromCache:!1},u?(n(u),u=null):c=n}u||(n=d,s=i,l=function(e){c?(c(e),c=null):u=e},(r=new XMLHttpRequest).open("GET",n,!0),r.responseType="arraybuffer",r.onprogress=function(a){var o=n,l=s;if(a.total&&(l=a.total),a.loaded){r.addedTotal?e.dataFileDownloads[o].loaded=a.loaded:(r.addedTotal=!0,e.dataFileDownloads||(e.dataFileDownloads={}),e.dataFileDownloads[o]={loaded:a.loaded,total:l});var d=0,i=0,c=0;for(var u in e.dataFileDownloads){var p=e.dataFileDownloads[u];d+=p.total,i+=p.loaded,c++}d=Math.ceil(d*e.expectedDataFileDownloads/c),e.empackSetStatus&&e.empackSetStatus("Downloading",t,i,d),e.setStatus&&e.setStatus("Downloading data... ("+i+"/"+d+")")}else e.dataFileDownloads||e.setStatus&&e.setStatus("Downloading data...")},r.onerror=function(e){throw new Error("NetworkError for: "+n)},r.onload=function(e){if(!(200==r.status||304==r.status||206==r.status||0==r.status&&r.response))throw new Error(r.statusText+" : "+r.responseURL);var a=r.response;l(a)},r.send(null)),e.calledRun?p():(e.preRun||(e.preRun=[]),e.preRun.push(p))}({files:[{filename:"/home/runner/micromamba-root/envs/pyjs-wasm-env/lib/python3.10/site-packages/dataclasses-0.8.dist-info/direct_url.json",start:0,end:107}]})}}]);