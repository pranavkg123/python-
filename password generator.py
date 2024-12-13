

import random
import string

def generate_password(length=12, use_uppercase=True, use_numbers=True, use_special_chars=True):
 
    if length < 4:
        raise ValueError("Password length should be at least 4 for a strong password.")
    
    # Define character pools
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase if use_uppercase else ""
    numbers = string.digits if use_numbers else ""
    special = string.punctuation if use_special_chars else ""
    
    all_chars = lower + upper + numbers + special
    
    if not all_chars:
        raise ValueError("At least one character set must be enabled.")
    
    # Ensure the password contains at least one of each selected type
    password = [
        random.choice(lower),
        random.choice(upper) if use_uppercase else random.choice(lower),
        random.choice(numbers) if use_numbers else random.choice(lower),
        random.choice(special) if use_special_chars else random.choice(lower)
    ]
    
    # Fill the rest of the password length with random characters
    password += random.choices(all_chars, k=length - len(password))
    
    # Shuffle to ensure randomness
    random.shuffle(password)
    
    return ''.join(password)

