##### Environment Variable #####

# Write a program that accesses the environment variables named 
# USERNAME and PASSWORD and outputs their values in the followng format.

# Username: username_from_environment_variable
# Password: password_from_environment_variable

import os

USERNAME = os.environ.get('USERNAME')
PASSWORD = os.environ.get('PASSWORD')

print(f"Username: {USERNAME}")
print(f"Password: {PASSWORD}")