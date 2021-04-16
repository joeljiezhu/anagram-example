// the top level file to run the express app
const express = require('express')
// const http = require('http')
const app = express()
const PORT = process.env.PORT || 3000

app.get('/', (req, res) => {
  res.send(`Hello`)
})
.listen(PORT, () => {
  console.log(`Express is running on ${PORT}`)
})
