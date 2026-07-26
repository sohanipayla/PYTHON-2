let a = 1;
let b = 2;

setInterval(() => {

    console.log("A =", a);
    console.log("B =", b);
    console.log("Addition =", a + b);
    a++;
    b++;

}, 1000);