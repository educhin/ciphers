#!/usr/bin/python 
import string as STRING
import argparse

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
group.add_argument("-d", "--decrypt", type=str, nargs=1, default=None, help="Use this flag to decrypt the message you provide")
group.add_argument("-e", "--encrypt", type=str, nargs=1, default=None, help="Use this flag to encrypt the message you provide" )
parser.add_argument("-f","--file", action="store_true", help="Use this flag so that your file name will not be treated as a string")
args = parser.parse_args()


def encrypt(string, key):
  # takes in a string and rotates each character by 13 places 
  arr = []
  for el in string:
    #print(el)
    if el in STRING.ascii_lowercase:
      char = chr((ord(el) - 96 + key) % 26 + 96)
      arr.append(char)
    elif el in STRING.ascii_uppercase:
      char = chr((ord(el) - 64 + key) % 26 + 64)
      arr.append(char)
    else:
      arr.append(el)
  return ''.join(arr)

if args.decrypt != None:
  print("decrypting...")
  decrypted_value = encrypt(args.decrypt[0], -13)
  print(decrypted_value)
elif args.encrypt != None:
  print("encrypting...")
  encrypted_value = encrypt(args.encrypt[0], 13)
  print(encrypted_value)
