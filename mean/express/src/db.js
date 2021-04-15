
const { MongoClient } = require('mongodb')


function connect(dbname) {
  const url = `mongodb://localhost:27017/${dbname}`
  return new Promise((resolver, rejecter) => {
    MongoClient.connect(url, function(err, db) {
      if (err) {
        return rejecter(err)
      }
      const dbase = db.db(dbname)

      return {
        dbase,
        db
      }
      // db.close()
    })
  })
}

module.exports = { connect }
