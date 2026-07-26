const EventEmitter=require("events")
const event=new EventEmitter();

let radius=5
let side=4

event.on("circle",()=>{
    if(radius<0){
        console.log("Radius must be positive");
    }
    else{
        console.log("Area of Circle is",3.14*radius*radius);
    }
})

event.on("square",()=>{
    if(side<0){
        console.log("Side must be positive");
    }
    else{
        console.log("Area of Square is",side*side);
    }
})
event.emit("circle")
event.emit("square")