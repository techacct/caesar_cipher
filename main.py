alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

"""
solution 1
if direction == 'encode':

  def encrypt(plain_text, shift_amount):
    cipher_text = ''
    for letter in text:
      position = alphabet.index(letter)
      new_position = position + shift
      new_letter = alphabet[new_position]
      cipher_text += new_letter
    print(f'The encoded text is {cipher_text}')
  encrypt(plain_text=text, shift_amount=shift)
else:
  def decrypt(cipher_text, shift_amount):
    plain_text = ''
    for letter in cipher_text:
      position = alphabet.index(letter)
      new_position = position - shift
      new_letter = alphabet[new_position]
      decryption +=new_letter
    print(f'The decoded text is {plain_text}')
  decrypt(cipher_text=text, shift_amount=shift)
"""
'''
solution2
def encrypt_decrypt(text, shift, direction):
  if direction == 'encode':
 
    cipher_text = ''
    for letter in text:
      position = alphabet.index(letter)
      new_position = position + shift
      new_letter = alphabet[new_position]
      cipher_text += new_letter
    print(f'The encoded text is {cipher_text}')
  else:
    direction == 'decode'
    plain_text = ''
    for letter in text:
      position = alphabet.index(letter)
      new_position = position - shift
      new_letter = alphabet[new_position]
      plain_text +=new_letter
    print(f'The decoded text is {plain_text}')

encrypt_decrypt(text, shift, direction)
'''

'''solution3'''
def caeser(start_text, shift_amount, cipher_direction):
  end_text = ''

  if cipher_direction == 'decode':
    shift_amount *=-1

  for letter in start_text:
    position = alphabet.index(letter)
    new_position = position + shift_amount
    end_text += alphabet[new_position]
  print(f'The {cipher_direction}d text is {end_text}')

caeser(start_text=text, shift_amount=shift, cipher_direction=direction)
  
   

