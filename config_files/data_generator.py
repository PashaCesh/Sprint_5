import random
import secrets
import string

def generate_email(email_name, email_domain):
    random_digits = ''.join(str(random.randint(0, 9)) for _ in range(3))
    return f"{email_name}{random_digits}@{email_domain}"


name = "pavellopukhov16"
domain = "gmail.com"
email = generate_email(name, domain)

def generate_secure_password(length=6):
  characters = string.ascii_letters + string.digits
  password = ''.join(secrets.choice(characters) for i in range(length))
  return password

new_password = generate_secure_password()