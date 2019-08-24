### Databases
This project is a sandbox for creating databases.

All database files should be stored in tmp_dbs, ignored by git.

## Simple database
The most simple database available is just appending a file and finding the value in that file.
The simple implementation splits entries on the colon.

Pros:
- Easy to implement
- Fast writes, possibly the fastest (unless you use big key)

Cons
- Eventually slow reads, linear time consumption
- Reads the entire database to memory, eventually won't fit
