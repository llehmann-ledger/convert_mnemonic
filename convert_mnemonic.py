# pip3 install mnemonic py-algorand-sdk
from mnemonic import Mnemonic
from algosdk import mnemonic
import sys, subprocess, os, base64, binascii

mnemo = Mnemonic("english")

if (len(sys.argv) < 2):
    sys.exit("usage : conver_mnemonic.py 'my mnemonic phrase'")

words = sys.argv[1]

seed = mnemo.to_seed(words, passphrase="")

run_cmd = ["./build/src/privkey_algorand", seed.hex()]
testRun = subprocess.run(run_cmd, stdout=subprocess.PIPE, stdin=None, cwd=os.path.dirname(os.path.realpath(__file__)), stderr=subprocess.PIPE,  bufsize=0, universal_newlines=True, timeout=100)
privatekey = testRun.stdout.partition('\n')[0]

pkey_hex = binascii.unhexlify(privatekey)
algo_mnemonic = mnemonic.from_private_key(base64.b64encode(pkey_hex))

print(algo_mnemonic)