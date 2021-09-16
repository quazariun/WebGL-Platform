#version 300 es
precision highp float;

uniform mat4 uProjectionMatrix;
uniform mat4 uModelViewMatrix;

in vec3 aVertexPosition;

void main(void){
      gl_Position = uProjectionMatrix * uModelViewMatrix * vec4(aVertexPosition, 1.0);
}
