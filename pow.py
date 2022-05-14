import hashlib
import random
import string
import time
import statistics
import numpy

M="I Love Data Security Class So Much"

def nonce_generation(inp=M, size=16):
    nonce =''.join(random.choice(string.ascii_lowercase + string.digits) for x in range(size))
    return nonce

shaHashfunction=hashlib.sha256()

def convert_hex_to_dec(hex_inp):
    return int(hex_inp,16)

def convert_to_bin(int_inp):
    return format(int_inp, "b")

#Core function that takes in a string and number of leading zeroes

def pow_attempt(M, k):
    tries=0
    tries_list=[]
    count=0
    Found=False
    while Found==False:
        nonce = nonce_generation()
        shaHashfunction.update((M+nonce).encode())
        sol = (convert_hex_to_dec(shaHashfunction.hexdigest()))
        val = sol >> (256-k)
        if not val:
            print(shaHashfunction.hexdigest(),", ", nonce, ", ",tries, ", ", "for k = {}".format(k))
            Found=True
            count +=1
        tries +=1
        tries_list.append([tries])
        std_dev=numpy.std(tries_list)
    # print(std_dev)
    # print(tries_list)

    return "Average = ",tries/10, " Standard deviation = ",std_dev

for k in range(2,10,2):
    print()
    for x in range(9):
        pow_attempt(M,k)

    print(pow_attempt(M,k))




