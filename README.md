# You're gonna 7 me 4 this

A linear multiply accumlate based hash is malleable under not so strict circumstances. The data to be modified needs a following scratch space, where the ripples of the modification can be dumped. As far as I know AES-GCM's Galois hash is just like this - the only difference is that the MAC is over Galois field. Although the subkey H is necessarily needed to perform this.

Some not so real life examples:
* A scenario inbetween two financial institutions: "charge my bank account with 0000100USD, notice box: this is a present" and the receiver bank charges 1000100USD, and claims, that it has received a message like "charge my bank account with 1000100USD, notice box: hg4"65/%@<#gi(/Rt" and again the messages may have the same hash as the original since H is known by both parties. (But who would donate 100 bucks to a bank???)
* Or a regular download site sends regular data to most users, but sends ones containing a virus to some dedicated people, who should understand whom they should stop messing with, but since they could have forged the files themselves, can't claim it has come with the download from the website. A perfect tool for hacker groups and companies to play around with one another.
