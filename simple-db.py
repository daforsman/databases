import os

db_file_name = 'tmp_dbs/simple-db'

def set(key, value):
    with open(db_file_name, "a") as database:
        database.write(str(key) + ":" + value + '\n')

def get(key):
    with open(db_file_name, "r") as database:
        for line in reversed(list(database)):
            line = line.rstrip('\n')
            (k, v) = line.split(":")
            if (str(key) == k):
                return v
        raise ValueError('Not found key')

if (raw_input("Reset db?") == 'y')
    open(db_file_name, 'w').close() # use to reset db

while (True):
    key = raw_input("Key:")
    if key == "":
        break
    value = raw_input("Value:")
    if value == "":
        break

    set(key, value)

while(True):
    key = raw_input("Get key:")
    if key == "":
        break

    try:
        print(get(key))
    except:
        print('Not found key')
