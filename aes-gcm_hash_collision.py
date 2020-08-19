# Demonstrating collision generation on AES-GCM's Galois hash with barly no computational price at all.

def gf_mult(x, y):
    res = 0
    for i in range(127, -1, -1):
        res ^= x * ((y >> i) & 1)  # branchless
        x = (x >> 1) ^ ((x & 1) * 0xE1000000000000000000000000000000)
    return res

def gcm_H(lst, h):
    hash = 0
    for l in lst:
        hash ^= l
        hash = gf_mult(hash, h)
    return(hash)
    
def string2ints(s):
    slices = [s[(i*16):((i+1)*16)] for i in range(len(s)//16)]
    int128list = []
    for slice in slices:
        int128 = 0
        for c in slice:
            int128 *= 256
            int128 += ord(c)
        int128list.append(int128)
    return(int128list)

def ints2string(ints):
    s1 = ""
    for i in ints:
        s2 = ""
        while i > 0:
            s2 = chr(i%256) + s2
            i //= 256
        s1 += s2
    return(s1)

# keyed hash's key

H = 0x2421257badc0de87587deadbeef58664

 # text to be hacked

string_a = "Mind the gap!!! Mind the gap!!! Don't care data begins here...!!"
list_a  = string2ints(string_a)
print("Original text:   ", ints2string(list_a))
print("Original's hash: ", hex(gcm_H(list_a, H)))

# text to hack with

string_b = "Mined a crap... Mined a crap... "
list_b  = string2ints(string_b)

# dumping on the first 128 bits of the don't care data field

H_pow1 = H
H_pow2 = gf_mult(H, H)
list_hack = 0
list_hack ^= gf_mult(list_a[0] ^ list_b[0], H_pow2)
list_hack ^= gf_mult(list_a[1] ^ list_b[1], H_pow1)
list_c = [list_b[0], list_b[1], list_a[2] ^ list_hack, list_a[3]]

print("Colliding text:  ", ints2string(list_c))
print("Collision's hash:", hex(gcm_H(list_c, H)))

# dumping on the second 128 bits of the don't care data field

H_pow2 = gf_mult(H, H)
H_pow3 = gf_mult(H_pow2, H)
list_hack = 0
list_hack ^= gf_mult(list_a[0] ^ list_b[0], H_pow3)
list_hack ^= gf_mult(list_a[1] ^ list_b[1], H_pow2)
list_c = [list_b[0], list_b[1], list_a[2], list_a[3] ^ list_hack]

print("Colliding text:  ", ints2string(list_c))
print("Collision's hash:", hex(gcm_H(list_c, H)))
