
const ctx = document.getElementById("output").getContext('2d');
const screenWidth = 200;
const screenHeight = 200;

// one value for each pixel in our screen
const depthBuffer = new Array(screenWidth * screenHeight);

// create buffer for color output
const numChannels = 3; // R G B
const colorBuffer = new Array(screenWidth * screenHeight * numChannels);

/**
 * Represents a 2D box
 * @class
 */
class Box {
  /** @member {Object} position of the box storing x,y,z coordinates */
  position;
  /** @member {Object} size of the box storing width and height */
  size;
  /** @member {Object} color of the box given in RGB */
  color;

  constructor (props) {
    this.position = props.position;
    this.size = props.size;
    this.color = props.color;
  }

  /**
   * Check if given point is in box
   * @param {Number} px coordinate of the point
   * @param {Number} py coordinate of the point
   * @return {Boolean} point in box
   */
  pointInBox (px,py) {
    return this.position.x < px && this.position.x + this.size.width > px
        && this.position.y < py && this.position.y + this.size.height > py;
  }
}

a = 2*Math.PI
b = Math.PI
t = 25


const boxes = [
    // blue box
    new Box({
      position: { x: 20, y: 30, z: 10 },
      size: { width: 50, height: 50 },
      color: { r: 0, g: 0, b: 255 }
    }),
    // red box
    new Box({
      position: { x: 75, y: 50, z: 5 },
      size: { width: 50, height: 50 },
      color: { r: 255, g: 0, b: 0 }
    }),
    // yellow box
    new Box({
      position: { x: 40, y: 70 , z: 10 },
      size: { width: 50, height: 50 },
      color: { r: 255, g: 255, b: 0 }
    }),
    // green box
    new Box({
      position: { x: 50, y: 20, z: 5 },
      size: { width: 50, height: 50 },
      color: { r: 0, g: 255, b: 0 }
    }),
    // white box
    new Box({
      position: { x: 0, y: 0, z: 2 },
      size: { width: 50, height: 50 },
      color: { r: 255, g: 255, b: 255 }
    })
  ]




/*
const boxes = [
    // blue box
    new Box({
      position: { x: 20, y: 30, z: 20*20 + 30 },
      size: { width: 50, height: 50 },
      color: { r: 0, g: 0, b: 255 }
    }),
    // red box
    new Box({
      position: { x: 75, y: 50, z: 3*75 - 2*50 + 5 },
      size: { width: 50, height: 50 },
      color: { r: 255, g: 0, b: 0 }
    }),
    // yellow box
    new Box({
      position: { x: 30 + Math.cos(a)* t, y: 50 + Math.sin(a)*t, z: 10 + t },
      size: { width: 50, height: 50 },
      color: { r: 255, g: 255, b: 0 }
    }),
    // green box
    new Box({
      position: { x: 100 + 30*Math.cos(a)*Math.cos(b), y: 50 + 30*Math.cos(a)*Math.sin(b), z: 20 + 30*Math.sin(a) },
      size: { width: 50, height: 50 },
      color: { r: 0, g: 255, b: 0 }
    }),
    // white box
    new Box({
      position: { x: 0, y: 0, z: 10 },
      size: { width: 50, height: 50 },
      color: { r: 255, g: 255, b: 255 }
    })
  ]
*/

const varyZ = document.getElementById('varyz');
varyZ.onchange = draw;

function draw () {
  // clear depth buffer of previous frame
  depthBuffer.fill(10);
  for(const box of boxes) {
    for(let x = 0; x < screenWidth; x++) {
      for(let y = 0; y < screenHeight; y++) {
        // check if our pixel is within the box
        if (box.pointInBox(x,y)) {
          // check if this pixel of our box is covered by something else
          // compare depth value in depthbuffer against box position
          if (depthBuffer[x + y * screenWidth] < box.position.z) {
            // something is already closer to the viewpoint that our current primitive, don't draw this pixel:
            if (!varyZ.checked) continue;
            if (depthBuffer[x + y * screenWidth] < box.position.z + Math.sin((x+y))*Math.cos(x)*5) continue;
          }
          // we passed the depth test, put our current depth value in the z-buffer
          depthBuffer[x + y * screenWidth] = box.position.z;
          // put the color in the color buffer, channel by channel
          colorBuffer[(x + y * screenWidth)*numChannels + 0] = box.color.r;
          colorBuffer[(x + y * screenWidth)*numChannels + 1] = box.color.g;
          colorBuffer[(x + y * screenWidth)*numChannels + 2] = box.color.b;
        }
      }
    }
  }

  // convert to rgba for presentation
  const oBuffer = new Uint8ClampedArray(screenWidth*screenHeight*4);
  for (let i=0,o=0; i < colorBuffer.length; i+=3,o+=4) {
  oBuffer[o]=colorBuffer[i];
  oBuffer[o+1]=colorBuffer[i+1];
  oBuffer[o+2]=colorBuffer[i+2];
  oBuffer[o+3]=255;
  }
  ctx.putImageData(new ImageData(oBuffer, screenWidth, screenHeight),0,0);
}

document.getElementById('blueZ').oninput = e=>{boxes[0].position.z=parseInt(e.target.value,10);draw()};
document.getElementById('redZ').oninput = e=>{boxes[1].position.z=parseInt(e.target.value,10);draw()};
document.getElementById('yellowZ').oninput = e=>{boxes[2].position.z=parseInt(e.target.value,10);draw()};
document.getElementById('greenZ').oninput = e=>{boxes[3].position.z=parseInt(e.target.value,10);draw()};
document.getElementById('whiteZ').oninput = e=>{boxes[4].position.z=parseInt(e.target.value,10);draw()};


draw();



/*
for(let x = 10; x <= 30; x++) {
    for(let y = 20; y <= 40; y++) {
      // create blue box with x,y values
      boxes.push(new Box({
        position: { x: x, y: y, z: x*x + y },
        size: { width: 50, height: 50 },
        color: { r: 0, g: 0, b: 255 }
      }));
    }
  }
  for(let x = 50; x <= 100; x++) {
    for(let y = 30; y <= 80; y++) {
      // create red box with x,y values
      boxes.push(new Box({
        position: { x: x, y: y, z: 3*x - 2*y + 5 },
        size: { width: 50, height: 50 },
        color: { r: 255, g: 0, b: 0 }
      }));
    }
  }
  let t = 0;
  while(t <= 50) {
    for(let a = 0; a < 2*Math.PI; a += 0.1) {
      // create yellow box with t,a values
      boxes.push(new Box({
        position: { x: 30 + Math.cos(a)*t, y: 50 + Math.sin(a)*t, z: 10 + t },
        size: { width: 50, height: 50 },
        color: { r: 255, g: 255, b: 0 }
      }));
    }
    t += 1;
  }
  for(let a = 0; a < 2*Math.PI; a += 0.1) {
    for(let b = 0; b < 2*Math.PI; b += 0.1) {
      // create green box with a,b values
      boxes.push(new Box({
        position: { x: 100 + 30* Math.cos(a)* Math.cos(b), y: 50 + 30* Math.cos(a)* Math.sin(b), z: 20 + 30* Math.sin(a) },
        size: { width: 50, height: 50 },
        color: { r: 0, g: 255, b: 0 }
      }));
    }
  }
// create white box
boxes.push(new Box({
    position: { x: 0, y: 0, z: 0 },
    size: {width: 40, height: 40 },
    color: { r: 255, g: 255, b: 255 }
}));

*/