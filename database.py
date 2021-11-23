import sqlite3
def createdbase():
    #connection to db and cursor
    con = sqlite3.connect('Movie.db')
    cur = con.cursor()   
    cur.execute(""" CREATE TABLE Movies(
    movie_name text,
    actor_name text,
    actress_name text,
    year_release integer,
    director_name text
   )""")
    

 #====================================================================================           

def add_one(movie, actor, actress, year, director):
    con = sqlite3.connect('Movie.db')
    cur = con.cursor()
    #adding data to db
    cur.execute("INSERT INTO Movies VALUES (?, ?, ?, ?, ?)",(movie, actor, actress, year, director))
    print("Record Inserted Sucessfully...")
    #comit and close
    con.commit()
    con.close()
#=======================================================================================

def fetching():
    conn = sqlite3.connect('Movie.db')
    c = conn.cursor()
    c.execute("SELECT * FROM Movies")
    items=c.fetchall()
    print("name", "\t\t", "actor", "\t\t", "actress", "\t\t", "release")
    print("-----------------------------------------------------------")
    for i in items:
        print(i[0], "\t" ,i[1], "\t", i[2], "\t", i[3], "\t", i[4])

    conn.commit()
    conn.close()
#============================================================================================

def actor_search(Factor):
    con = sqlite3.connect('Movie.db')
    cur = con.cursor() 
    #searching the actors
    cur.execute("SELECT * FROM Movies WHERE actor_name = (?)", (Factor,))
    items = cur.fetchall()
    print("ACTOR"," ", "MOVIE NAME")
    print("-----"," ", "---------")
    for i in items:
        print(i[1]," ", i[0])  
    #comit and close
    con.commit()
    con.close()   

#=============================================================================================

def delete_rec(Dactor):
    conn = sqlite3.connect('Movie.db')
    c = conn.cursor()
    c.execute("DELETE FROM Movies WHERE actor_name = (?)", (Dactor,))
    print("Record Deleted Sucessfully...")
    conn.commit()
    conn.close()
#==============================================================================================
def delete_database():
    conn = sqlite3.connect('Movie.db')
    c = conn.cursor()
    c.execute("DROP TABLE Movies")
    print("Table Deleted Sucessfully...")

    conn.commit()
    conn.close()