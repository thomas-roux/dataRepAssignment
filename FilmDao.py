#Import necessary modules
import mysql.connector
import dbconfig as cfg

#Create Film class
class FilmDao:
    #Database connection
    db = ""

    #Define initiation function to connect to db
    def __init__(self):
        self.db = mysql.connector.connect(
            host = cfg.mysql['host'],
            user = cfg.mysql['username'],
            password = cfg.mysql['password'],
            database = cfg.mysql['database']
        )
        #print("Connected to database.")

    #Create an entry in database
    def create(self, film):
        cursor = self.db.cursor()
        sql = "INSERT INTO films (Title, Year, Genre, Director, Language, Runtime, IFCO) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        values = [
            film['Title'],
            film['Year'],
            film['Genre'],
            film['Director'],
            film['Language'],
            film['Runtime'],
            film['IFCO']
        ]
        cursor.execute(sql, values)
        self.db.commit()
        return cursor.lastrowid

    #Get all entries of database
    def getAll(self):
        cursor = self.db.cursor()
        sql = "SELECT * FROM films"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        #print(results)

        #Converts tuple result into dict object to later enter as JSON
        for result in results:
            resultAsDict = self.convertToDict(result)
            returnArray.append(resultAsDict)

        return returnArray 

    #Convert tuples to dict objects
    def convertToDict(self, result):
        colnames = [
            'id',
            'Title',
            'Year',
            'Genre',
            'Director',
            'Language',
            'Runtime',
            'IFCO'
        ]
        film = {}

        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                film[colName] = value
        return film

    #Find entry by primary key in DB (id)
    def findById(self, id):
        cursor = self.db.cursor()
        sql = "SELECT * FROM films WHERE id = %s"
        value = (id,)
        cursor.execute(sql, value)
        result = cursor.fetchone()
        #print(results)
        return self.convertToDict(result)

    #Update entry in table
    def update(self, film, id):
        cursor = self.db.cursor()
        sql = "UPDATE films SET Title = %s, Year = %s, Genre = %s, Director = %s, Language = %s, Runtime = %s, IFCO = %s WHERE id = %s"
        values = [
            film['Title'],
            film['Year'],
            film['Genre'],
            film['Director'],
            film['Language'],
            film['Runtime'],
            film['IFCO'],
            id
        ]
        cursor.execute(sql, values)
        self.db.commit()
        return film

    #Remove an entry from the table by primary key (title)
    def delete(self, id):
        cursor = self.db.cursor()
        sql = "DELETE FROM films WHERE id = %s"
        value = (id,)
        cursor.execute(sql, value)
        self.db.commit()

        return {}

#Create new instance of FilmDao class for testing purposes
filmDao = FilmDao()