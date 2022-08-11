
const CELLSIZE = 20;
const offset = 0;
const cells = [];
let WIDTH = 0;
let HEIGHT = 0;
let intervalTime = 1000 // 1 second;
let frame = 0;
let generation = 0;
let count = 0;
let color = false;
let pause = false;

let useAlpha = true;



const lerp = (a, b, t) =>{
    return a + (b - a) * t
}

const Rand = (min = 0, max = 1) => { 
    return Math.floor(Math.random() * (max - min)) + min
}

class Color { 
    constructor(r, g, b, a = 1){
        this.r = r;
        this.g = g;
        this.b = b;
        this.a = a;
    }

    toString() {
        return `rgba(${this.r}, ${this.g}, ${this.b}, ${this.a})` 
    }

    static lerpColors(colorA, colorB, alpha){
        let r = lerp(colorA.r, colorB.r, alpha)
        let g = lerp(colorA.g, colorB.g, alpha)
        let b = lerp(colorA.b, colorB.b, alpha)
        let a = lerp(colorA.a, colorB.a, alpha)
        return new Color(r, g, b, a);
    }
}
let blackColor = new Color(0, 0, 0, 1);
let whiteColor = new Color(255, 255, 255, 1);


const requestAnimationFrameHandler = (callback) => {
    if(frame % 2 == 0){
        requestAnimationFrame(callback)
        return;
    }
}

class Cell {
    static _id = 0;
    constructor(position){
        this.deadColor = new Color(Rand(255 * 0.1, 255 * 0.5), Rand(255 * 0.1, 255 * 0.5), Rand(255 * 0.1, 255 * 0.5))
        this.staticColor =  new Color(Rand(0, 255), Rand(0, 255), Rand(0, 255))
        this.aliveColor = new Color(Rand(0, 255), Rand(0, 255), Rand(0, 255), 0.875)
        this.state = 0;
        this.prevState = 0;
        this.pos = position;
        this.neighbors = [];
        this.id = Cell._id++;
        this.body =  document.createElement('div');
        this.body.style.left = `${(position[0] * CELLSIZE)}px`;
        this.body.style.top = `${(position[1] * CELLSIZE)}px`;
        if(this.id == 0){
            this.color = this.state == 0 ? this.deadColor : this.aliveColor;
        }
        else { 
            this.color = this.state == 0 ? cells[count].deadColor : cells[count].aliveColor;
        }
        this.body.style.position = 'absolute';
        this.body.style.width = `${CELLSIZE - 1}px`
        this.body.style.height = `${CELLSIZE - 1}px`
        this.aliveNeighbors = 0;
        this.body.style.backgroundColor = this.color.toString()
        document.body.appendChild(this.body)
        this.body.addEventListener('click', () => {
            this.state = this.state == 1 ? 0 : 1;
            if(color){
                this.color = this.state == 0 ? cells[count].deadColor : cells[count].aliveColor;
            }
            else { 
                this.color = this.state == 0 ? blackColor : whiteColor
            }
            this.body.style.backgroundColor = this.color.toString()
        })
    }
}



const createGrid = (width, height) => {
    WIDTH = width;
    HEIGHT = height;
    for(let x = 0; x < width; x++){
        for(let y = 0; y < height; y++){
            const cell = new Cell([x, y])
            cells.push(cell)
      
            if(Rand(0, 100) > 85){
                cell.state = 1;
            }

        }
    }
}

