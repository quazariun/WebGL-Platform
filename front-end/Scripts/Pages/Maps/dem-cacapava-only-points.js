import { main } from '../../WGLdebugger/WGLdebugger.js';
import * as utils from '../../Libs/utils.js';

import init_dem, * as dem from '../../WebGL/Maps/dem-cacapava-only-points.js';

window.onload = function() {
    let canvas = utils.getCanvas("webgl-canvas");
    let gl = utils.getGLContext(canvas);
    utils.autoResizeCanvas(canvas);

    init_dem(gl);
    main(gl);
}