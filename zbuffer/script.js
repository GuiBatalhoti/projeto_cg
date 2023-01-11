let cnv = document.getElementById("myCanvas");
let ctx = cnv.getContext("2d");
ctx.fillStyle = "#FF0000";

const h = cnv.height;
const w = cnv.width;
const o = initCanvas(ctx, h, w);

window.onload = function() 
{
    document.getElementById('ZBuffer').addEventListener('click', clicked);
    clicked();
}

function rotateObjects(blueObj, redObj, yellowObj, greenObj, whiteObj, degree) {
    if(document.getElementById('eixoX').checked){
      X_rotation(blueObj, degree);
      X_rotation(redObj, degree);
      X_rotation(yellowObj, degree);
      X_rotation(greenObj, degree);
      X_rotation(whiteObj, degree);
    }
    else if(document.getElementById('eixoY').checked){
      Y_rotation(blueObj, degree);
      Y_rotation(redObj, degree);
      Y_rotation(yellowObj, degree);
      Y_rotation(greenObj, degree);
      Y_rotation(whiteObj, degree);
    }
    else if(document.getElementById('eixoZ').checked){
      Z_rotation(blueObj, degree);
      Z_rotation(redObj, degree);
      Z_rotation(yellowObj, degree);
      Z_rotation(greenObj, degree);
      Z_rotation(whiteObj, degree);
    }
  
  }

  
  function zBufferClicked() {
    let zBuffer = initZBuffer(w, h);
          
    let blueObj = drawBlueObject(10, 30, 20, 40); 
    let redObj = drawRedObject(50, 100, 30, 80); 
    let yellowObj = drawYellowObject(0, 50, 0, 2 * Math.PI); 
    let greenObj = drawGreenObject(0, 2 * Math.PI, 0, 2 * Math.PI); 
    let whiteObj = drawWhiteObect(0, 40); 
  
    calcZBuffer(o, zBuffer, blueObj, [0, 0, 255]); 
    calcZBuffer(o, zBuffer, redObj, [255, 0, 0]); 
    calcZBuffer(o, zBuffer, yellowObj, [255, 255, 0]); 
    calcZBuffer(o, zBuffer, greenObj, [0, 255, 0]); 
    calcZBuffer(o, zBuffer, whiteObj, [255, 255, 255]); 
  
    drawZBuffer(ctx, zBuffer, w, h);
  
    document.getElementById('btnRotacao').onclick = function() {
        let degree = Number(document.getElementById('grau').value) * (Math.PI / 180);
        
        rotateObjects(blueObj, redObj, yellowObj, greenObj, whiteObj, degree)
        zBuffer = initZBuffer(w, h);
  
        calcZBuffer(o, zBuffer, blueObj, [0, 0, 255]); 
        calcZBuffer(o, zBuffer, redObj, [255, 0, 0]); 
        calcZBuffer(o, zBuffer, yellowObj, [255, 255, 0]); 
        calcZBuffer(o, zBuffer, greenObj, [0, 255, 0]); 
        calcZBuffer(o, zBuffer, whiteObj, [255, 255, 255]); 
  
        drawZBuffer(ctx, zBuffer, w, h);
    }
  }

  
  function clicked() {
    ctx.clearRect(0, 0, cnv.width, cnv.height);
    //disableElements(false, false, false, false, false, true, true, true, true, true, true, true, true, true)
    
    if(document.getElementById('ZBuffer').checked) { 
      zBufferClicked()
        } 
  } 

  
function initCanvas(ctx, h, w) 
{
    ctx.clearRect(0, 0, h, w);
    return {x: parseInt(w / 2), y: parseInt(h / 2)}
}

function initZBuffer(w, h) 
{
    let rows = [];
        
    for (let i = 0; i < w; i++) {
        let cols = Array(h);
        for (let j = 0; j < h; j++) {
            cols[j] = { val: Number.MAX_SAFE_INTEGER, color: [0, 0, 0] }
        }
        rows.push(cols);
    }
    
    return rows;
}

function calcZBuffer(origin, zBuffer, coordinates, color) 
{
    for (let i = 0; i < coordinates.length; i++) {
        let x = Math.round(coordinates[i].x + origin.x);
        let y = Math.round(origin.y - coordinates[i].y);
        if (zBuffer[x] != undefined && zBuffer[x][y] != undefined && coordinates[i].z < zBuffer[x][y].val) {
            zBuffer[x][y].val = coordinates[i].z;
            zBuffer[x][y].color = color;
        }
    }    
}

