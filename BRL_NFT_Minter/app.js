const express = require('express')
const app = express();
const mintRoute = require('./routes/mint-nft') 
const { json } = require('body-parser');
var cors = require('cors')
const testRoute = require("./routes/test");
//Middlewares
app.use(cors());
//Parse json req.body
app.use(json());
//minting NFT middleware
app.use('/mint', mintRoute);
app.use('/test', testRoute)
// start listening to server
// port # = 9000
app.listen(9000);

// Future work
// 1. add user auth
// 2. add db to store all the meta about NFT (mongo is easy to integrate)