const express = require('express')
const app = express()
const path = require('path');
const port = process.env.PORT || 8080;


app.get('/', function(req, res) {
  res.sendFile(path.join(__dirname, '/index.html'));
});

app.use(express.static(__dirname + '/public'))

app.listen(port, () => {
  console.log(`https://localhost:${port}`)
})