function drawZBuffer(ctx, zBuffer, w, h) 
{
    for (let i = 0; i < w; i++) {
        for (let j = 0; j < h; j++) {
            let color = zBuffer[i][j].color;
            ctx.fillStyle = 'rgb(' + color[0] + ',' + color[1] + ',' + color[2] + ')';
            ctx.fillRect(i, j, 1, 1);
        }
    }
}


function drawBlueObject(x1, x2, y1, y2) 
{
    let blue = [];

    for(let i = x1; i < x2; i++){
        for(let j = y1; j < y2; j++){
            blue.push({x: i, y: j, z: (i*i) + j});
        }
    }

    return blue;
}

function drawRedObject(x1, x2, y1, y2) 
{
    let red = [];
    for (let i = x1; i < x2; i++){
        for (let j = y1; j < y2; j++){
            red.push({x: i, y: j, z: 3 * i - 2 * j + 5});
        }
    }
    
    return red;
}

function drawYellowObject(t1, t2, a1, a2) 
{
    let yellow = [];
    let inc = 0.01;
    
    for (let a = a1; a <= a2; a += inc){
        for (let t = t1; t <= t2; t += 1){
            yellow.push({x: Math.round(30 + t * Math.cos(a)), y: Math.round(50 + t * Math.sin(a)), z: Math.round(10 + t)});
        }
    }
    
    return yellow;
}

function drawGreenObject(a1, a2, b1, b2) 
{
    let green = [];
    let inc = 0.01;
            
    for (let a = a1; a <= a2; a += inc){
        for (let b = b1; b <= b2; b += inc){
            green.push({x: Math.round(100 + 30 * Math.cos(a) * Math.cos(b)), y: Math.round(50 + 30 * Math.cos(a) * Math.sin(b)), z: Math.round(20 + 30 * Math.sin(a))});
        }
    }
    
    return green;
}
      

function drawWhiteObect(origin, side) 
{
    let white = [];
    let x1 = Math.round(origin - side/2);
    let x2 = Math.round(origin + side/2);
    let y1 = Math.round(origin - side/2);
    let y2 = Math.round(origin + side/2);
    let aux1 = Math.round(origin - side/2);
    let aux2 = Math.round(origin + side/2);

    for (let i = x1; i < x2; i++) {
        for (let j = y1; j < y2; j++) {
            white.push({ x: i, y: j, z: aux1 });
        }
    }
    
    for (let i = x1; i < x2; i++) {
        for (let j = y1; j < y2; j++) {
            white.push({ x: i, y: j, z: aux2 });
        }
    }
            
    for (let i = x1; i < x2; i++){
        for (let j = y1; j < y2; j++){
            white.push({ x: i, y: aux1, z: j });
        }
    }

    for (let i = x1; i < x2; i++){
        for (let j = y1; j < y2; j++){
            white.push({ x: i, y: aux2, z: j });
        }
    }

    for (let i = x1; i < x2; i++){
        for (let j = y1; j < y2; j++){
            white.push({ x: aux1, y: i, z: j });
        }
    }
      
    for (let i = x1; i < x2; i++){
        for (let j = y1; j < y2; j++){
            white.push({ x: aux2, y: i, z: j });
        }
    }
            
    return white;
}

function X_rotation(coordinates, alpha) 
{
    for (let i = 0; i < coordinates.length; i++) 
        coordinates[i] = {x: coordinates[i].x, y: Math.round(coordinates[i].y * Math.cos(alpha) + coordinates[i].z * Math.sin(alpha)), z: Math.round(-coordinates[i].y * Math.sin(alpha) + coordinates[i].z * Math.cos(alpha))};
}

function Y_rotation(coordinates, alpha) 
{
    for (let i = 0; i < coordinates.length; i++) 
        coordinates[i] = {x: Math.round(coordinates[i].x * Math.cos(alpha) - coordinates[i].z * Math.sin(alpha)), y: coordinates[i].y, z: Math.round(coordinates[i].x * Math.sin(alpha) + coordinates[i].z * Math.cos(alpha))};
}

function Z_rotation(coordinates, alpha) 
{
    for (let i = 0; i < coordinates.length; i++)
        coordinates[i] = {x: Math.round(coordinates[i].x * Math.cos(alpha) + coordinates[i].y * Math.sin(alpha)), y: Math.round(-coordinates[i].x * Math.sin(alpha) + coordinates[i].y * Math.cos(alpha)), z: coordinates[i].z};
}

