// Super simple REST API 
const { join } = require('path')
const express = require('express')
// const http = require('http')
const app = express()
const PORT = process.env.PORT || 3000

const SHARE = join('..', '..', 'share')
// just impor this, we need it anyway
const configJson = require(join(SHARE, 'config.json'))
const {
  MAX_CHAR,
  MIN_CHAR,
  POSSIBLE_MAX_CHAR,
  FILE_EXT
} = configJson

app
  .get('/', (req, res) => {
    res.send('Hello Anagram')
  })
  // data end point here
  .get('/anagram/:id', (req, res) => {
    let id = req.params.id
    switch (id) {
      case 'config': // return the config.json
          res.json(configJson)
        break;
      default:
        if (!isNaN(parseInt(id))) {

        } else {
          // throw error!
          res.status(404).send("OOPs NOT FOUND")
        }
    }
  })
  .listen(PORT, () => {
    console.log(`Express is running on ${PORT}`)
  })
