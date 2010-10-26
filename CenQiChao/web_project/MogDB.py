from django.db import connection

class MogDB(object):
    def __init__(self):
        self.connect = None
        pass

    def __del__(self):
        pass

    def Connect():
        if not self.connect:
            self.connect = connection.cursor()
        
    def Execute(sql, param):
        if not self.connect:
            Connect()
        connect.execute(sql,param)
        
    def Close():
        if self.connect:
            self.connect.close()
