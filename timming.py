import re
import numpy as np

# assume strings are same length and limited to given alphabet
def timming_distance(string1, string2):
    """Encode the strings and calc the distance in one go
    """
    b1 = string_to_npm(string1)
    b2 = string_to_npm(string2)

    return hamming_dist_calc(b1, b2)


def hamming_dist_calc(binary1, binary2):
    return count_set_bits( np.bitwise_or(* binary1 ^ binary2) )


# assumes strings only contain given alphabet
def string_to_npm(text):
    """Encode a string for fast Hamming. The string must be composed of ATCG,
       but this could be made generic.
    """
    encoding = dict( A = (0,0),
                     C = (0,1),
                     G = (1,0),
                     T = (1,1) )

    return np.stack( np.packbits([encoding[l][n] for l in text]) for n in (0,1) )


def count_set_bits(v, lt = np.array([bin(i).count('1') for i in range(256)]).astype(np.uint8)):
    """Nicked from @mborgerding
       https://github.com/numpy/numpy/issues/16325
        returns the count of set bits in each element of v
    """
    return lt[v].sum()

