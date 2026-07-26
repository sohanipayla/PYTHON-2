// Connect to Primary
// mongosh --port 27019

// Initialize Replica Set
rs.initiate({
  _id: "rs1",
  members: [
    { _id: 0, host: "localhost:27019" },
    { _id: 1, host: "localhost:27020" }
  ]
})

// Create Database
// use college

// Insert Documents
db.student.insertMany([
  {name:"Amit", age:18, date:new Date()},
  {name:"Rahul", age:20, date:new Date()},
  {name:"Neha", age:17, date:new Date()},
  {name:"Riya", age:14, date:new Date()}
])

// Connect to Secondary
// mongosh --port 27020

// Read Data
rs.secondaryOk()

// use college

db.student.find({age:{$gt:15}})