import matplotlib.pyplot as plt # for histogram data visualization
import pandas as pd # for CSV file I/O

# Read the cereal CSV file and present a histogram on calorie data.
cereal = pd.read_csv("../input/cereal.csv")
calories = cereal["calories"]
plt.hist(calories, bins=9, edgecolor="black")
plt.title("Calories in Cereal") # add a title
plt.xlabel("Calories") # label the x axes 
plt.ylabel("Count") # label the y axes

# Alternative way of plotting a histogram from the pandas plotting API.
# cereal.hist(column="calories", figsize = (12,12)) # figsize is used to enlarge the graph
# plt.title("Calories in Cereal") # add a title
# plt.xlabel("Calories") # label the x axes 
# plt.ylabel("Count") # label the y axes

plt.show(block=True) # only close the program when plot.show() returns (once all figures are closed)