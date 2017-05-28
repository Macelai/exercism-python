def to_rna(dna):
    rna = ''
    dna_rna = {'G':'C', 'C':'G', 'T':'A', 'A':'U'}
    for char in dna:
        try:
            rna = rna + dna_rna[char]
        except:
            return ""
    return rna
