import { main } from '../../WGLdebugger/WGLdebugger.js';
import { getCanvas, getGLContext, autoResizeCanvas } from '../../Libs/utils.js';

import init_square, * as square from '../../WebGL/Geometries/square.js';

window.onload = function() {

    let canvas = getCanvas("webgl-canvas");
    let gl = getGLContext(canvas);
    autoResizeCanvas(canvas);

    init_square(gl);
    main(gl);
}