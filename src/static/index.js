// import { wall_img, player_img, space_img, box_img } from "./assets_loader.js";
var width = 480;
var height = 360;

var canvas_back = document.createElement("canvas");
canvas_back.setAttribute("width", width);
canvas_back.setAttribute("height", height);
canvas_back.setAttribute("class", "back_canv");
// canvas_back.setAttribute("z-index", -1);
document.body.appendChild(canvas_back);
var ctx = canvas_back.getContext("2d");

var canvas_2 = document.createElement("canvas");
canvas_2.setAttribute("width", width);
canvas_2.setAttribute("height", height);
document.body.appendChild(canvas_2);
var ctx_2 = canvas_2.getContext("2d");

var element_colors = {
  WALL: "grey",
  PLAYER: "lightblue",
  TRAGET: "green",
  EMPTY: "white",
};
var map = fetch("http://127.0.0.1:5000/map")
  .then((response) => response.json())
  .then((data) => {
    const points = data.map;
    const map_width = data.width;
    const map_height = data.height;
    const [step_x, step_y] = canvas_step(map_width,map_height);
    points.forEach((point) => {
      const x = point.location.x * step_x
      const y = point.location.y * step_y
      draw_element(x, y, step_x,step_y, point.content, ctx);
      if (point.node_id != null)
        draw_id(x + step_x /3, y + step_y *3/4, point.node_id, ctx_2);
        

    });
  });

function canvas_step( map_width, map_height) {
  const canvas_width = width;
  const canvas_height = height;
  const step_x = parseInt(canvas_width / map_width);
  const step_y = parseInt(canvas_height / map_height);

  return [step_x, step_y];
}

function draw_element(x, y, x_size, y_size, element, canv) {
  canv.beginPath();
  canv.rect(x, y, x_size, y_size);
  canv.fillStyle = element_colors[element];
  // canv.fillStyle("red");
  canv.stroke();
  canv.fill();
  canv.closePath();
}

function draw_id(x,y,id,canv){
  canv.beginPath();
  canv.font = "12px Arial"
  canv.fontalign = "center"
  canv.fillText(id,x,y)
}
function draw() {
  // ctx.clearRect(0, 0, canvas.width, canvas.height);
  // draw_element(0, 0,"wall");

  // points.forEach(element => {

  // });
  requestAnimationFrame(draw);
}

function draw_map() {}
// draw_element(50, 50, "wall", ctx);
draw();
