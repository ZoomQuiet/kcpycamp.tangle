from storm.locals import *
db_url = "mysql://root:123456@localhost/kchhd"

database = None
store = None
def getStore():
    global store
    if store == None:
        store = Store(getDatabase())
   
    return store
   
   
def getDatabase():
   global database
   if database == None:
       database = create_database(db_url)
   return database
'''
def close(obj):
    global database
    global store
    if obj == store:
        store.close()
        store = None
    elif obj == database:
        database.close()
        database = None

'''
