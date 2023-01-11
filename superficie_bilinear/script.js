let cnv = document.getElementById("myCanvas");
let ctx = cnv.getContext("2d");
ctx.fillStyle = "#FF0000";

const h = cnv.height;
const w = cnv.width;
const o = initCanvas(ctx, h, w);

window.onload = function() 
{
    document.getElementById('SupBilinear').addEventListener('click', clicked);
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

  
  function bilinearSuperficiesClicked() {
    let zBuffer = initZBuffer(w, h);
    let objects = drawSurfaces();   
  
    zBufferObjects(o, zBuffer, objects);
  
    drawZBuffer(ctx, zBuffer, w, h);
  
    document.getElementById('btnRotacao').onclick = function()
    {            
        let degree = Number(document.getElementById('grau').value) * (Math.PI / 180);
  
        if(document.getElementById('eixoX').checked)
            X_rotation(objects, degree);
        else if(document.getElementById('eixoY').checked)
            Y_rotation(objects, degree);
        else if(document.getElementById('eixoZ').checked)  
            Z_rotation(objects, degree);
  
        zBuffer = initZBuffer(w, h);
  
        zBufferObjects(o, zBuffer, objects);
  
        drawZBuffer(ctx, zBuffer, w, h);
    }
  }
    
  function clicked() {
    ctx.clearRect(0, 0, cnv.width, cnv.height);
    document.getElementById('SupBilinear').checked = true
    //disableElements(false, false, false, false, false, true, true, true, true, true, true, true, true, true)
    
    if(document.getElementById('SupBilinear').checked) { 
        bilinearSuperficiesClicked()
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

function drawSurfaces()
{
    let surfaces = [];
    //Objeto verde
    surfaces.push({ x: 0, y: 0, z: 0 });
    surfaces.push({ x: 20, y: 0, z: 0 });
    surfaces.push({ x: 0, y: 0, z: 80 });
    surfaces.push({ x: 20, y: 0, z: 80 });
    
    surfaces.push({ x: 0, y: 0, z: 0 });
    surfaces.push({ x: 0, y: 40, z: 0 });
    surfaces.push({ x: 0, y: 0, z: 80 });
    surfaces.push({ x: 0, y: 40, z: 80 });

    surfaces.push({ x: 0, y: 0, z: 80 });
    surfaces.push({ x: 20, y: 0, z: 80 });
    surfaces.push({ x: 0, y: 40, z: 80 });
    surfaces.push({ x: 20, y: 40, z: 80 });

    surfaces.push({ x: 0, y: 0, z: 0 });
    surfaces.push({ x: 20, y: 0, z: 0 });
    surfaces.push({ x: 0, y: 40, z: 0 });
    surfaces.push({ x: 20, y: 40, z: 0 });

    surfaces.push({ x: 0, y: 40, z: 0 });
    surfaces.push({ x: 20, y: 40, z: 0 });
    surfaces.push({ x: 0, y: 40, z: 80 });
    surfaces.push({ x: 20, y: 40, z: 80 });
    
    //Objeto vermelho
    surfaces.push({ x: 20, y: 0, z: 0 });
    surfaces.push({ x: 100, y: 0, z: 0 });
    surfaces.push({ x: 20, y: 40, z: 0 });
    surfaces.push({ x: 100, y: 40, z: 0 });

    //Objeto amarelo
    surfaces.push({ x: 20, y: 0, z: 0 });
    surfaces.push({ x: 20, y: 40, z: 0 });
    surfaces.push({ x: 20, y: 0, z: 80 });
    surfaces.push({ x: 20, y: 40, z: 80 });

    //Objeto azul
    surfaces.push({ x: 20, y: 0, z: 80 });
    surfaces.push({ x: 100, y: 0, z: 0 });
    surfaces.push({ x: 20, y: 40, z: 80 });
    surfaces.push({ x: 100, y: 40, z: 0 });

    //Objeto marrom
    surfaces.push({ x: 100, y: 0, z: 0 });
    surfaces.push({ x: 120, y: 0, z: 0 });
    surfaces.push({ x: 100, y: 40, z: 0 });
    surfaces.push({ x: 120, y: 40, z: 0 });

    return surfaces;
}

function interpolation(c00, c10, c01, c11) 
{
    let coordinates = [];
    for (let u = 0; u <= 1; u += 0.002) {
        for (let v = 0; v <= 1; v += 0.002) {
            coordinates.push({
                x: (c00.x * (1 - u) * (1 - v) + c10.x * v * (1 - u) +
                    c01.x * (1 - v) * u + c11.x * u * v),
                y: (c00.y * (1 - u) * (1 - v) + c10.y * v * (1 - u) +
                    c01.y * (1 - v) * u + c11.y * u * v),
                z: (c00.z * (1 - u) * (1 - v) + c10.z * v * (1 - u) +
                    c01.z * (1 - v) * u + c11.z * u * v)
            });
        }
    }
    return coordinates;
}

function zBufferObjects(origin, zBuffer, coordinates) 
{
    //Objeto verde
    calcZBuffer(origin, zBuffer, interpolation(coordinates[0], coordinates[1], coordinates[2], coordinates[3]), [0, 255, 0]);
    calcZBuffer(origin, zBuffer, interpolation(coordinates[4], coordinates[5], coordinates[6], coordinates[7]), [0, 255, 0]);
    calcZBuffer(origin, zBuffer, interpolation(coordinates[8], coordinates[9], coordinates[10], coordinates[11]), [0, 255, 0]);
    calcZBuffer(origin, zBuffer, interpolation(coordinates[12], coordinates[13], coordinates[14], coordinates[15]), [0, 255, 0]);
    calcZBuffer(origin, zBuffer, interpolation(coordinates[16], coordinates[17], coordinates[18], coordinates[19]), [0, 255, 0]);
    
    //Objeto vermelho
    calcZBuffer(origin, zBuffer, interpolation(coordinates[20], coordinates[21], coordinates[22], coordinates[23]), [255, 0, 0]);
    
    //Objeto amarelo
    calcZBuffer(origin, zBuffer, interpolation(coordinates[24], coordinates[25], coordinates[26], coordinates[27]), [255, 255, 0]);
    
    //Objeto azul
    calcZBuffer(origin, zBuffer, interpolation(coordinates[28], coordinates[29], coordinates[30], coordinates[31]), [0, 0, 255]);

    //Objeto marrom
    calcZBuffer(origin, zBuffer, interpolation(coordinates[32], coordinates[33], coordinates[34], coordinates[35]), [160, 80, 0]);
}

