from collections import Counter
from math import sqrt

def cosine_similarity(word1: str, word2: str) -> float:
    vec1 = Counter(word1)
    vec2 = Counter(word2)

    dot_prod = sum(vec1[ch] * vec2[ch] for ch in vec1.keys())
    mag_sq_1 = sum(count * count for count in vec1.values())
    mag_sq_2 = sum(count * count for count in vec2.values())
    return dot_prod / sqrt(mag_sq_1 * mag_sq_2)

def jaccard_similarity(word1: str, word2: str) -> float:
    set1 = set(word1)
    set2 = set(word2)
    return len(set1 & set2) / len(set1 | set2)
