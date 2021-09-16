export function getCanvas(id) {
    const canvas = document.getElementById(id);

    if (!canvas) {
        console.error(`Não há um elemento Canvas com esse o Id: ${id} nesta página.`);
        return null;
    }

    return canvas;
}

export function getGLContext(canvas) {
    return canvas.getContext('webgl2') || console.error('WebGL 2 não está disponível no seu navegador.');
}

export function autoResizeCanvas(canvas) {
    const expandFullScreen = () => {
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
    };
    expandFullScreen();

    window.addEventListener('resize', expandFullScreen);
}

export async function loadVertexShader(gl, name) {
    let shaderString = null;
    await fetch('/Shaders/Vertex/' + name + '.vert')
        .then(response => response.text())
        .then(text => shaderString = text.trim())

    let shader;

    shader = gl.createShader(gl.VERTEX_SHADER);

    gl.shaderSource(shader, shaderString);
    gl.compileShader(shader);

    if (!gl.getShaderParameter(shader, gl.COMPILE_STATUS)) {
        console.error(gl.getShaderInfoLog(shader));
        return null;
    }

    return shader;
}

export async function loadFragmentShader(gl, name) {
    let shaderString = null;
    await fetch('/Shaders/Fragment/' + name + '.frag')
        .then(response => response.text())
        .then(text => shaderString = text.trim())

    let shader;

    shader = gl.createShader(gl.FRAGMENT_SHADER);

    gl.shaderSource(shader, shaderString);
    gl.compileShader(shader);

    if (!gl.getShaderParameter(shader, gl.COMPILE_STATUS)) {
        console.error(gl.getShaderInfoLog(shader));
        return null;
    }

    return shader;
}