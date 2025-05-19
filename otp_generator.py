import random
import string

def generate_otp(length=6):
    """Generates a random OTP of the specified length."""
    characters = string.ascii_letters + string.digits
    otp = ''.join(random.choice(characters) for _ in range(length))
    return otp

if __name__ == '__main__':
    print(f"Generated OTP: {generate_otp()}")