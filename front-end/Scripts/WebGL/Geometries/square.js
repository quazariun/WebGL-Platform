import { loadFile } from "../../Handlers/handler.js";
import { loadVertexShader, loadFragmentShader } from "../../Libs/utils.js";

export default async function init_square(gl) {
    gl.clearColor(0.509, 0.509, 0.509, 1);
    gl.clear(gl.COLOR_BUFFER_BIT);

    let square = await loadFile("square");

    let vshader = await loadVertexShader(gl, "basic_2D");
    let fshader = await loadFragmentShader(gl, "basic_2D");

    let program = gl.createProgram();
    gl.attachShader(program, vshader);
    gl.attachShader(program, fshader);
    gl.linkProgram(program);

    if (!gl.getProgramParameter(program, gl.LINK_STATUS)) {
        console.error('Could not initialize shaders');
    }

    gl.useProgram(program);

    program.aVertexPosition = gl.getAttribLocation(program, 'aVertexPosition');

    // Setting up the VBO
    let squareVertexBuffer = gl.createBuffer();
    gl.bindBuffer(gl.ARRAY_BUFFER, squareVertexBuffer);
    gl.bufferData(gl.ARRAY_BUFFER, new Float32Array(square.vertices), gl.STATIC_DRAW);

    // Setting up the IBO
    let squareIndexBuffer = gl.createBuffer();
    gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, squareIndexBuffer);
    gl.bufferData(gl.ELEMENT_ARRAY_BUFFER, new Uint32Array(square.indices), gl.STATIC_DRAW);

    // Clean
    gl.bindBuffer(gl.ARRAY_BUFFER, null);
    gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, null);


    draw();

    // We call draw to render to our canvas
    function draw() {
        // Clear the scene
        gl.clear(gl.COLOR_BUFFER_BIT | gl.DEPTH_BUFFER_BIT);
        gl.viewport(0, 0, gl.canvas.width, gl.canvas.height);

        // Use the buffers we've constructed
        gl.bindBuffer(gl.ARRAY_BUFFER, squareVertexBuffer);
        gl.vertexAttribPointer(program.aVertexPosition, 3, gl.FLOAT, false, 0, 0);
        gl.enableVertexAttribArray(program.aVertexPosition);

        // Bind IBO
        gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, squareIndexBuffer);

        // Draw to the scene using triangle primitives
        gl.drawElements(gl.TRIANGLES, square.indices.length, gl.UNSIGNED_INT, 0);

        // Clean
        gl.bindBuffer(gl.ARRAY_BUFFER, null);
        gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, null);
    }
}