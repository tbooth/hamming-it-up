# assume strings are same length and limited to given alphabet
def timming_distance(string1, string2):
    """Encode the strings and calc the distance in one go
    """
    b1 = string_to_bin(string1)
    b2 = string_to_bin(string2)

    return hamming_dist_calc(b1, b2)


def hamming_dist_calc(binary1, binary2):
    """Hamming distance by XOR
    """
    return bit_count( (binary1[0] ^ binary2[0]) | (binary1[1] ^ binary2[1]) )


# assumes strings only contain given alphabet
def string_to_bin(text):
    """Encode a string for fast Hamming. The string must be composed of ATCG,
       but this could be made generic.
    """
    encoding = dict( A = (0,0),
                     C = (0,1),
                     G = (1,0),
                     T = (1,1) )

    res = [0b0, 0b0]
    for n in (0,1):
        for l in text:
            res[n] = (res[n] << 1) | encoding[l][n]

    return res


# counter with a lookup table is faster if Hamming distance is high
tsize = 16
tmask = 2**tsize-1
tcounts = [bin(i).count('1') for i in range(2**tsize)]
def bit_count(number):
    count = 0
    while number:
        count += tcounts[number & tmask]
        number >>= tsize
    return count
