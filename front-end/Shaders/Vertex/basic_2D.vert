#version 300 es
precision highp float;

in vec3 aVertexPosition;

void main(void){
    gl_Position = vec4(aVertexPosition,1);
}
