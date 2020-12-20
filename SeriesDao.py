#Import necessary modules
import mysql.connector
import dbconfig as cfg

#Create Film class
class SeriesDao:
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
    def create(self, series):
        cursor = self.db.cursor()
        sql = "INSERT INTO series (Title, Started, Ended, Genre, Language, Seasons, Episodes) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        values = [
            series['Title'],
            series['Started'],
            series['Ended'],
            series['Genre'],
            series['Language'],
            series['Seasons'],
            series['Episodes']
        ]
        cursor.execute(sql, values)
        self.db.commit()
        return cursor.lastrowid

    #Get all entries of database
    def getAll(self):
        cursor = self.db.cursor()
        sql = "SELECT * FROM series"
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
            'Started',
            'Ended',
            'Genre',
            'Language',
            'Seasons',
            'Episodes'
        ]
        series = {}

        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                series[colName] = value
        return series

    #Find entry by primary key in DB (id)
    def findById(self, id):
        cursor = self.db.cursor()
        sql = "SELECT * FROM series WHERE id = %s"
        value = (id,)
        cursor.execute(sql, value)
        result = cursor.fetchone()
        #print(results)
        return self.convertToDict(result)

    #Update entry in table
    def update(self, series, id):
        cursor = self.db.cursor()
        sql = "UPDATE series SET Title = %s, Started = %s, Ended = %s, Genre = %s, Language = %s, Seasons = %s, Episodes = %s WHERE id = %s"
        values = [
            series['Title'],
            series['Started'],
            series['Ended'],
            series['Genre'],
            series['Language'],
            series['Seasons'],
            series['Episodes'],
            id
        ]
        cursor.execute(sql, values)
        self.db.commit()
        return series

    #Remove an entry from the table by primary key (title)
    def delete(self, id):
        cursor = self.db.cursor()
        sql = "DELETE FROM series WHERE id = %s"
        value = (id,)
        cursor.execute(sql, value)
        self.db.commit()

        return {}

#Create new instance of FilmDao class for testing purposes
seriesDao = SeriesDao()