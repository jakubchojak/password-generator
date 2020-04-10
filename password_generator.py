import random
import sys
import pyperclip

try:
    if sys.argv[1] == '-l':
        pass_length = int(sys.argv[2])
    elif sys.argv[1] == '-h':
        print("Use -l <value> to set password's length")
        sys.exit()
except(IndexError):
    print("Oops something went wrong! Use -h instead.")
    sys.exit()
characters = "ABCDEFGHIJKLMNOPRSTUVWXYZabcdefghijklmnoprstuvwxyz1234567890!#$@*&^%"
passw = ''
if pass_length < 12:
    print("ALERT! Password will be shorter than 12 characters!")
for i in range(pass_length):
    passw += characters[random.randint(0, len(characters) - 1)]
print(passw)
pyperclip.copy(passw)