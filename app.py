import pyotp
import streamlit as st
import base64

def generate_totp_token(secret):
    # Ensure the secret key is Base32 padded correctly
    if len(secret) % 8 != 0:
        secret += '=' * (8 - len(secret) % 8)  # Add padding to the secret key if necessary

    try:
        # Create a TOTP object with the given secret
        totp = pyotp.TOTP(secret)
        # Generate the current TOTP token
        token = totp.now()
        return token
    except Exception as e:
        return f"Error generating OTP: {str(e)}"

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
    if token.startswith("Error"):
        st.error(token)
    else:
        st.success(f'TOTP Token Anda: {token}')
else:
    st.error("Tidak ada secret key di URL. Harap tambahkan secret key pada query parameter.")
