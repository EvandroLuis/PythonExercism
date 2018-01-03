def to_rna(dna_strand):
    dna_letters = list(filter(str.isalnum, dna_strand.upper()))
    rna = ""
    for letter in dna_letters:
        if letter == "G":
            rna += "C"
        elif letter == "C":
            rna += "G"
        elif letter == "T":
            rna += "A"
        elif letter == "A":
            rna += "U"
        else:
            raise ValueError("Invalid dna letter")
    return rna