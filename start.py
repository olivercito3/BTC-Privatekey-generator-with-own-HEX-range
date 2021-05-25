#!/usr/bin/env python

import secrets
import json
import codecs
import ecdsa
import hashlib
import base58
import requests
import time
from smtplib import SMTP_SSL as SMTP
import logging
import random as r


wif = ""





def ping_address(publicAddress):
	global pk
	global wif
	global publicKey


	resp = requests.get("https://blockstream.info/api/address/"+ publicAddress)

	if resp.ok:
		ourJSON = resp.json()
		balance = dict(ourJSON['chain_stats'])['funded_txo_sum']
		print( balance )

	else:
		print(resp.text)
		raise ValueError("cannot reach block explorer for balance", resp)


	if float(balance) > 0.00000000:
		logging.info (''+ time.strftime("%m-%d-%y %H:%M:%S") +','+ wif.decode('utf-8') +','+publicAddress+' ,balance '+str(balance))

		print( "Congratulations, YOU DID IT" )
		print(wif.decode('utf-8'))
		with open('results.txt', 'a+') as f:
			f.write(''+ time.strftime("%m-%d-%y %H:%M:%S") +','+ wif.decode('utf-8') +','+publicAddress+' ,balance '+str(balance))
			f.close


def wif_conversion(pk):
	global wif
	padding = '80' + pk
	# print( padding )

	hashedVal = hashlib.sha256(codecs.decode(padding, 'hex')).hexdigest()
	checksum = hashlib.sha256(codecs.decode(hashedVal, 'hex')).hexdigest()[:8]
	# print( hashedVal )
	# print( padding+checksum )

	payload = padding + checksum
	wif = base58.b58encode(codecs.decode(payload, 'hex'))
	print( wif.decode('utf-8') )


while True:
    ran = r.randrange(415051741658795330514, 830103483316929822451+1)
    pk = "%064x" % ran
    #pk = secrets.token_hex(32)
    wif_conversion(pk)

    sk = ecdsa.SigningKey.from_string(codecs.decode(pk, "hex"), curve=ecdsa.SECP256k1)
    vk = sk.get_verifying_key()
    publicKey = "\04" + str(vk.to_string())
    ripemd160 = hashlib.new('ripemd160')
    ripemd160.update(hashlib.sha256(codecs.encode(publicKey)).digest())
    networkAppend = b'\00' + ripemd160.digest()
    checksum = hashlib.sha256(hashlib.sha256(networkAppend).digest()).digest()[:4]
    binary_address = networkAppend + checksum
    publicAddress = base58.b58encode(binary_address)
    print( publicAddress.decode('utf-8') )
    while True:
        try:
            ping_address(publicAddress.decode('utf-8'))
            # probably does nothing...who knows ;)
            time.sleep(.3)
        except ValueError:
            print( "we got Timed Out" )
            print( pk )
            print( publicAddress )
            time.sleep(3)
            continue
        except KeyError:
            print( "we may be denied or something, keep the script moving" )
            time.sleep(4)
        break
