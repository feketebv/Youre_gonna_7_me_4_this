# You're gonna 7 me 4 this

A linear multiply accumlate based hash is malleable under not so strict circumstances. The data to be modified needs a following scratch space, where the ripples of the modification can be dumped. In case of a bank transfer for example, maybe the sum needs to get overwritten, and the notice box contents may be arbitrarily changed...

As far as I know AES-GCM's Galois hash is just like this - the only difference is that the MAC is over Galois field.
