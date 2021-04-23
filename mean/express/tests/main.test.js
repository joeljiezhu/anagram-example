// not running it with any test suite at the moment
// const test = require('ava')

const { processor } = require('../src/processor')
const { join, normalize, resolve } = require('path')

const file = resolve('..', '..', 'share', '5.txt')

// let word = "whatever".split('')
// console.log(word.join(''))

processor(file)
  .then(content => {
    console.log(content)
  })
  .catch(err => {
    console.error(err)
  })

/*
// see the pain in the back side with async / await now?
(async () => {
  // const content = await processor(file)
  console.log('wtf')
  // console.log(content)
})()
*/
