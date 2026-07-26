const EventEmitter=require("events");
const event=new EventEmitter();

function listener1(){
    console.log("Listener 1 executed");
}   
function listener2(){
    console.log("Listener 2 executed");
}

event.on("myEvent",listener1);
event.on("myEvent",listener2);
event.emit("myEvent");

console.log("Total listeners:",event.listenerCount("myEvent"));
event.removeListener("myEvent",listener1);
event.emit("myEvent");
console.log("Remaining listeners:",event.listenerCount("myEvent"));