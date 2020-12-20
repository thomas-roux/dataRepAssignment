# dataRepAssignment
This is the final assignment for Module 52957 "Data representation and Querying", GMIT Higher Diploma in Computer Science. The whole project contains 5 program files, a `requirements.txt` containing the virtual environment requirements for the server, and a .gitignore file. In addition, there is a standard MIT Licence and this readme.md file.

# Contents of code files
- `dbconfigtemplate.py` contains the user details for the SQL server in a python object
- `filmServer.py` contains the code for the actual server
- `FilmDao.py` contains code for connection to the database, and SQL code for effecting changes on the database in the films table
- `SeriesDao.py` contains code for connection to the database, and SQL code for effecting changes on the database in the series table
- `initdb.sql` contains SQL code for creation of the tables

# Purpose of code
This code is in completion of the final assignment as specified above. It is a database repository library of films and tv series, that are accessed via a webpage, and allow direct interaction on the webpage with the database through a server.

# Setup
1. Before running `filmServer.py`, you need to set up the `dbconfig.py` file. The basic template can be found in the `dbcongfigtemplate.py` file. Change the `mysql` object to contain the necessary details specific to your SQL server. Then save the file as `dbconfig.py` in the same folder as the other files.
2. You will need to create the tables for the database. This is best done by going into your SQL database and creating the tables there. The full SQL code for both tables (there is a film and series table), can be found in the `initdb.sql` file. Copy and paste each table code in turn into SQL. Make sure not to include the comment section
3. Make sure that all files are downloaded into the same folder.
4. You're good to go

# Running the server
1. Start by running `filmServer.py` on the command line: `python filmServer.py`
2. Once the server is up and running, open up a web-browser and type in: `http://127.0.0.1:5000/index.html`
3. You will be greeted by a webpage containing a brief welcome message and two tables, one for films and the other for series

# Using the webpage
1. If this is the first time using the tables, there will be no entries visible
2. Hit `Create` button and fill in the form. ID will populate automatically once database entry created - you will not be able to select an ID yourself. Some fields will accept numbers only - the form will not process if letters are entered, and the corresponding fields will be outlined in red. If you wish to cancel an entry, just hit the `cancel` button at the bottom of the form.
3. Once a new entry has been created, refresh the page to show the updated entry with the new ID Number
4. You can update the database entries by hitting the `Update` button that appears alongside an entry. Make any changes on the form and hit `Update` to update the database entry. If you wish to cancel an updatge, just hit the `cancel` button at the bottom of the form. It isn't necessary to refresh the page after an update.
5. You can also delete an entry. BE WARNED - no error message will appear before deletion!

# Troubleshooting
- If you get a webpage error message, make sure your server is running. 
- If the table doesn't populate, or you're unable to make changes to the table, make sure that the credentials for accessing SQL have been updated properly in the `dbconfig.py` file. If you don't see a `dbconfig.py` file, see point 1 in Setup above.
