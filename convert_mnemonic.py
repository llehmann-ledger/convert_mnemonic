# pip3 install mnemonic
import hashlib
import hmac
from mnemonic import Mnemonic


def b58encode(v: bytes) -> str:
    alphabet = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"

    p, acc = 1, 0
    for c in reversed(v):
        acc += p * c
        p = p << 8

    string = ""
    while acc:
        acc, idx = divmod(acc, 58)
        string = alphabet[idx: idx + 1] + string
    return string

def to_hd_master_key(seed: bytes, testnet: bool = False) -> str:
    if len(seed) != 64:
        raise ValueError("Provided seed should have length of 64")

     # Compute HMAC-SHA512 of seed
    seed = hmac.new(b"Bitcoin seed", seed,
                    digestmod=hashlib.sha512).digest()

    # Serialization format can be found at: https://github.com/bitcoin/bips/blob/master/bip-0032.mediawiki#Serialization_format
    xprv = b"\x04\x88\xad\xe4"  # Version for private mainnet
    if testnet:
        xprv = b"\x04\x35\x83\x94"  # Version for private testnet
    xprv += b"\x00" * 9  # Depth, parent fingerprint, and child number
    xprv += seed[32:]  # Chain code
    xprv += b"\x00" + seed[:32]  # Master key

    # Double hash using SHA256
    hashed_xprv = hashlib.sha256(xprv).digest()
    hashed_xprv = hashlib.sha256(hashed_xprv).digest()

    # Append 4 bytes of checksum
    xprv += hashed_xprv[:4]

    # Return base58
    return b58encode(xprv)


####################################################################################################


mnemo = Mnemonic("english")

# Ceci n'est pas un message subliminal :)
words = "abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon about"

# Ledger ajoute-t-il une passphrase par défaut ? (Non mentionné dans la doc)
seed = mnemo.to_seed(words, passphrase="")

# BIP32
xprv = to_hd_master_key(seed)
print(xprv)
