def gf_mult(x, y):
    res = 0
    for i in range(127, -1, -1):
        res ^= x * ((y >> i) & 1)  # branchless
        x = (x >> 1) ^ ((x & 1) * 0xE1000000000000000000000000000000)
    return res

H         = 0xbadC0de00000000000000000deadbeef

# same for both messages because of 0 padding
ghash_sum_of_ciphertexts = 0x97548785224854128785214798452558

length_a  = 0x00000000000000000000004f26a8c6f5

length_b  = 0x00000000000000000000004f26a8c6f6

whitening = 0x23876544567898764323456789873453

hash_a = gf_mult(gf_mult(ghash_sum_of_ciphertexts, H) ^ length_a, H) ^ whitening

hash_b = gf_mult(gf_mult(ghash_sum_of_ciphertexts, H) ^ length_b, H) ^ whitening

print(hex(hash_a ^ hash_b))
print(hex(gf_mult(3,H)))

# Okay so it is 3*H over GF2 that one may get as result by downloading
# two strings with and without the terminating 0.

# A possible attack scenario is thus that someone uploads two files to
# some open source sharing site etc. where the 1st is closed with a
# trailing zero byte, the other one this byte shorter. When somebody
# downloads both, hopefully in 2 separately encrypted and signed TLS 1.3
# packets with some AES-GCM based suite, the two hashes XOR will result
# 3*H over GF2 if the encryption key was the same. Then at a 3rd download
# all the ciphertext blocks can be altered if the 3rd downloaded file
# is also known, and contains dump space. For example it may be modified
# to contain any shorter malicious code if it's an executable.
