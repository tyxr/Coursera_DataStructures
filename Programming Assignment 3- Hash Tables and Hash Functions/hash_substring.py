# python3
import random
def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences1(pattern, text):
    temp = []
    hvalue = hash_func(pattern)
    for i in range(len(text) - len(pattern) + 1):
        if hash_func(text[i:i + len(pattern)]) == hvalue:
            if text[i:i + len(pattern)]==pattern:
                temp.append(i)
        else:
            pass
    return temp
def hash_func(s):
    
    ans = 0
    for c in reversed(s):
    	ans = (ans * multiplier  + ord(c)) % prime
    return ans

def precompute_hashes(text, plength):
    H = [0] * (len(text) - plength + 1)
    s = text[-plength:]
    H[len(text)-plength] = hash_func(s)
    y = 1
    for i in range(1, plength+1):
        y = (y * multiplier) % prime
    for i in reversed(range(len(text) - plength)):
        prehash = multiplier * H[i + 1] + ord(text[i]) - y * ord(text[i + plength])
        while(prehash < 0):
            prehash += prime
        H[i] = prehash % prime
    return H

def get_occurrences2(pattern, text):
    global multiplier ,prime
    prime = 1000000007
    multiplier = random.randint(1, prime)
    tlength = len(text)
    plength = len(pattern)
    phash = hash_func(pattern)
    H = precompute_hashes(text, plength)
    return [
        i 
        for i in range(len(text) - len(pattern) + 1) 
        if phash == H[i] and text[i:i + len(pattern)] == pattern
    ]

if __name__ == '__main__':
    print_occurrences(get_occurrences2(*read_input()))

