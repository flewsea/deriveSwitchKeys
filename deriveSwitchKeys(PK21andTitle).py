# Derive Switch Keys [PK21, Title]
# SocraticBliss (Mastarifla)
# Copyright 2018 All rights reserved
# Feel free to submit code changes/optimizations/updates

from binascii import unhexlify as uhx, hexlify as hx
from Crypto.Cipher import AES
import sys

master_keys = [ 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
		'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
		'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
		'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX']
			   
package2_key_source = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
titlekek_source = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

def decrypt(keyName, sourceKey):
	for key in range(len(master_keys)):
		#Create our AES MasterKey
		aes_masterKey = AES.new(uhx(master_keys[key]), AES.MODE_ECB)
		#Use our AES MasterKey to Decrypt our Package2/TitleKek Source Key
		dec_sourceKey = aes_masterKey.decrypt(uhx(sourceKey))
		#Print out the Generated Package2/TitleKek Keys [MasterKey Enumerated]
		print('%s%d = %s' % (keyName, key, hx(dec_sourceKey).upper()))

def main():
	try:
		decrypt('package2_key_0', package2_key_source)
		decrypt('titlekek_0', titlekek_source)
	except TypeError:
		print('You forgot to add your prerequisite keys to the script...')
	
if __name__ == '__main__':
	sys.exit(main())
