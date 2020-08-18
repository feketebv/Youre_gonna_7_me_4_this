# You're gonna 7 me 4 this

A linear multiply accumlate based hash is malleable under not so strict circumstances. The data to be modified needs a following scratch space, where the ripples of the modification can be dumped. As far as I know AES-GCM's Galois hash is just like this - the only difference is that the MAC is over Galois field. Although the subkey H is necessarily needed to perform this.

I guess this situation, that by knowing H a message with colliding hash can be forged, comes into play when Bob texts Mallory, "If you eavesdrop my communication with Alice I fill you!!!!!!!!!" and signes it accidentially, then Mallory can go to the police and claim, that he's been death threatened by Bob with the following signed message: "If you eavesdrop my communication with Alice I kill u u +!@%!(%" where "fill" has been modified to "kill", you to "u u", and the end of the message was used as scratch space, looking like some non-verbal cursing. And it has the same hash, which has been signed.

So all in all do not send texts to people with AES-GCM signed if they can not be trusted not to abuse your signature against you!

A similar scenario inbetween two financial institutions: "charge my bank account with 0000100USD, notice box: this is a present" and the receiver bank charges 1000100USD, and claims it has received a message like "charge my bank account with 1000100USD, notice box: hg4"65/%@<#gi(/Rt" and again the message is may have tha same hash as the original since H is known by both parties...

So generally it can not be proven what a sender has written a with a signed AES-GCM message to any third party, by the receiver, although the receiver can be sure about it. (So ultimately Bob would win against Mallory in front of a cryptographically skilled court, meaning AES-GCM being a perfect tool for successful threatenings with plausible deniability.)
