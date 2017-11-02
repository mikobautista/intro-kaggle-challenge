import pandas as pd # pandas for data frames
from scipy.stats import ttest_ind # just the t-test from scipy.stats
from scipy.stats import probplot # for a qqplot
import matplotlib.pyplot as plt # for a qqplot

# Read in our data.
cereals = pd.read_csv("../input/cereal.csv")
# Check out the first few lines.
cereals.head()

# Plot a qqplot to check normality. If the varaible is normally distributed,
# most of the points should be along the center diagonal.
probplot(cereals["sodium"], dist="norm", plot=pylab)

# Get the sodium for hot cerals
hotCereals = cereals["sodium"][cereals["type"] == "H"]
# and for cold ceareals.
coldCereals = cereals["sodium"][cereals["type"] == "C"]
# Then, compare them using a t-test.
ttest_ind(hotCereals, coldCereals, equal_var=False)

# Look at the means of each group to see which is larger.
print("Mean sodium for the hot cereals:")
print(hotCereals.mean())
print("Mean sodium for the cold cereals:")
print(coldCereals.mean())

# Plot the cold cereals
plt.hist(coldCereals, alpha=0.5, label='cold')
# and the hot cereals
plt.hist(hotCereals, label='hot')
# and add a legend
plt.legend(loc='upper right')
# add a title.
plt.title("Sodium(mg) content of cereals by type")

plt.show(block=True) # only close the program when plot.show() returns (once all figures are closed)
