# we take the data from the mariadb then use it to populate our sqlite database

from mylib.maria import Maria


# just test it
db = Maria()

result = db.execute("SELECT count(*) as total FROM entries")

for total in db.cur:
    print(total[0])
