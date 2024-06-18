import random
import string 

def pw_generator(length):
    all_charac = string.ascii_letters + string.digits + string.punctuation
    if length <8:
        print("Password length should be at least 8 characters")
        return None
    password = ''.join(random.choice(all_charac)for i in range(length))
    return password

length = int(input("Enter the length of the password:"))
print("Generated Password: ", pw_generator(length))
