import time
import random
import string


# ---------------- Naive String Matching ---------------- #

def naive_search(text, pattern):
    n = len(text)
    m = len(pattern)

    matches = []
    comparisons = 0

    for i in range(n - m + 1):
        j = 0

        while j < m:
            comparisons += 1

            if text[i + j] != pattern[j]:
                break

            j += 1

        if j == m:
            matches.append(i)

    return matches, comparisons


# ---------------- Compute LPS Array ---------------- #

def compute_lps(pattern):
    m = len(pattern)

    lps = [0] * m
    length = 0
    i = 1

    while i < m:

        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1

        elif length != 0:
            length = lps[length - 1]

        else:
            lps[i] = 0
            i += 1

    return lps


# ---------------- KMP Algorithm ---------------- #

def kmp_search(text, pattern):

    n = len(text)
    m = len(pattern)

    lps = compute_lps(pattern)

    matches = []
    comparisons = 0

    i = 0
    j = 0

    while i < n:

        comparisons += 1

        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == m:
            matches.append(i - j)
            j = lps[j - 1]

        elif i < n and pattern[j] != text[i]:

            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return matches, comparisons


# ---------------- Rabin-Karp Algorithm ---------------- #

def rabin_karp(text, pattern, q=101):

    n = len(text)
    m = len(pattern)

    d = 256

    h = pow(d, m - 1, q)

    pattern_hash = 0
    text_hash = 0

    matches = []
    comparisons = 0

    # Initial hash values
    for i in range(m):
        pattern_hash = (d * pattern_hash + ord(pattern[i])) % q
        text_hash = (d * text_hash + ord(text[i])) % q

    # Sliding window
    for s in range(n - m + 1):

        if pattern_hash == text_hash:

            for k in range(m):
                comparisons += 1

                if text[s + k] != pattern[k]:
                    break

            else:
                matches.append(s)

        if s < n - m:

            text_hash = (
                d * (text_hash - ord(text[s]) * h)
                + ord(text[s + m])
            ) % q

            if text_hash < 0:
                text_hash += q

    return matches, comparisons


# ---------------- Main Program ---------------- #

text = "AABAACAADAABAABA"
pattern = "AABA"

print("Text    :", text)
print("Pattern :", pattern)

m1, c1 = naive_search(text, pattern)
m2, c2 = kmp_search(text, pattern)
m3, c3 = rabin_karp(text, pattern)

print("\nNaive Search")
print("Matches      :", m1)
print("Comparisons  :", c1)

print("\nKMP Search")
print("Matches      :", m2)
print("Comparisons  :", c2)

print("\nRabin-Karp Search")
print("Matches      :", m3)
print("Comparisons  :", c3)


# ---------------- Performance Analysis ---------------- #

text_large = "".join(random.choices("ABCD", k=10000))

patterns = [
    "AB",
    "ABCD",
    "ABCDAB",
    "ABCDABCD"
]

print("\nPerformance Comparison")
print("-" * 55)
print(f"{'Pattern':<15}{'Naive':>10}{'KMP':>10}{'RK':>10}")
print("-" * 55)

for p in patterns:

    _, c1 = naive_search(text_large, p)
    _, c2 = kmp_search(text_large, p)
    _, c3 = rabin_karp(text_large, p)

    print(f"{p:<15}{c1:>10}{c2:>10}{c3:>10}")