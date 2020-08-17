# Showcasing under what circumstance a limnear MAC based hash is malleable...

def rolling_hash_by_mac(list):
    hash = 0
    for byte in list:
        hash += byte
        hash *= 0x01000193
        hash %= 2**32
    return(hash)

lista_Pista = [0x58, 0x76, 0x54, 0x3a, 0x0e, 0x58, 0x76, 0x54, 0xbe, 0xcd, 0x45, 0x66, 0x85, 0x65]
#to be set to 0xf* :                   ^^^^
#don't care scratch space:                                                             ^^^^
#powers:       14    13    12    11    10    9     8     7     6     5     4     3     2     1

print(lista_Pista)
print(rolling_hash_by_mac(lista_Pista))

def rolling_hash_hacking(list_in, set_pos, set_data, scratch):
    list_out = list_in
    list_out[set_pos] = list_in[set_pos] + set_data
    list_out[scratch] = list_in[scratch] - set_data*0x01000193**(scratch - set_pos)%2**32
    if list_out[scratch] < 0:
        list_out[scratch] += 2**32
    return(list_out)

lista_Kornel = rolling_hash_hacking(lista_Pista, 4, 0xf0, 12)

print(lista_Kornel)
print(rolling_hash_by_mac(lista_Kornel))
