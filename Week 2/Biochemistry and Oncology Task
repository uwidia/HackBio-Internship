import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#import SIFT and FoldX datasets
SIFT_data = pd.read_csv("https://raw.githubusercontent.com/HackBio-Internship/public_datasets/main/R/datasets/sift.tsv", sep = r"\s+")
FoldX_data = pd.read_csv("https://raw.githubusercontent.com/HackBio-Internship/public_datasets/main/R/datasets/foldX.tsv", sep = r"\s+")

FoldX_data.info()

SIFT_data["specific_Protein_aa"] = SIFT_data["Protein"] + "_" + SIFT_data["Amino_Acid"]
FoldX_data["specific_Protein_aa"] = FoldX_data["Protein"] + "_" + FoldX_data["Amino_Acid"]

#merge both datasets
merged_data = pd.merge(SIFT_data, FoldX_data, on = "specific_Protein_aa")

#drop one copy of redundant columns
merged_data.drop(["Protein_y", "Amino_Acid_y"], axis = 1, inplace = True)

#rename protein_x and amino_acid_x columns
merged_data.rename(columns = {"Protein_x": "Protein", "Amino_Acid_x": "Amino_Acid"}, inplace = True)

#Mutations with a SIFT score below 0.05 and FoldX Score above 2 (i.e. Mutations that affect Structure and Function)
deleterious_mutations = merged_data[(merged_data['sift_Score'] < 0.05) & (merged_data['foldX_Score'] > 2)]

amino_acids = []
for amino_acid in deleterious_mutations["Amino_Acid"]:
    amino_acids.append(amino_acid[0])

#Create a frequency table
frequency_table = {}
for amino_acid in amino_acids:
    if amino_acid in frequency_table:
        frequency_table[amino_acid] += 1
    else:
        frequency_table[amino_acid] = 1

#sort frequency table dictionary based on values
sorted_frequency_table = dict(sorted(frequency_table.items(), key = lambda x: x[1], reverse = True))

#Create Bar Plot and Pie Chart
fig, ax = plt.subplots(nrows = 1, ncols = 2, figsize = (12, 5))
ax[0].bar(sorted_frequency_table.keys(), sorted_frequency_table.values())
ax[0].set_xlabel("Amino Acid")
ax[0].set_ylabel("Frequency")
ax[0].set_title("Frequency of Mutations by Amino Acid")


ax[1].pie(sorted_frequency_table.values(), labels = sorted_frequency_table.keys())
ax[1].set_title("Mutations by Amino Acid")
plt.tight_layout()
plt.show()

print(f"The Amino Acid with the highest impact on structure and function is {list(sorted_frequency_table.keys())[0]}, which represents Glycine\n\nGlycine is characterized by a single hydrogen atom as its side chain. It is a non-essential amino acid, meaning the human body can synthesize it internally. Glycine is involved in the synthesis of important compounds such as creatine, heme, and glutathione. Additionally, glycine functions as an inhibitory neurotransmitter in the central nervous system, contributing to the regulation of nerve impulses. Due to its small size and flexibility, glycine is integral to the formation of alpha-helices in protein structures. It is also a precursor for many macromolecules in cells.")

#Identify amino acids that appeared over 100 times among those with Significant SIFT and FoldX Scores
keys = sorted_frequency_table.keys()

above_100 = {}
for key in keys:
    if sorted_frequency_table[key] > 100:
        above_100[key] = sorted_frequency_table[key]

print(f"Nonsense mutations involving amino acids that have over 100 occurences {tuple(above_100.keys())}, are more likely to have significantly deleterious effects, than others")



