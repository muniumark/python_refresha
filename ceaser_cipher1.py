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

#cipher encryption function
def encrypt_text(plaintext,n):

	#empty str variable to be assinged encrypted cipher
	ans = ""

	# loop impelementing e =(a+n)%26 algorithm
	for i in range(len(plaintext)):
		ch = plaintext[i]

		if ch == " ":
			ans+=" "

		# encrypting for uppercase letters
		elif (ch.isupper()):
			ans += chr((ord(ch) + n-65) % 26 + 65)

		# encrypting for lowercase letters
		else:
			ans += chr((ord(ch) + n-97) %26 + 97)

	return ans

#receiving text for encryption
plaintext = str(input("Enter text to encrypt:\n"))
#shift key
n = 6
#function output
print("plain Text is :" + plaintext)
print("Shift pattern is : " +str(n))
print("Cipher text is: " + encrypt_text(plaintext,n))


#brute force decryption function
def decrypt_cipher():

	#function inheritance
	message = encrypt_text(plaintext, n)
	Letters = 'abcdefghijklmnopqrstuvwxyz'

	#brute force loop to find all possible ciphers
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

	#function output
	return key, deciphered


#Clean decrypt function
def decrypt_clean():

	#function inheritance
	encrypted_cipher = encrypt_text(plaintext,n)
	abc_set = 'abcdefghijklmnopqrstuvwxyz'

	#input cipher_key
	cipher_key = int(input("Enter Keygen: "))
	decrypted_cipher = ""

	#loop implementing Cipher(n)=De-cipher(26-n) algorithm
	# *** Possible bug loop does not decipher Uppercase chr ***	
	#resolved bug by adding change to lowercase function .lower()
	for ch in encrypted_cipher.lower():
		if ch in abc_set:
			position = abc_set.find(ch)
			new_pos = (position - cipher_key) % 26
			new_char = abc_set[new_pos]
			decrypted_cipher += new_char
		else:
			decrypted_cipher += ch

	print("Your decrypted_cipher is:\n")
	print(cipher_key, decrypted_cipher)

#calling decrypt functions
if __name__ == '__main__':
	decrypt_cipher(), decrypt_clean()
