import database
#-----------------------Warning---------------------------. 
def databaseCreation():
    #use this code only for creating and then comment it. 
    database.createdbase()
#----------------------Warning----------------------------.


def addingSingleRecord():
    movie = input("Please Enter Movie Name: ")
    actor = input("Please Enter Actor Name: ")
    actress = input("Please Enter Actress Name: ")
    year = input("Please Enter Year: ")
    director = input("Please Enter Director Name: ")
    database.add_one(movie, actor, actress, year, director)

def deletingOneRecord():
    Dactor = input("Please Enter the Actor name to delete the record: ")
    database.delete_rec(Dactor)

def ActorLookup():
    Factor = input("Please Enter The Actor Name for his movie details:  ")
    database.actor_search(Factor)

def ShowDB():
    print("THE MOVIE DATABASE IS: ")
    database.fetching()

def DeleteTable():
    database.delete_database()

print("""1.Create DataBase(!NOTE: USE THIS FUNCTION ONLU ONCE!)
2. Add Record.
3. Delete Single Record.
4. Find Actor Details.
5. Show DATABASE.
6. Delete Table.
""")
Data = int(input())
if Data == 1:
    databaseCreation()
elif Data == 2:
    addingSingleRecord()
    database.fetching()
elif Data == 3:
    deletingOneRecord()
    database.fetching()
elif Data == 4:
    ActorLookup()
elif Data == 5:
    ShowDB()
elif Data == 6:
    DeleteTable()
else:
    print("PLEASE ENTER VALID NUMBER")