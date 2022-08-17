import panzoom from 'panzoom';
import flicking from '@egjs/flicking';

console.log(panzoom);
console.log(flicking);


// just grab a DOM element
var element = document.querySelector('#scene')

// And pass it to panzoom
panzoom(element)