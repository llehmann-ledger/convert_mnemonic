# pip3 install mnemonic pycryptodome
from mnemonic import Mnemonic
from Crypto.Hash import SHA512
import base64
import binascii

mnemo = Mnemonic("english")

# Ceci n'est pas un message subliminal :)
words = "abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon about"

# Ledger ajoute-t-il une passphrase par défaut ? (Non mentionné dans la doc)
seed = mnemo.to_seed(words, passphrase="")

# TODO

# Convert public key to readable algorand address
publickey = "89afdb83e3b65d9ec966e5a126a0aa41b826df9571f5bc0897efbbad8e0402f7"

h = SHA512.new(truncate="256")
h.update(bytes(publickey, 'utf-8'))

res = h.digest()
tmp = binascii.unhexlify(publickey) + res[-4:]

# Python use RFC3548 and padding giving the wrong result
address = base64.b32encode(tmp)
