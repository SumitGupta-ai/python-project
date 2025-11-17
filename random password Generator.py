#password Generator (project)

import random
import string

password_length = int(input("Enter the dedired password length: "))

all_character = string.ascii_letters + string.digits 

password_charecter = random.choices(all_character,k=password_length)

final_password = ''.join(password_charecter)

print(f"Your Generate Password is", final_password)

