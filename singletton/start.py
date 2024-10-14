class Database:
    import threading
    __connection = None
    #__lock = threading.Lock()

    @staticmethod
    def getConnection():
        if Database.__connection == None:
            Database()
        return Database.__connection

    def __init__(self):
        if Database.__connection != None:
            raise Exception("A connection exists already!")
        else:
            Database.__connection = self


conn1 = Database.getConnection()
conn2 = Database.getConnection()



print(conn1)
print(conn2)



