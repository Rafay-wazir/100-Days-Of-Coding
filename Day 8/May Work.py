# if direction == "encode":
#   def encrypt(plain_text, shift_amount):
#     cipher_text = ""
#     for letter in plain_text:
#       position = alphabet.index(letter)
#       new_position = position + shift_amount
#       cipher_text += alphabet[new_position]
#     print(f"The encoded text is {cipher_text}")
# elif direction == "decode":
#   def decrypt(cipher_text, shift_amount):
#     plain_text = ""
#     for letter in cipher_text:
#       position = alphabet.index(letter)
#       new_position = position - shift_amount
#       plain_text += alphabet[new_position]
#     print(f"The decoded text is {plain_text}")