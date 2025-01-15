import pyotp
import streamlit as st
import base64

def generate_totp_token(secret):
    # Ensure the secret key is Base32 padded correctly
    try:
        # Pad the secret to a length that is a multiple of 8
        padded_secret = secret
        if len(padded_secret) % 8 != 0:
            padded_secret += '=' * (8 - len(padded_secret) % 8)  # Add padding to make the length a multiple of 8
        
        # Create a TOTP object with the given secret
        totp = pyotp.TOTP(padded_secret)
        # Generate the current TOTP token
        token = totp.now()
        return token
    
    except binascii.Error:
        return "Invalid Base32 secret key. Please ensure the key is Base32 encoded."

# Streamlit application layout
st.title("TOTP OTP Generator")

# Ambil parameter 'secret' dari URL
query_params = st.query_params

# Cek apakah parameter 'secret' ada
if 'secret' in query_params:
    secret_key = query_params['secret'][0]  # Ambil nilai secret dari URL
    
    # Generate OTP
    token = generate_totp_token(secret_key)
    
    # Display the result
    if token.startswith("Invalid"):
        st.error(token)
    else:
        st.success(f'TOTP Token Anda: {token}')
else:
    st.error("Tidak ada secret key di URL. Harap tambahkan secret key pada query parameter.")
