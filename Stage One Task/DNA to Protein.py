#Task 1: DNA Translation:
Task1: #Function 1: Write a function for translating DNA to protein
def translate_dna (dna_seq):
#Transcribe DNA to RNA
    rna_sequence = ""
    for bases in dna_seq:
        if bases == "A":
            rna_sequence = rna_sequence + "U"
        elif bases == "T":
            rna_sequence = rna_sequence + "A"
        elif bases == "G":
            rna_sequence = rna_sequence + "C"
        elif bases == "C":
            rna_sequence = rna_sequence + "G"
        else:
            print("DNA sequence contains an inappropriate nucleotide")
            quit()
#Translate RNA to protein
    protein_sequence = ""
    codon_table = {
            'AUG': 'M', 'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',
            'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
            'UAU': 'Y', 'UAC': 'Y', 'UAA': '*', 'UAG': '*', 'UGA': '*',
            'UGU': 'C', 'UGC': 'C', 'UGG': 'W',
            'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
            'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
            'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
            'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
            'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'ACU': 'T', 'ACC': 'T',
            'ACA': 'T', 'ACG': 'T', 'AAU': 'N', 'AAC': 'N',
            'AAA': 'K', 'AAG': 'K', 'AGU': 'S', 'AGC': 'S',
            'AGA': 'R', 'AGG': 'R', 'GUU': 'V', 'GUC': 'V',
            'GUA': 'V', 'GUG': 'V', 'GCU': 'A', 'GCC': 'A',
            'GCA': 'A', 'GCG': 'A', 'GAU': 'D', 'GAC': 'D',
            'GAA': 'E', 'GAG': 'E', 'GGU': 'G', 'GGC': 'G',
            'GGA': 'G', 'GGG': 'G'
        }
    #find startcodon
    start_codon = rna_sequence.find("AUG")
    #Start translation
    for codons in range(start_codon, len(rna_sequence)- len(rna_sequence)%3, 3):
        codon = rna_sequence[codons:codons + 3]
        aminoacid = codon_table.get(codon)
        if aminoacid == "*":
            break
       else:
            protein_sequence += aminoacid
    print(f"The result of the translation of the DNA sequence: {dna_seq} to protein is {protein_sequence}")
dna_sequence = "ATTACTGCTACTAGCCCTTAATCGGACGAC"
protein_seq = translate_dna(dna_sequence)
