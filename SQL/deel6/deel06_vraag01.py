import db

# maak connectie met de database
database = 'rubyquest.db'
dbConnection = db.connect(database)

# zet de query
query = "select * from weapon where price between 100 and 1000"
dbConnection.setQuery(query)

# voer query uit
dbConnection.execute()

# haal data op die bij de query hoort
data = dbConnection.fetch()

# laat een stuk van de data zien
dbConnection.printSnippet(data)

# optionele view functie
# dbConnection.showInPopup(data)