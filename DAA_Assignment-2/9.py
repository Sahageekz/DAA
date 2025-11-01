#Hack a OTP authentication system using brute force methodology, where OTP is of 4 digits long

import random

def generate_otp():
    return f"{random.randint(0,9999):04d}"

def brute_force_local(secret):
    for attempts in range(10000):
        guess = f"{attempts:04d}"
        if guess == secret:
            return attempts + 1, guess  
    return None, None

if __name__ == "__main__":
    secret = generate_otp()
    
    attempts, found = brute_force_local(secret)
    if found is not None:
        print(f"Found OTP {found} in {attempts} attempts (local simulation).")
    else:
        print("OTP not found (unexpected).")
