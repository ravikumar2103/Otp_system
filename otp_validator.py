# In a real application, you'd likely store generated OTPs
# in a database or a temporary cache with an associated identifier
# (e.g., user ID, email). For this simple example, we'll use an in-memory dictionary.

otp_store = {}

def store_otp(identifier, otp):
    """Stores the OTP associated with an identifier."""
    otp_store[identifier] = otp

def validate_otp(identifier, entered_otp):
    """Validates the entered OTP against the stored OTP for the identifier."""
    if identifier in otp_store and otp_store[identifier] == entered_otp:
        del otp_store[identifier]  # Invalidate after successful verification
        return True
    return False

if __name__ == '__main__':
    test_identifier = "user123"
    generated_otp = "ABC123XYZ" # For testing purposes
    store_otp(test_identifier, generated_otp)
    print(f"Stored OTP for {test_identifier}: {generated_otp}")
    entered = input(f"Enter OTP for {test_identifier}: ")
    if validate_otp(test_identifier, entered):
        print("OTP Verified successfully!")
    else:
        print("Invalid OTP.")