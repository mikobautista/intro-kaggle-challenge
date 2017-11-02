import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt # for plotting

# Read in our data.
dataframe = pd.read_csv("../input/anonymous-survey-responses.csv")
# Look at the first few rows.
dataframe.head()

# Matplotlib is a little bit involved, so we need to do quite a bit of 
# data manipulation before we can make our bar chart.

## Data Preperation

# Count how often each pet preference is observed.
petFreqTable = dataframe["Just for fun, do you prefer dogs or cat"].value_counts()

# Just FYI: this will get us a list of the names.
list(petFreqTable.index)
# Just FYI: this will get us a list of the counts.
petFreqTable.values

# Get all the name from our frequency plot and save them for later.
labels = list(petFreqTable.index)

# Generate a list of numbers as long as our number of labels.
positionsForBars = list(range(len(labels)))

## Actual Plotting

# Pass the names and counts to the bar function.
plt.bar(positionsForBars, petFreqTable.values) # plot our bars
plt.xticks(positionsForBars, labels) # add lables
plt.title("Pet Preferences")

# Alternatively, we can also use the seaborn package to plot.
# import seaborn as sns
# sns.countplot(dataframe["Just for fun, do you prefer dogs or cat"])

plt.show(block=True) # only close the program when plot.show() returns (once all figures are closed)