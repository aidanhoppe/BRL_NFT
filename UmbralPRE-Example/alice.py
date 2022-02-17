from umbral import SecretKey, Signer
from umbral import encrypt, decrypt_reencrypted
from umbral import generate_kfrags, reencrypt, CapsuleFrag
import random

file = open("pubkeys.txt", "w")

alices_secret_key = SecretKey.random()
alices_public_key = alices_secret_key.public_key()
file.write(repr(alices_public_key)+"\n")

alices_signing_key = SecretKey.random()
alices_verifying_key = alices_signing_key.public_key()
alices_signer = Signer(alices_signing_key)

password = b'username: brlnftasu@gmail.com password: brlnftTest'
capsule, ciphertext = encrypt(alices_public_key, password)
print("Alice successfully encrypts data")

bobs_secret_key = SecretKey.random()
bobs_public_key = bobs_secret_key.public_key()
file.write(repr(bobs_public_key)+"\n")
file.write(repr(capsule) + "\n")
file.write(repr(ciphertext) + "\n")

kfrags = generate_kfrags(delegating_sk=alices_secret_key, receiving_pk=bobs_public_key, signer=alices_signer, threshold=10, shares=20)
print("Alice successfully generate kfrags for bob")

#Bob's part
kfrags = random.sample(kfrags, 10)
cfrags = list()
for kfrag in kfrags:
        cfrag = reencrypt(capsule=capsule, kfrag=kfrag)
        cfrags.append(cfrag) #Bob collects cfrag from Ursula
        print("Bob has collected a cfrag")

#Validate capsule fragments
suspicious_cfrags = [CapsuleFrag.from_bytes(bytes(cfrag)) for cfrag in cfrags]
cfrags = [cfrag.verify(capsule, 
        verifying_pk=alices_verifying_key, 
        delegating_pk=alices_public_key, 
        receiving_pk=bobs_public_key,
        )
    for cfrag in suspicious_cfrags]
print("Cfrags are verified")

cleartext = decrypt_reencrypted(receiving_sk=bobs_secret_key,
        delegating_pk=alices_public_key,
        capsule=capsule,
        verified_cfrags=cfrags,
        ciphertext=ciphertext)
print("Bob successful decryption")


print(cleartext)
