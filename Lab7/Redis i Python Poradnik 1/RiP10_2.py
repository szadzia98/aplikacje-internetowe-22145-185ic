from walrus import *

db = Database(host='localhost', port=6379, db=0)


class Book(Model):
    __database__ = db
    id= UUIDField()
    title = TextField()
    description = TextField()
    pages = IntegerField()
    tags = SetField


book = Book.create(title="Włam się do mózgu", description="O tym jak się uczyć", pages=300, tags={'nauka','uczenie'})