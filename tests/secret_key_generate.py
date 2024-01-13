#Test script to generate JWT token
#
#Osman Elias 1/12/2024

import secrets


secret_key = secrets.token_urlsafe(16)  # Generates a 16-byte (128-bit) key
print(secret_key)