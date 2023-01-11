let cnv = document.getElementById("myCanvas");
let ctx = cnv.getContext("2d");
ctx.fillStyle = "#FF0000";

const h = cnv.height;
const w = cnv.width;
const o = initCanvas(ctx, h, w);

window.onload = function() 
{
    document.getElementById('VarrRot').addEventListener('click', clicked);
    clicked();
}

function sweepClicked() {
    //disableElements(true, true, true, true, true, false, true, true, true, true, true ,true, true)
    
    ctx.beginPath();
    ctx.moveTo(500, 0);
    ctx.lineTo(500, 500);
    ctx.stroke();
  
    let isDown = false;
    let x1, y1, x2, y2;
    let coordinates1 = [];
    let coordinates2 = [];
    let ax = cnv.width/2;
    
    cnv.onmousedown = function(evt)
    {
        if (isDown == false) {
            isDown = true;
  
            ctx.clearRect(0, 0, cnv.width, cnv.height);
  
            coordinates1 = [];
            coordinates2 = [];
  
            ctx.beginPath();
            ctx.moveTo(500, 0);
            ctx.lineTo(500, 500);
            ctx.stroke();
  
            x1 = evt.clientX - cnv.offsetLeft;
            y1 = evt.clientY - cnv.offsetTop;
        }
    }
  
    cnv.onmousemove = function(evt)
    {
        if(isDown){
            x2 = evt.clientX - cnv.offsetLeft;
            y2 = evt.clientY - cnv.offsetTop;
  
            ctx.fillRect(x2, y2, 1, 1);
            coordinates1.push({x: x2, y: y2, z: 0});
        
            x1 = x2;
            y1 = y2;
        }
    }
  
    cnv.onmouseup = function(evt)
    {
        if (isDown == true) 
        {
            isDown = false;
            x2 = evt.clientX - cnv.offsetLeft;
            y2 = evt.clientY - cnv.offsetTop;
  
            ctx.fillRect(x2, y2, 1, 1);
            coordinates1.push({x: x2, y: y2, z: 0});
  
            sweep(coordinates1, coordinates2, ax);
        }
    }
  
    document.getElementById('aplicarVarredura').onclick = function()
    {
        let cavaleiraCoords = parallelProjection(coordinates2);
        drawSweep(cavaleiraCoords, ctx, 'black', ax);
  
        coordinates1 = [];
        coordinates2 = [];        
    }
  }

function clicked() {
    ctx.clearRect(0, 0, cnv.width, cnv.height);
    document.getElementById('VarrRot').checked = true
    //disableElements(false, false, false, false, false, true, true, true, true, true, true, true, true, true)
    
    if(document.getElementById('VarrRot').checked) {
        document.getElementById('aplicarVarredura').disabled = false;
        sweepClicked() 
      }
} 


function sweep(coordinates, circleCoordinates, ax)
{
    for(let i = 0; i < coordinates.length; i++)
    {
        let ratio = Math.abs(coordinates[i].x - ax);
        let x = 0;
        let z = ratio;
        let d = 3 - (2 * ratio);

        while(x <= z){
            if(d < 0)
            {
                d += (4 * x) + 6;
            }
            else
            {
                d += 4 * (x - z) + 10;
                z--;
            }
            x++;
            circleCoordinates.push({x: x, y: coordinates[i].y, z: z});
            circleCoordinates.push({x: z, y: coordinates[i].y, z: x});
            circleCoordinates.push({x: -x, y: coordinates[i].y, z: z});
            circleCoordinates.push({x: -z, y: coordinates[i].y, z: x});
            circleCoordinates.push({x: -x, y: coordinates[i].y, z: -z});
            circleCoordinates.push({x: -z, y: coordinates[i].y, z: -x});
            circleCoordinates.push({x: x, y: coordinates[i].y, z: -z});
            circleCoordinates.push({x: z, y: coordinates[i].y, z: -x});
        }
    }
}

function drawSweep(coordinates, ctx, color, offset)
{
    for(let i = 0; i < coordinates.length; i++){
        ctx.fillStyle = color;
        ctx.fillRect(coordinates[i].x + offset, coordinates[i].y, 1, 1);
    }
}

function parallelProjection(coordinates) 
{
    let projection = [];

    for (let i = 0; i < coordinates.length; i++) 
        projection.push({x: coordinates[i].x + coordinates[i].z * Math.cos(45 * Math.PI/180), y: coordinates[i].y + coordinates[i].z * Math.sin(45 * Math.PI/180), z: 0});
    
    return projection;
}

function initCanvas(ctx, h, w) 
{
    ctx.clearRect(0, 0, h, w);
    return {x: parseInt(w / 2), y: parseInt(h / 2)}
}
