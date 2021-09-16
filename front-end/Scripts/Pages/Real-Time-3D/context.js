import { main } from '../../WGLdebugger/WGLdebugger.js';
import { getCanvas, getGLContext } from '../../Libs/utils.js';

import init_context, * as canvas from '../../WebGL/Real-Time-3D/context.js';

window.onload = function() {

    let canvas = getCanvas("webgl-canvas");
    let gl = getGLContext(canvas);

    if (!canvas) {
        console.error('Desculpe! Não há um elemento HTML 5 Canvas nesta páginas!');
        return;
    }

    const message = gl ? 'YAY!!! VOCÊ TEM O CONTEXTO WEBGL 2!!!' : 'Desculpa! WebGL não está disponível no seu navegador.Sorry!';
    alert(message);

    init_context(gl);
    main(gl);
}