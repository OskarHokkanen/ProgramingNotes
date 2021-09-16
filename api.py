from pysondb import db as database
DB_NAME = 'notes_db.json'

# @NOTE Should the method proved DB name?
def postItem(data):
    a = database.getDb(DB_NAME)
    a.add(data)


def getAllWithProjectName(projectName):
    a = database.getDb(DB_NAME)
    return a.getBy({'project_name': projectName})


def updateItemById(id, data):
    # updateById(ID,what_to_update)
    a = database.getDb(DB_NAME)

def getAllItems():
    # GET ALL ITEMS IN DB
    return
