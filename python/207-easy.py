"""
This week's theme is bioinformatics.

---Description---

DNA - deoxyribonucleic acid - is the building block of every organism.
It contains information about hair color, skin tone, allergies, and more.
It's usually visualized as a long double helix of base pairs.
DNA is composed of four bases - adenine, thymine, cytosine, guanine -
paired as follows: A-T and G-C.

Your program should take a DNA squence as input
and return the complementary strand.
"""

pairs = {'A': 'T',
         'T': 'A',
         'G': 'C',
         'C': 'G'}

strand = input("Enter a series of DNA base pairs:\n").split()
mirror = [pairs[x] for x in strand]

print(' '.join(mirror))
