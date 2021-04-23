

// create a simple processor here to grab the text file
// then turn it into a json and return it
// using the all new promise api
const fs = require('fs/promises')

/**
 * make it comparable char sequence
 * @param {string} word input word
 * @return {string} seq sorted
 */
function getCharSeq(word) {
  let s = word.split('')
  s.sort()
  return s.join('')
}


/**
 * Just read from the file turn it into a json
 * @param {string} file where the file is
 * @return {promise} that resolve with the json
 */
exports.processor = async function(file) {
  let fh;
  try {
    fh = await fs.open(file, 'r')
    let content = await fh.readFile("utf-8")
    let words = content.replace(/[\n\t\r]/g,"").split(' ')

    return words.map(word => {
                    let seq = getCharSeq(word)
                    return {[word]: seq}
                }).reduce((a, b) => Object.assign(a, b), {})
  } catch(e) {
    throw e
  } finally {
    await fh?.close()
  }
}
