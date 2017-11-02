import scipy.stats # statistics
import pandas as pd # dataframe

# Read in our data.
surveyData = pd.read_csv("../input/anonymous-survey-responses.csv")

# First, let's do a one-way chi-squared test for stats background.
scipy.stats.chisquare(surveyData["Have you ever taken a course in statistics"].value_counts())

# Then, let's do a one-way chi-squared test for programming background.
scipy.stats.chisquare(surveyData["Do you have any previous experience with programming"].value_counts())

# Finally, let's do a two-way chi-square test. Is there a relationship between programming background and stats background?
contingencyTable = pd.crosstab(surveyData["Do you have any previous experience with programming"],
                               surveyData["Have you ever taken a course in statistics"])

print(scipy.stats.chi2_contingency(contingencyTable))