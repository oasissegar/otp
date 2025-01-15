import pyotp
import streamlit as st

def generate_totp_token(secret):
    # Create a TOTP object with the given secret
    totp = pyotp.TOTP(secret)
    
    # Generate the current TOTP token
    token = totp.now()
    
    return token

# Ambil parameter 'secret' dari URL
query_params = st.experimental_get_query_params()

# Cek apakah parameter 'secret' ada
if 'secret' in query_params:
    secret_key = query_params['secret'][0]  # Ambil nilai secret dari URL
    token = generate_totp_token(secret_key)
    
    # Menampilkan OTP di tengah dengan ukuran font yang besar menggunakan HTML
    st.markdown(f"""
        <div style="display: flex; justify-content: center; align-items: center; height: 50vh;">
            <h1 style="font-size: 50px; font-weight: bold; color: green;">OTP Anda :\n {token}</h1>
        </div>
    """, unsafe_allow_html=True)
else:
    st.error("Tidak ada secret key di URL. Harap tambahkan secret key pada query parameter.")
