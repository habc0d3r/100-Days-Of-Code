alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(start_text, shift_amount, cipher_direction):
  final_text = ""
  encode = False
  decode = True
  for letter in start_text:
    position = alphabet.index(letter)
    if cipher_direction == "encode":
      new_position = position + shift_amount
      encode = True
    elif cipher_direction == "decode":
      new_position = position - shift_amount
    final_text += alphabet[new_position]
  if encode:
    print(f"The encoded text is {final_text}")
  elif decode:
    print(f"The decoded text is {final_text}")

caesar(start_text=text, shift_amount=shift, cipher_direction=direction)