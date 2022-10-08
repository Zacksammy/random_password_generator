#code written and tested by @zacksammy

import string, secrets
chrs =  string.ascii_letters
numbers = string.digits

choose = input("choose your security,password/pin?: ")
length = input("Ënter your password/pin length: ")

password_in_chrs = ''.join(secrets.choice(chrs)for i in range(int(length)))
password_in_numbers = ''.join(secrets.choice(numbers)for i in range(int(length)))

print("***********Password Generator***********")

#the if statement written here will decide if its a password or pin you want to generate

if choose == "password":
    print(password_in_chrs)

if choose == "pin":
    print(password_in_numbers)


