# we take the data from the mariadb then use it to populate our sqlite database

from mylib.maria import Maria
from mylib.db import DB
# note we use a different database
sqlite = DB('../share/anagrams_1.db')

# just test it
sql = Maria()

result = sql.execute("SELECT count(*) as total FROM entries")

for total in db.cur:
    print(total[0])

# run the sqlite, take the world out then search from mysql
# then fill out the sqlite table
