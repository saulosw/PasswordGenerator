import random
import string


def generate_random_password(length):
  characters = string.ascii_letters + string.digits + string.punctuation
  password = ''.join(random.choice(characters) for i in range(length))
  return password


def generate_passwords(num_passwords, password_length):
  passwords = [
      generate_random_password(password_length) for _ in range(num_passwords)
  ]
  return passwords


num_passwords = int(input("Enter the number of passwords to generate: "))
password_length = int(input("Enter the length of each password: "))

passwords = generate_passwords(num_passwords, password_length)
for idx, password in enumerate(passwords, 1):
  print(f"Password {idx}: {password}")
