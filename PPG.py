import random

length = int(input("Enter the length of the password\n"))

letters = int(input("\nDo you want uppercase/lowercase letters?\n(1) Only uppercase letters ABC"
                    "\n(2) Only lowercase letters abc\n(3) Both ABCabc\n(4) None of them\n"))

if letters == 1:
    mode = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
elif letters == 2:
    mode = 'abcdefghijklmnopqrstuvwxyz'
elif letters == 3:
    mode = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
elif letters == 4:
    mode = ''

symbols = int(input('\nDo you want symbols/numbers?\n(1) Only symbols ,.-#+*!"§$%&/()=?@\n(2) Only numbers'
                    '\n(3) Both\n(4) None of them\n'))

if symbols == 1:
    mode += '.-#+*!"§$%&/()=?@.-#+*!"§$%&/()=?@'
elif symbols == 2:
    mode += '012345678901234567890123456789'
elif symbols == 3:
    mode += '0123456789,.-#+*!"§$%&/()=?@'
elif symbols == 4:
    mode = mode

amout = int(input("\nHow many passwords do you need?\n"))

print("\nThese are your passwords:")

for i in range(amout):
    password_temp = random.sample(mode, length)
    password = "".join(password_temp)
    print(password)



