// import { wall_img, player_img, space_img, box_img } from "./assets_loader.js";
import { draw_map_element, draw_node_id } from "./drawer.js";
var width = 4080;
var height = 1080;

var canvas_back = document.createElement("canvas");
canvas_back.setAttribute("width", width);
canvas_back.setAttribute("height", height);
canvas_back.setAttribute("class", "back_canv");
document.body.appendChild(canvas_back);
var ctx_back = canvas_back.getContext("2d");

var canvas_nodes = document.createElement("canvas");
canvas_nodes.setAttribute("width", width);
canvas_nodes.setAttribute("height", height);
document.body.appendChild(canvas_nodes);
var ctx_nodes = canvas_nodes.getContext("2d");

const options = {
  draw_wall: false,
  draw_target: false,
  draw_player: false,
  draw_ids: false,
};

const element_types = {
  WALL: "WALL",
  PLAYER: "PLAYER",
  TRAGET: "TRAGET",
  EMPTY: "EMPTY",
};

const test_expantion = [
  0,
  0,
  1,
  2,
  3,
  14,
  36,
  100,
  67,
  68,
  69,
  202,
  246,
  263,
  272,
  262,
  245,
  244,
  261,
  271,
  281,
  282,
  221,
  222,
  283,
  284,
  250,
  251,
  238,
  252,
  253,
  254,
  285,
  275,
  276,
  239,
  256,
  257,
  268,
  280,
  267,
  266,
  279,
  278,
  265,
  264,
  277,
  286,
  287,
  258,
  232,
  211,
  200,
  288,
];

const map_data = fetch("http://127.0.0.1:5000/map").then((response) =>
  response.json()
);

// map_data.then(async (map_data) => {
//   draw_map(map_data,options)
//   const [step_x, step_y] = step_map(map_data);

//   async function draw_routes(node_id,last_draw) {
//     const res = await fetch(`http://127.0.0.1:5000/map/path?from=${node_id}`);

//     const routes = await res.json();
//     for (node_id in routes) {
//       let element = element_types.TRAGET;
//       if (parseInt(node_id) === last_draw){
//         element = element_types.PLAYER
//       }
//       const route = routes[node_id];
//       route.forEach((point) => {
//         const x = point.location.x * step_x
//         const y = point.location.y * step_y
//         draw_map_element(x,y,step_x,step_y,element,ctx)
//     })

//       };
//     }

//   for (let i = 0; i < test_expantion.length; i++) {
//     const p = get_point_by_node_id(map_data,test_expantion[i])
//     const x = p.location.x * step_x
//     const y = p.location.y * step_y
//     let last_draw = NaN
//     if (i>0)
//       last_draw = test_expantion[i-1]
//     setTimeout(async ()=>{
//     draw_map_element(x, y, step_x, step_y,element_types.PLAYER,ctx)
//     await draw_routes(test_expantion[i],last_draw);

//     },800*i)
//   }

//   test_expantion.forEach(async (node_id)=>{
//   })

// });

function get_point_by_node_id(maze_map, node_id) {
  const points = maze_map.map;
  for (let p in points) {
    const id = parseInt(points[p].node_id);
    if (id == node_id) {
      return points[p];
    }
  }
}

function canvas_step(map_width, map_height) {
  const canvas_width = width;
  const canvas_height = height;
  const step_x = parseInt(canvas_width / map_width);
  const step_y = parseInt(canvas_height / map_height);

  return [step_x, step_y];
}

function draw_map(map_data, options,canv) {
  const points = map_data.map;
  const [step_x, step_y] = step_map(map_data);
  points.forEach((point) => {
    const x = point.location.x * step_x;
    const y = point.location.y * step_y;
    let element = point.content;
    if (element == element_types.WALL) {
      element = options.draw_wall ? element : element_types.EMPTY;
    } else if (element == element_types.TRAGET) {
      element = options.draw_target ? element : element_types.EMPTY;
    } else if (element == element_types.PLAYER) {
      element = options.draw_player ? element : element_types.EMPTY;
    }
    draw_map_element(x, y, step_x, step_y, element, canv);

    if (options.draw_ids)
      if (point.node_id != null) {
        draw_node_id(
          x + step_x / 3,
          y + (step_y * 3) / 4,
          point.node_id,
          ctx_nodes
        );
      }
  });
}

function step_map(map_data) {
  const map_width = map_data.width;
  const map_height = map_data.height;
  return canvas_step(map_width, map_height);
}

function draw() {
  // ctx.clearRect(0, 0, canvas.width, canvas.height);
  // draw_element(0, 0,"wall");
  // points.forEach(element => {
  //
  // });
  requestAnimationFrame(draw);
}

// draw_element(50, 50, "wall", ctx);
// draw();

async function main() {
  const map_data = await fetch("http://127.0.0.1:5000/map").then((res) =>
    res.json()
  );

  const options = {
  draw_wall: true,
  draw_target: true,
  draw_player: true,
  draw_ids: true,
  
  };
  // draw_map(map_data, { draw_wall: true }, ctx_back);
  draw_map(map_data, options, ctx_back);

  // draw_map(map_data, { draw_ids: true }, ctx_nodes);

}

main();
