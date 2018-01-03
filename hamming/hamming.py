def distance(strand_a, strand_b):
    hamming = 0
    if len(strand_a) == len(strand_b):
        for letter_a, letter_b in zip(strand_a, strand_b):
            if letter_a != letter_b:
                hamming += 1
        return hamming
    else:
        raise ValueError("The DNA's")
