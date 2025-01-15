import pyotp
import streamlit as st

def generate_totp_token(secret):
    # Create a TOTP object with the given secret
    totp = pyotp.TOTP(secret)
    
    # Generate the current TOTP token
    token = totp.now()
    
    return token

# Streamlit application layout
st.title("Master Media OTP Generator")

# Ambil parameter 'secret' dari URL
#query_params = st.experimental_get_query_params()
query_params = st.st.query_params()

# Cek apakah parameter 'secret' ada
if 'secret' in query_params:
    secret_key = query_params['secret'][0]  # Ambil nilai secret dari URL
    token = generate_totp_token(secret_key)
    st.success(f'TOTP Token Anda: {token}')
else:
    st.error("Tidak ada secret key di URL. Harap tambahkan secret key pada query parameter.")
