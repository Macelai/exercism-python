def to_rna(dna):
    for char in dna:
        rna = dna.replace("G", "C")
        rna = dna.replace("C", "G")
        rna = dna.replace("T", "A")
        rna = dna.replace("A", "U")
    return rna
