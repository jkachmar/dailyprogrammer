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


def base_pair(strand):
    """Return matching base pairs for a strand of DNA."""
    pairs = {'A': 'T',
             'T': 'A',
             'G': 'C',
             'C': 'G'}

    mirror = ' '.join([pairs[x] for x in strand.split()])
    return(mirror)

if __name__ == '__main__':
    strand = input("Enter a series of DNA base pairs:\n")
    print(base_pair(strand))
