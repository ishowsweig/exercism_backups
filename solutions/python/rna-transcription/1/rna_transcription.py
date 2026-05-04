def to_rna(dna_strand):
    if dna_strand == '':
        return  ''
    rna = ''
    for char in dna_strand:
        if char == 'T': 
            rna += 'A'
        if char == 'C': 
            rna += 'G'
        if char == 'G':
            rna += 'C'
        if char == 'A':
            rna += 'U'
    return rna