const neighborCheck = () => { 

    for(let i = 0; i < cells.length; i++){
        let cell = cells[i];
        if((i + 1) % HEIGHT != 0){
            cell.neighbors.push(cells[i + 1])
        }
        else { 
            cell.neighbors.push(cells[i - HEIGHT + 1])
        }

        if(i % HEIGHT != 0){
            cell.neighbors.push(cells[i - 1])
        }
        else { 
            cell.neighbors.push(cells[i + HEIGHT - 1])
        }
 
        if(i < cells.length - HEIGHT ){
            cell.neighbors.push(cells[i + HEIGHT])
        }
        if(i > HEIGHT){
            cell.neighbors.push(cells[i - HEIGHT])
        }
   
        if(i % HEIGHT != 0 && i < cells.length - HEIGHT){
            cell.neighbors.push(cells[i - 1 + HEIGHT])
        }
        if((i + 1) % HEIGHT != 0 && i < cells.length - HEIGHT){
            cell.neighbors.push(cells[i + 1 + HEIGHT])
        }
        if(i % HEIGHT != 0 && i > HEIGHT){
            cell.neighbors.push(cells[i - 1 - HEIGHT])
        }
        if((i + 1) % HEIGHT != 0 && i > HEIGHT){
            cell.neighbors.push(cells[i + 1 - HEIGHT])
        }



    }

}
createGrid(Math.floor(window.innerWidth / (CELLSIZE) ), Math.floor(window.innerHeight / CELLSIZE));



neighborCheck();


const MainLoop = () => { 
    if(generation % 30 == 0) count++;
    else if(generation % 200 == 0) random()
    for(const cell of cells){
        let count = 0;
        for(const neighbor of cell.neighbors){
            count += neighbor.state;
        }
        cell.aliveNeighbors = count;
        cell.prevState = cell.state;
    }
    
    for(const cell of cells){
        if(!pause){
            if(cell.aliveNeighbors == 2){
            }
            else if(cell.aliveNeighbors == 3){
                cell.state = 1
            }
            else {
                cell.state = 0
            }
        }

        if(color){
            if (cell.state == 0) {
                cell.color = Color.lerpColors(cell.color, cells[count].deadColor, useAlpha ? 0.1 : 1.0)
                cell.body.style.backgroundColor = cell.color.toString()
            }
            else if(cell.prevState == 0 && cell.state == 1){
                cell.color = Color.lerpColors(cell.color, cells[count].aliveColor, 1.0)
                cell.body.style.backgroundColor = cell.color.toString()
            }
            else if(cell.prevState == 1 && cell.state == 1){
                cell.color = Color.lerpColors(cell.color, cells[count].staticColor, useAlpha ? 0.1 : 1.0)
                cell.body.style.backgroundColor = cell.color.toString()
            }
        }
        else { 
            if(cell.state == 1){
                cell.color = Color.lerpColors(cell.color, whiteColor, useAlpha ? 0.5 : 1.0)
                cell.body.style.backgroundColor = cell.color.toString()
            }else { 
                cell.color = Color.lerpColors(cell.color, blackColor, useAlpha ? 0.25 : 1.0)
                cell.body.style.backgroundColor = cell.color.toString()
            }
        }
    }
    generation+=1;
}


let fps = 10, fpsInterval, startTime, now, then, elapsed;

function startAnimating(fps) {
    fpsInterval = 1000 / fps;
    then = Date.now();
    startTime = then;
    animate();
}

function animate() {

    requestAnimationFrame(animate);

    now = Date.now();
    elapsed = now - then;

    if (elapsed > fpsInterval) {

        then = now - (elapsed % fpsInterval);

        MainLoop()
    }
}

let random = () => { 
    for(const cell of cells){
        cell.state = Rand(0, 100) > 75 ? 1 : 0
    }
}

let clear = () => { 
    for(const cell of cells) cell.state = 0;
}


startAnimating(fps)

document.addEventListener('keydown', (event) => { 
   if(event.key == ' ') pause = !pause;
   if(event.key == 'r') random()
   if(event.key == 'c') color = !color
   if(event.key == 'v') clear()
   if(event.key == 'a') useAlpha = !useAlpha
   if(event.key == 'ArrowLeft') fpsInterval = 1000 / (fps > 0 ? fps -- : 0);
   if(event.key == 'ArrowRight') fpsInterval = 1000 / (fps <= 99 ? fps ++ : 100);
})