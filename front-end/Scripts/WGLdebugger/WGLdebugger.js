 let GL_Local;

 export function main(gl) {
     GL_Local = gl;
     createDiv();
     linkCSS();
 }

 function createDiv() {
     var div_main = document.createElement("div");
     div_main.id = 'div-main';

     var div_state = document.createElement("div");
     div_state.id = 'div-state';

     //WebGL elements
     var span_color_clear_value = document.createElement("span");

     div_state.appendChild(span_color_clear_value);

     //Create Toggle to Show and Hide WebGL Status
     let toggle_debugger = document.createElement("button");
     toggle_debugger.id = 'toggle-debugger'
     toggle_debugger.innerHTML = "Show States";
     toggle_debugger.onclick = function() {
         let toggle = document.getElementById("toggle-debugger");
         let state_table = document.getElementById("div-state");
         let style = getComputedStyle(toggle);

         if (style.backgroundColor == "rgb(210, 105, 30)") {
             state_table.style.display = "block";
             toggle.style.backgroundColor = "rgb(31, 156, 161)";
         } else {
             state_table.style.display = "none";
             toggle.style.backgroundColor = "rgb(210, 105, 30)";
         }
     }

     div_main.appendChild(div_state);
     div_main.appendChild(toggle_debugger);
     document.body.appendChild(div_main);
 }

 function linkCSS() {
     var head = document.getElementsByTagName('HEAD')[0];
     var link = document.createElement('link');

     link.rel = 'stylesheet';
     link.type = 'text/css';
     link.href = '/Scripts/WGLdebugger/WGLdebugger.css';

     head.appendChild(link);
 }