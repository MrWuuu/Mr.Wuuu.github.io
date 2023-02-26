def jaccard_similarity(a: list, b: list):
    a = set(a)
    b = set(b)

    intersection = len(a.intersection(b))
    union = len(a.union(b))

    return intersection / union


def jaccard_containment(a: list, b: list):
    a = set(a)
    b = set(b)

    intersection = len(a.intersection(b))

    return intersection / len(a)


def build_kmers(sequence, ksize):
    kmers = []
    n_kmers = len(sequence) - ksize + 1

    for i in range(n_kmers):
        kmer = sequence[i:1+ksize]
        kmers.append(kmer)
        
    return kmers
