let cnv = document.getElementById("myCanvas");
let ctx = cnv.getContext("2d");
ctx.fillStyle = "#FF0000";

const h = cnv.height;
const w = cnv.width;
const o = initCanvas(ctx, h, w);

window.onload = function() 
{
    // document.getElementById('ZBuffer').addEventListener('click', clicked);
    // document.getElementById('SupBilinear').addEventListener('click', clicked);
    // document.getElementById('VarrRot').addEventListener('click', clicked);
    document.getElementById('Iluminacao').addEventListener('click', clicked);
    clicked();
}


function lightningModelClicked() {
  
    //disableElements(true, true, true, true, true, true, false, false, false, false, false, false, false)
  
    let zBuffer = initZBuffer(w, h);
    
    let ball = ballCoordinates(0, 50); 
    let flat = flatCoordinates(0, 100, 0, 100); 
    
    calcZBuffer(o, zBuffer, ball, [255, 90, 255]); 
    calcZBuffer(o, zBuffer, flat, [0, 0, 255]); 
  
    drawZBuffer(ctx, zBuffer, w, h);
  
    let Ia = Number(document.getElementById('Ia').value);
    let Ka = Number(document.getElementById('Ka').value);
    let Il = Number(document.getElementById('Il').value);
  
    document.getElementById('aplicarIluminacao1').onclick = function()
    {
        zBuffer = initZBuffer(w, h);
  
        lightningModel_1(ball, Ia, Ka, Il, 0.3, 'esfera', luz = [100, 0, 100], o, zBuffer, cor = [255, 90, 255]);
        lightningModel_1(flat, Ia, Ka, Il, 0.7, 'plano', luz = [100, 0, 100], o, zBuffer, cor = [0, 0, 255]);
  
        drawZBuffer(ctx, zBuffer, w, h);
    }
    document.getElementById('aplicarIluminacao2').onclick = function()
    {
        let k = Number(document.getElementById('k').value);
        let n = Number(document.getElementById('n').value);
  
        zBuffer = initZBuffer(w, h);
  
        lightningModel_2(ball, Ia, Ka, Il, 0.3, k, 0.8, n, 'esfera', luz = [100, 0, 100], observador = [0, 0, 100], o, zBuffer, cor = [255, 90, 255]);
        lightningModel_2(flat, Ia, Ka, Il, 0.7, k, 0.4, n, 'plano', luz = [100, 0, 100], observador = [0, 0, 100], o, zBuffer, cor = [0, 0, 255]);
  
        drawZBuffer(ctx, zBuffer, w, h);
    }
  }

function clicked() {
    document.getElementById('Iluminacao').checked = true
    ctx.clearRect(0, 0, cnv.width, cnv.height);
    //disableElements(false, false, false, false, false, true, true, true, true, true, true, true, true, true)
    
    if(document.getElementById('Iluminacao').checked) { 
        document.getElementById('Ia').disabled = false;
        document.getElementById('Ka').disabled = false;
        document.getElementById('Il').disabled = false;
        document.getElementById('k').disabled = false;
        document.getElementById('n').disabled = false;
        document.getElementById('aplicarIluminacao1').disabled = false;
        document.getElementById('aplicarIluminacao2').disabled = false;
        document.getElementById('Ia').disabled = false;

      lightningModelClicked()
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


function ballCoordinates(origin, ratio) 
{
    let ball = [];
    let inc = 0.01;
            
    for (let a = 0; a <= 2 * Math.PI; a += inc){
        for (let b = 0; b <= 2 * Math.PI; b += inc){
            ball.push({x: Math.round(origin + ratio * Math.cos(a) * Math.cos(b)), y: Math.round(origin + ratio * Math.cos(a) * Math.sin(b)), z: Math.round(origin + ratio * Math.sin(a))});
        }
    }
    
    return ball;
}

function flatCoordinates(x1, x2, y1, y2) 
{
    let flat = [];

    for (let i = x1; i < x2; i++){
        for (let j = y1; j < y2; j++){
            flat.push({ x: i, y: j, z: 0 });
        }
    }
            
    return flat;
}

function scalarProduct(v1, v2) 
{
    var result = 0;

    for (var i = 0; i < 3; i++)
        result += v1[i] * v2[i];
    
    return result;
}

function norm(v1)
{
    var result = 0;

    for (var i = 0; i < 3; i++)
        result += v1[i] * v1[i];
    
    return Math.sqrt(result);
}

function distance(p1, p2)
{
    var result = 0;

    for (var i = 0; i < 3; i++)
        result += Math.pow(p1[i] - p2[i], 2);
    
    return Math.sqrt(result);
}

function lightningModel_1(coordinates, Ia, Ka, Il, Kd, type, light = [100, 0, 100], origin, zBuffer, color)
{
    let I = 0;
    let normal = [0, 0, 0];

    for(let i = 0; i < coordinates.length; i++)
    {
        if(type == 'plano')
            normal = [coordinates[i].x, coordinates[i].y, 1];
        else if(type == 'esfera')
            normal = [coordinates[i].x, coordinates[i].y, coordinates[i].z];

        cosAng = scalarProduct(normal, light)/(norm(normal)*norm(light));

        I = Ia*Ka + Il*Kd*cosAng;

        let x = Math.round(coordinates[i].x + origin.x);
        let y = Math.round(origin.y - coordinates[i].y);
        if (zBuffer[x] != undefined && zBuffer[x][y] != undefined && coordinates[i].z < zBuffer[x][y].val) 
        {
            zBuffer[x][y].val = coordinates[i].z;
            zBuffer[x][y].color = color.map(canal => canal * I);;
        }
    }  
}

function lightningModel_2(coordinates, Ia, Ka, Il, Kd, k, Ks, n, type, light = [100, 0, 100], observer = [0, 0, 100], origin, zBuffer, color)
{
    let I = 0;
    let normal = [0, 0, 0];
    let alpha = 0;
    let d = 0;

    for(let i = 0; i < coordinates.length; i++)
    {
        if(type == 'plano')
            normal = [coordinates[i].x, coordinates[i].y, 1];
        else if(type == 'esfera')
            normal = [coordinates[i].x, coordinates[i].y, coordinates[i].z];

        cosAng = scalarProduct(normal, light)/(norm(normal)*norm(light));
        alpha = Math.acos(scalarProduct(observer, light)/(norm(observer)*norm(light))) - 2*Math.acos(cosAng);
        cosAlpha= Math.cos(alpha);
        
        d = distance([coordinates[i].x, coordinates[i].y, coordinates[i].z], light);

        I = Ia*Ka + (Il/(d+k))*(Kd*cosAng + Ks*Math.pow(cosAlpha, n));

        let x = Math.round(coordinates[i].x + origin.x);
        let y = Math.round(origin.y - coordinates[i].y);
        if (zBuffer[x] != undefined && zBuffer[x][y] != undefined && coordinates[i].z < zBuffer[x][y].val) 
        {
            zBuffer[x][y].val = coordinates[i].z;
            zBuffer[x][y].color = color.map(canal => canal * I);;
        }
    }
}
