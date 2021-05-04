# we take the data from the mariadb then use it to populate our sqlite database
import datetime
import time
import json
from sys import argv
# start timer

# our lib
from mylib.maria import Maria
from mylib.db import DB
# note we use a different database
sqlite = DB('../share/anagramdicts.db')
dictDb = DB('../share/dictionary.db')
sqlite.connect()
dictDb.connect()
# sql = Maria()

def getSqlTotal():

    result = sql.execute("SELECT count(*) as total FROM entries")
    total = 0
    for row in sql.cur:
        total = row[0]
        print(f"total {total} words in entries")
    return total

def getWordsFromAnagram():
    # run the sqlite, take the world out then search from mysql
    # then fill out the sqlite table
    wordGroups = {}
    allWords = []
    ctn = 0
    for word in sqlite.execute("SELECT word FROM anagrams"):
        ctn += 1
        allWords.append(word[0]) # store all the words in one array
        wlen = len(word[0])
        wordGroups[wlen] = wordGroups.get(wlen) or [] # If I didn't use dict.get I get a Key error
        wordGroups[wlen].append(word[0])

    return (wordGroups, allWords, ctn)

# wrap the whole thing in one function
def fillTable():
    before = datetime.datetime.now()
    (wordGroups, allWords, wordsLen) = getWordsFromAnagram()
    print(f"total {wordsLen} in anagrams table")
    placeholder = ["?" for i in range(wordsLen)]
    # (fields) word, wordtype, definition
    findSql = f"SELECT lcword, definition FROM dicts WHERE lcword IN ({','.join(placeholder)})"
    # print(findSql)
    findResult = dictDb.execute(findSql, tuple(allWords))
    # there are lots of duplicate in the result ... WTF?
    wordsDef = {}
    ctn = 0
    for row in findResult:
        ctn += 1
        (word, definition) = row
        wordsDef[word] = wordsDef.get(word) or []
        wordsDef[word].append(definition)

    print(f"return row total is {ctn} has wordDef size of {len(wordsDef)}")

    updateTable(wordsDef)

    # python is really slow
    after = datetime.datetime.now()
    print(f"Elasped time = {after - before}")

    return True

def updateTable(wordsDef):
    # now finally update the sqlite table
    updateSql = "UPDATE anagrams SET dict = ? WHERE word = ?"
    # the query executed but the table is not filled
    # sqlite.executeMany(updateSql, wordsDef)
    ctn = 0
    data = []

    print(f"going to update {len(wordsDef)}")

    # do this with a timer
    for key in wordsDef.keys():
        data.append((json.dumps(wordsDef[key]), key))

    # do this one by one!
    for row in data:
        sqlite.execute(updateSql, row)
        print(f"update {row[1]} with entries of {len(row[0])}", end="\r")
        time.sleep(0.3)

    # finally just check the total
    checkTableValue()

    return True # just a stop word

def checkTableValue():
    checkSql = f"SELECT count(*) as total FROM anagrams WHERE dict IS NOT NULL"
    for row in sqlite.execute(checkSql):
        print(f"Total word has no def is {row[0]}")
    # for row in output:
    #    print(row)

def takeFromMysql():
    """
    take all the data from the mysql and create a new database in sqlite
    """
    sqlite = DB('../share/dictionary.db')
    sqlite.connect()
    create_table_sql = "CREATE TABLE IF NOT EXISTS dicts (word TEXT, wordtype TEXT, definition TEXT, lcword TEXT)"
    sqlite.execute(create_table_sql)
    # take data from mariadb
    data = []
    sql.execute("SELECT * FROM entries ORDER BY word")
    for row in sql.cur:
        nr = row + (str(row[0]).lower(),)
        data.append(nr)
        print(f"entries: {nr}", end="\r")
        time.sleep(0.1)
    # dump the data back into the sqlite
    sqlite.executeMany("INSERT INTO dicts (word, wordtype, definition, lcword) VALUES (?,?,?,?)", data)

    return True

if __name__ == '__main__':
    script, cmd = argv
    if cmd == "fill":
        fillTable()
    elif cmd == "show":
        for row in sqlite.execute("SELECT count(*) FROM anagrams WHERE dict IS NULL"):
            print(row)
    elif cmd == "take":
        takeFromMysql()
    else:
        checkTableValue()
