    from databases.storm.locals import *
    db_url = "mysql://root:123456@192.168.1.160/kchhd"
    
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
