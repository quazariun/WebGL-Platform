import { main } from '../WGLdebugger/WGLdebugger.js';
import * as utils from '../Libs/utils.js';

import init_triangle, * as triangle from '../WebGL/Geometries/triangle.js';

window.onload = function() {
    let canvas = utils.getCanvas("webgl-canvas");
    let gl = utils.getGLContext(canvas);
    utils.autoResizeCanvas(canvas);

    init_triangle(gl);
    main(gl);
}