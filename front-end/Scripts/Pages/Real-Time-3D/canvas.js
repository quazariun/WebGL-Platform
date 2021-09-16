import { main } from '../../WGLdebugger/WGLdebugger.js';
import { getCanvas, getGLContext } from '../../Libs/utils.js';

import init_canvas, * as canvas from '../../WebGL/Real-Time-3D/canvas.js';

window.onload = function() {

    let canvas = getCanvas("webgl-canvas");
    let gl = getGLContext(canvas);

    init_canvas(gl);
    main(gl);
}