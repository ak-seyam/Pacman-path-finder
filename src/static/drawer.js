
var element_colors = {
  WALL: "grey",
  PLAYER: "lightblue",
  TRAGET: "green",
  EMPTY: "white",
  RANDOM: getRandomColor
};

function getRandomColor() {
  var letters = '0123456789ABCDEF';
  var color = '#';
  for (var i = 0; i < 6; i++) {
    color += letters[Math.floor(Math.random() * 16)];
  }
  return color;
}


function draw_map_element_arc(x, y, x_size, y_size, color, canv) {
  (x = x * x_size), (y = y * y_size);

  canv.beginPath();
  canv.arc(x + x_size / 2, y + y_size / 2, x_size / 3, 0, 2 * Math.PI);
  canv.fillStyle = color;
  canv.stroke();
  canv.fill();
  canv.closePath();
}



function draw_map_element(x, y, x_size, y_size, element, canv) {
  x = x*x_size, y = y*y_size;
  
  canv.beginPath();
  canv.rect(x, y, x_size, y_size);
  canv.fillStyle = element_colors[element];
  canv.stroke();
  canv.fill();
  canv.closePath();
}


function draw_node_id(x, y, id,x_size,y_size, canv) {
  x = x * x_size + x_size / 3;
  y = y*y_size + (y_size *2.5 )/4
  
  canv.beginPath();
  canv.font = "16px Arial";
  canv.fontalign = "center";
  canv.fillText(id, x, y);
  canv.closePath();

}


export { draw_map_element, draw_node_id, draw_map_element_arc, getRandomColor ,element_colors};