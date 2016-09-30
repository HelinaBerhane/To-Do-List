# This Python file uses the following encoding: utf-8

### Import Modules ###
import sqlite3 # databases

#--------------------#
#-- Initialisation --#
#--------------------#

# create the connection object that represents the database
connection = sqlite3.connect('plan.db')
# create a Cursor object and call its execute() method to perform SQL commands:
c = connection.cursor()

# Create the tables
c.execute("CREATE TABLE IF NOT EXISTS solarTable(date INT, amount FLOAT, dailyAmount FLOAT, notes STRING(1000))")


#---------------------#
#----- Functions -----#
#---------------------#



#---------------#
#-- Questions --#
#---------------#



#---------#
#-- End --#
#---------#

# Commit all changes to the database and close the connection
connection.commit()   # Save (commit) the changes:
connection.close()    # Close the connection
