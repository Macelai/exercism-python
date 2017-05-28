def distance(dna0, dna1):
    count = 0
    if len(dna0) == len(dna1):
        for i in range(len(dna0)):
            if dna0[i] != dna1[i]:
                count += 1
    else:
        raise ValueError
    return count
