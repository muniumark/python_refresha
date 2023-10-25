#!/usr/bin/env python3
# Ceaser Cipher L1 
# 24 OCT 2023
# Practice Model

"""
 Pre-requisites:
	
	- For loop
	- ord in python 
	- String in python

"""

def encrypt_text(plaintext,n):

	ans = ""

	for i in range(len(plaintext)):
		ch = plaintext[i]

		if ch == " ":
			ans+=" "

		elif (ch.isupper()):
			ans += chr((ord(ch) + n-65) % 26 + 65)

		else:
			ans += chr((ord(ch) + n-97) %26 + 97)

	return ans

plaintext = "HELLO EVERYONE"
n = 6
print("plain Text is :" + plaintext)
print("Shift pattern is : " +str(n))
print("Cipher text is: " + encrypt_text(plaintext,n))



def decrypt_cipher():

	message = encrypt_text(plaintext, n)
	Letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

	for key in range(len(Letters)):
		deciphered = ''
		for ch in message:
			if ch in Letters:
				num = Letters.find(ch)
				num = num - key
				if num < 0:
					num = num + len(Letters)
				deciphered = deciphered + Letters[num]

			else:
				deciphered = deciphered + ch

		print('Possible deciphers are %s: %s' % (key, deciphered))

	return key, deciphered

if __name__ == '__main__':
	decrypt_cipher()





