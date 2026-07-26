const express=require("express");
const app=express();

const products=[
    {id:1,name:"Laptop",description:"DEL Laptop",price:50000},
    {id:2,name:"Mobile",description:"Samsung Mobile",price:20000},
    {id:3,name:"Smartwatch",description:"Apple Smartwatch",price:30000}
]

app.get("/",(req,res)=>{
    res.send(`<h2>Welcome to Online Store</h2>`)
})

app.get("/products",(req,res)=>{
    let html="<h2>Product List</h2><ul>";
    products.forEach(product=>{
        html+=
        `<li>${product.name} - ${product.description} - ${product.price}
        <a href="/products/${product.id}">View Details</a></li>`;
    })
    html+="</ul>";
    res.send(html);
})

app.get("/products/:id",(req,res)=>{
    const productId=parseInt(req.params.id);
    const product=products.find(p=>p.id===productId);
    if(!product){
        res.status(404).send("<h2>Product Not Found</h2>");
    }   
    res.send(`<h2>Product Details</h2>
        Name:${product.name}<br>
        Description:${product.description}<br>
        Price:${product.price}<br>
        <a href='/products'>Back to Products</a>`)
}).listen(3000)