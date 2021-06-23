var express = require("express");
var app = express();
var fs = require('fs');
//
app.listen(3000, () => {
  console.log("Api server runing on port 3000");
});

app.get("/name-api-poe_site", (req, res, next) => {
  fs.readFile('data.json', function(err, data) {
    if (err) {
      return console.log(err);
    }
    let parsed_data = JSON.parse(data);
    res.json(parsed_data);
  });

})