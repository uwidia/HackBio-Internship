#Dataset used available at: https://gist.githubusercontent.com/stephenturner/806e31fce55a8b7175af/raw/1a507c4c3f9f1baaa3a69187223ff3d3050628d4/results.txt
#For Dataset Description, visit: https://github.com/HackBio-Internship/public_datasets/blob/main/R/nhanes_dd.csv

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#!pip install adjustText

#import adjustText package help with annotating genes on the volcano plot
from adjustText import adjust_text

df = pd.read_csv("https://gist.githubusercontent.com/stephenturner/806e31fce55a8b7175af/raw/1a507c4c3f9f1baaa3a69187223ff3d3050628d4/results.txt", sep = r"\s+")

df.head()

df['nlog10'] = -np.log10(df.padj) #create new column, -nlog10 (where n = padj)

#upregulated and downregulated genes
upregulated_genes = df[(df.log2FoldChange > 1) & (df.pvalue < 0.01) ]
downregulated_genes = df[(df.log2FoldChange < -1) & (df.pvalue < 0.01) ]

#sort upregulated and downregulated genes according to their expression levels
upregulated_genes= upregulated_genes.sort_values(by = 'log2FoldChange', axis = 0, ascending = False)
downregulated_genes = downregulated_genes.sort_values(by = 'log2FoldChange', axis = 0, ascending = True)

#create a new column that sorts genes into one of three categories - upregulated, downregulated, and not significant
def map_regulation(a):
    if a in upregulated_genes['Gene'].values:
        return "upregulated"
    elif a in downregulated_genes['Gene'].values:
        return "downregulated"
    else:
        return "not significant"
df['regulation'] = df["Gene"].apply(map_regulation)

ax = sns.scatterplot(data = df, x = 'log2FoldChange', y = 'nlog10', hue = 'regulation', hue_order = ['not significant', 'upregulated', 'downregulated'], palette = ['lightgrey', 'green', 'red']) #create volcano plot with seaborn
ax.axvline(-1, c = 'black', ls = '--', alpha = 0.3)
ax.axvline(1, c = 'black', ls = '--', alpha = 0.3)
ax.legend(loc =1, bbox_to_anchor = [1.38, 1])


ax.spines[['top', 'right']].set_visible(False)
ax.set_ylim(bottom = -0.1)

texts = []
for i in range(5):
    plt.text(upregulated_genes["log2FoldChange"].values[i], y = upregulated_genes['nlog10'].values[i], s = upregulated_genes['Gene'].values[i], weight = 'bold')
    texts.append(plt.text(downregulated_genes["log2FoldChange"].values[i], y = downregulated_genes['nlog10'].values[i], s = downregulated_genes['Gene'].values[i], weight = 'bold'))

adjust_text(texts, arrowprops = dict(arrowstyle = '-', color = 'k'))

#create dictionary with up- and downregulated genes and their functions
t5_upregulated_genes  ={"DTHD1": "This gene encodes a protein which contains a death domain. Death domain-containing proteins function in signaling pathways and formation of signaling complexes, as well as the apoptosis pathway. Alternative splicing results in multiple transcript variants", "EMILIN2": "Predicted to enable extracellular matrix constituent conferring elasticity. Involved in several processes, including positive regulation of angiogenesis; positive regulation of defense response to bacterium; and positive regulation of platelet aggregation. Located in extracellular region.", "PI16": "Predicted to enable peptidase inhibitor activity. Predicted to be involved in negative regulation of peptidase activity. Predicted to act upstream of or within negative regulation of cell growth involved in cardiac muscle cell development. Predicted to be located in extracellular region. Predicted to be active in extracellular space.", "C4orf45": "SPMIP2 (formerly C4orf45) (Sperm Microtubule Inner Protein 2) is a Protein Coding gene. Diseases associated with SPMIP2 include Hyperekplexia.", "FAM180B": "FAM180B (Family With Sequence Similarity 180 Member B) is a Protein Coding gene. Diseases associated with FAM180B include Borderline Leprosy and Mosaic Variegated Aneuploidy Syndrome."}
t5_downregulated_genes = {"TBX5": "TBX5 (T-Box Transcription Factor 5) is a Protein Coding gene. It codes for a DNA-binding protein that regulates the transcription of several genes and is involved in heart development and limb pattern formation", 'IFITM1': "IFITM1 (Interferon Induced Transmembrane Protein 1) is a Protein Coding gene. Diseases associated with IFITM1 include Influenza and West Nile Virus. Among its related pathways are Cytokine Signaling in Immune system and Antiviral mechanism by IFN-stimulated genes. Gene Ontology (GO) annotations related to this gene include obsolete signal transducer activity, downstream of receptor.", "TNN": "Predicted to enable integrin binding activity. Involved in positive regulation of sprouting angiogenesis; regulation of cell adhesion; and regulation of cell migration. Part of tenascin complex.", "COL13A1": "This gene encodes the alpha chain of one of the nonfibrillar collagens. The function of this gene product is not known, however, it has been detected at low levels in all connective tissue-producing cells so it may serve a general function in connective tissues.", "IFITM3": "Codes for the IFN-induced antiviral protein which disrupts intracellular cholesterol homeostasis. Inhibits the entry of viruses to the host cell cytoplasm by preventing viral fusion with cholesterol depleted endosomes. May inactivate new enveloped viruses which buds out of the infected cell, by letting them go out with a cholesterol depleted membrane." }

#print out the top 5 upregulated genes
print("TOP 5 UNREGULATED GENES AND THEIR FUNCTIONS\n*Functions gotten from Genecards.org\n--------------------------------")
for i in range(5):
    for key, value in t5_upregulated_genes.items():
        gene = key
        function = value
    print(f"Gene{i+1}. Name: {gene} \nFunction{function}\n")

#print out the top 5 downregulated genes
print("TOP 5 DOWNREGULATED GENES AND THEIR FUNCTIONS\n*Functions gotten from Genecards.org\n--------------------------------")
for i in range(5):
    for key, value in t5_downregulated_genes.items():
        gene = key
        function = value
    print(f"Gene{i+1}. Name: {gene} \nFunction{function}\n")

