var WIDTH;
var HEIGHT;
var ctx;
var paddlex;
var paddleh = 10;
var paddlew = 75;
var rightDown = false;
var leftDown = false;
var canvasMinX = 0;
var canvasMaxX = 0;
var intervalId = 0;

function onKeyDown(evt) {
  if (evt.keyCode == 39) rightDown = true;
  else if (evt.keyCode == 37) leftDown = true;
}

function onKeyUp(evt) {
  if (evt.keyCode == 39) rightDown = false;
  else if (evt.keyCode == 37) leftDown = false;
}

function onMouseMove(evt) {
  if (evt.pageX > canvasMinX && evt.pageX < canvasMaxX) {
    paddlex = evt.pageX - canvasMinX - (paddlew/2);
  }
}

$(document).keydown(onKeyDown);
$(document).keyup(onKeyUp);
$(document).mousemove(onMouseMove);

function init() {
  ctx = $('#canvas')[0].getContext("2d");
  WIDTH = $("#canvas").width()
  HEIGHT = $("#canvas").height()
  paddlex = WIDTH / 2;
  canvasMinX = $("#canvas").offset().left;
  canvasMaxX = canvasMinX + WIDTH;
  intervalId = setInterval(draw, 10);
}
function circle2 (x2,y2,r,check2) {
	if(check2==0){
  ctx.beginPath();
  ctx.arc(x2, y2, r, 0, Math.PI*2, true);
  ctx.closePath();
    ctx.fillStyle="red";
  ctx.fill();
  ctx.fillStyle="black";
  }
}

function circle(x,y,r,check1) {
if (check1==0) {  
  ctx.beginPath();
  ctx.arc(x, y, r, 0, Math.PI*2, true);  
    ctx.fillStyle="blue";  
  ctx.closePath();
  ctx.fill();
   ctx.fillStyle="black";
}
}

function rect(x,y,w,h) {
  ctx.beginPath();
  ctx.rect(x,y,w,h);
  ctx.closePath();
  ctx.fill();
}

function clear() {
  ctx.clearRect(0, 0, WIDTH, HEIGHT);
}
