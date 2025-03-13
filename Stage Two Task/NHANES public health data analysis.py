import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("https://raw.githubusercontent.com/HackBio-Internship/public_datasets/main/R/nhanes.csv")

#make a copy of the original dataset
original_dataset = df.copy()

#examine dataset
df.info()

#Task 1: Select numeric columns in the dataframe and fill them with zero(0)
numeric_columns = df.select_dtypes(exclude=["bool_","object_"]).columns
i = 0
for column in numeric_columns:
    df[column] = df.select_dtypes(exclude=["bool_","object_"]).fillna(0).iloc[:,i]
    i+=1

#Select categorical columns in the dataframe and fill them with "Unknown"
categorical_columns = df.select_dtypes(exclude=["number", "bool_"]).columns
j = 0
for column in categorical_columns:
    df[column] = df.select_dtypes(exclude=["number", "bool_"]).fillna("Unknown").iloc[:,j]
    j+=1

df.info()

#Create a new column, Weight(pounds)
df["Weight(pounds)"] = df["Weight"] * 2.2

#Task 2: Plot the distribution of BMI, Weight, Weight(pounds), and Age with a histogram
fig, ax = plt.subplots(nrows = 2, ncols = 2, figsize = (12,6))
ax[0][0].hist(df["BMI"])
ax[0][0].set_title("BMI (distribution)")


ax[0][1].hist(df["Weight"])
ax[0][1].set_title("Weight (distribution)")

ax[1][0].hist(df["Weight(pounds)"])
ax[1][0].set_title("Weight(pounds) (distribution)")

ax[1][1].hist(df["Age"])
ax[1][1].set_title("Age (distribution)")

plt.tight_layout()


#Task 3: Mean of 60 second pulse rate (without inputed zero values, since it will affect the mean)
pulse_rate_mean = df["Pulse"][df["Pulse"] != 0].mean()

print(f"The mean 60 second pulse rate is {pulse_rate_mean:.2f}")

BPDia_min = df["BPDia"].min()
BPDia_max = df["BPDia"].max()

print(f"The range of values for diastolic blood pressure is {BPDia_min:.0f} -- {BPDia_max:.0f}")

#Income variance among participants (discounting imputed zero values since they would affect the variance)
income_variance = df["Income"][df["Income"] != 0].var()
print(f"The variance of income is {income_variance:.2f}")


#Income standard deviation among participants (discounting imputed zero values since they would affect the std)
income_std = df["Income"][df["Income"] != 0].std()
print(f"The variance of income is {income_std:.2f}")

#Relationship between height and weight based on gender
fig = sns.scatterplot(data = df, x = "Weight", y = "Height", hue = "Gender", palette = ['blue', 'pink'])
fig.set_title("Height vs Weight")
fig.legend(loc = 1, bbox_to_anchor = (1.25,1), title = "Gender")

#Relationship between height and weight based on Diabetes Status
fig = sns.scatterplot(data = df, x = "Weight", y = "Height", hue = "Diabetes", palette = ['green','red', 'blue'], style = "Diabetes", style_order = ["No", "Yes", "Unknown"], markers = ['*', 'o',  'd'])
fig.set_title("Height vs Weight")
fig.legend(loc = 1, bbox_to_anchor = (1.28,1), title = "Diabetes Status")

#Relationship between height and weight based on Diabetes Status
fig = sns.scatterplot(data = df, x = "Weight", y = "Height", hue = "SmokingStatus", style ="SmokingStatus", style_order = ["Unknown", "Current", "Never", "Former"], markers = ['*', 'o',  'd', 's'])
fig.set_title("Height vs Weight")
fig.legend(loc = 1, bbox_to_anchor = (1.28,1), title = "Smoking Status")

#sort ages according to gender
male_participants = df.Age[df["Gender"] == "male"]
female_participants = df.Age[df["Gender"] == "female"]

#Performing a ttest on difference in ages based on Gender
t_stat, p_value = stats.ttest_ind(male_participants, female_participants)

if p_value < 0.05:
    print("There is a significant difference in ages between male and female participants.")
else:
    print("There is no significant difference in ages between male and female participants.")

#sort BMI according to Diabetes Status
diabetic = df.BMI[df["Diabetes"] == "Yes"]
non_diabetic = df.BMI[df["Diabetes"] == "No"]

#Performing a ttest on difference in BMI based on Diabetes Status
t_stat, p_value = stats.ttest_ind(diabetic, non_diabetic)

if p_value < 0.05:
    print("There is a significant difference in BMI between diabetic and non-diabetic participants.")
else:
    print("There is no significant difference in BMI between diabetic and non-diabetic participants.")

#sort Alcohol Year according to Relationship Status
committed = df.AlcoholYear[df["RelationshipStatus"] == "Committed"]
single = df.AlcoholYear[df["RelationshipStatus"] == "Single"]

#Performing a ttest on difference in Alcohol Year based on Relationship Status
t_stat, p_value = stats.ttest_ind(committed, single)

if p_value < 0.05:
    print("There is a significant difference in Alcohol Year between committed and single participants.")
else:
    print("There is no significant difference in Alcohol Year between committed and single participants.")
