#!/usr/bin/python 
import string as STRING


def decrypt(string):
  # takes in a string and rotates each character by 13 places 
  arr = []
  for el in string:
    print(el)
    if el in STRING.ascii_lowercase:
      char = chr((ord(el) - 96 - 13) % 26 + 96)
      arr.append(char)
    elif el in STRING.ascii_uppercase:
      char = chr((ord(el) - 64 - 13) % 26 + 64)
      arr.append(char)
    else:
      arr.append(el)
  return ''.join(arr)

def encrypt(string):
  # takes in a string and rotates each character by 13 places 
  arr = []
  for el in string:
    print(el)
    if el in STRING.ascii_lowercase:
      char = chr((ord(el) - 96 + 13) % 26 + 96)
      arr.append(char)
    elif el in STRING.ascii_uppercase:
      char = chr((ord(el) - 64 + 13) % 26 + 64)
      arr.append(char)
    else:
      arr.append(el)
  return ''.join(arr)

def run():
  string = input("Please enter the message you would like to encrypt: ")
  encrypted_value = decrypt(string)
  print(encrypted_value)

run()
