import sys
import argparse

parser = argparse.ArgumentParser(description='Simple steganography program based on the LSB method.')
parser.add_argument('a', help='file or message to encode (if none, will read host)', nargs='*')
parser.add_argument('b', help='host file')
parser.add_argument('-p', '--password', help='set password to encrypt or decrypt a hidden file', nargs='?')
parser.add_argument('-b', '--bits', help='number of bits per byte (default is 2)', nargs='?', default=2, choices=['1', '2', '4'])
parser.add_argument('-c', '--check', help='check free space of argument files', action='store_true')
args = parser.parse_args()

print(args.password)