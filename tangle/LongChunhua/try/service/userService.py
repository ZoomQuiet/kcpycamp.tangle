from webapps.kcHHD.conf import storm_conf
from webapps.kcHHD.model.user_orm import User

store = storm_conf.getStore()

def addUser(ID,Name,Type,Pwd,Dept=""):
    if checkUserIDUsed(ID):
        raise IDDuplicate,ID
    user = User(ID,Name,Type,Pwd,Dept)
    store.add(user)
    store.commit()

def checkUserIDUsed(ID):
    if store.find(User,User.ID == ID).one():
        return True
    else:
        return False

def modifyUser(ID,Name,Type,Pwd,Dept=""):
    currentUser = store.find(User,User.ID == ID).one()
    currentUser.Name = Name
    currentUser.Type = Type
    currentUser.Pwd = Pwd
    currentUser.Dept = Dept
    store.commit() 

def deleteUser(userID):  
    uer = store.get(User,int(userID))
    store.remove(user)
    store.commit()
    