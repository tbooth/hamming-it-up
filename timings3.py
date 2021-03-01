# Thanks to https://www.geeksforgeeks.org/timeit-python-examples/ for timing examples.
# importing the required modules
import timeit
import random

from hamming import naive_hamming_distance, string_to_hamming_binary, hamming_distance, binary_hamming_dist_calc
from hamming_max_dist import naive_hamming_distance_max_stop, hamming_distance_max_stop, \
    binary_hamming_dist_calc_max_stop, bit_count_max_stop

CHARACTERS = ['A', 'G', 'T', 'C']
def string_generator(size=63, chars=tuple(CHARACTERS)):
    return ''.join(random.choice(chars) for _ in range(size))

length_of_strings = 63
number_of_strings = 10

# compute string hamming time
def string_time():
    SETUP_CODE = '''
from hamming import naive_hamming_distance
from random import choice
from __main__ import string_generator, length_of_strings, number_of_strings
list_of_strings1 = [string_generator(length_of_strings) for i in range(number_of_strings)]
list_of_strings2 = [string_generator(length_of_strings) for i in range(number_of_strings)]'''

    TEST_CODE = '''
s1 = choice(list_of_strings1)
s2 = choice(list_of_strings2)
naive_hamming_distance(s1, s2)
    '''
    # timeit.repeat statement
    times = timeit.repeat(setup=SETUP_CODE,
                          stmt=TEST_CODE,
                          repeat=3,
                          number=10000)

    # printing minimum exec. time
    print('Standard hamming string search time: {}'.format(min(times)))


# compute binary hamming time
def binary_inc_proccessing_time():
    SETUP_CODE = '''
from hamming import hamming_distance
from random import choice
from __main__ import string_generator, length_of_strings, number_of_strings
list_of_strings1 = [string_generator(length_of_strings) for i in range(number_of_strings)]
list_of_strings2 = [string_generator(length_of_strings) for i in range(number_of_strings)]'''

    TEST_CODE = '''
s1 = choice(list_of_strings1)
s2 = choice(list_of_strings2)
hamming_distance(s1, s2)
    '''
    # timeit.repeat statement
    times = timeit.repeat(setup=SETUP_CODE,
                          stmt=TEST_CODE,
                          repeat=3,
                          number=10000)

    # printing minimum exec. time
    print('Binary hamming string search time (including preprocessing): {}'.format(min(times)))


# compute binary hamming time (on preprocessed string to binaries)
def binary_preprocessed_time():
    SETUP_CODE_PREPROCESSED_BINARY = '''
from hamming import string_to_hamming_binary, binary_hamming_dist_calc
from random import choice
from __main__ import string_generator, length_of_strings, number_of_strings
list_of_binary_strings1 = [string_to_hamming_binary(string_generator(length_of_strings)) for i in range(number_of_strings)]
list_of_binary_strings2 = [string_to_hamming_binary(string_generator(length_of_strings)) for i in range(number_of_strings)]'''

    TEST_CODE = '''
s1 = choice(list_of_binary_strings1)
s2 = choice(list_of_binary_strings2)
binary_hamming_dist_calc(s1, s2)
    '''
    # timeit.repeat statement
    times = timeit.repeat(setup=SETUP_CODE_PREPROCESSED_BINARY,
                          stmt=TEST_CODE,
                          repeat=10,
                          number=10000)

    # printing minimum exec. time
    print('Binary hamming string search time (not including preprocessing): {}'.format(min(times)))

# Validate that my alternative approach gives the same result as naive_hamming_distance(s1,s2)
from timming3 import timming_distance
list_of_strings1 = [string_generator() for i in range(10)]
list_of_strings2 = [string_generator() for i in range(10)]
for s1 in list_of_strings1:
    for s2 in list_of_strings2:
        assert timming_distance(s1, s2) == naive_hamming_distance(s1,s2)

# compute binary hamming time (using the Tim method)
def timming_preprocessed_time():
    SETUP_CODE_PREPROCESSED_BINARY = '''
from timming3 import string_to_bin, hamming_dist_calc
from random import choice
from __main__ import string_generator, length_of_strings, number_of_strings
list_of_binary_strings1 = [string_to_bin(string_generator(length_of_strings)) for i in range(number_of_strings)]
list_of_binary_strings2 = [string_to_bin(string_generator(length_of_strings)) for i in range(number_of_strings)]'''

    TEST_CODE = '''
s1 = choice(list_of_binary_strings1)
s2 = choice(list_of_binary_strings2)
hamming_dist_calc(s1, s2)
    '''
    # timeit.repeat statement
    times = timeit.repeat(setup=SETUP_CODE_PREPROCESSED_BINARY,
                          stmt=TEST_CODE,
                          repeat=10,
                          number=10000)

    # printing minimum exec. time
    print('Timming string search time (not including preprocessing): {}'.format(min(times)))

if __name__ == "__main__":
    string_time()
    binary_preprocessed_time()
  #  binary_inc_proccessing_time()
    timming_preprocessed_time()
