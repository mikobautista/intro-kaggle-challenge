import pandas as pd # for CSV file I/O

# Read a few CSV files and output their summaries.
digimonlist = pd.read_csv("../input/DigiDB_digimonlist.csv")
print(digimonlist.describe())

movielist = pd.read_csv("../input/DigiDB_movielist.csv")
print(movielist.describe())

supportlist = pd.read_csv("../input/DigiDB_supportlist.csv")
print(supportlist.describe())