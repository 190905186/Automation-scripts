import streamlit as st
import csv
from cryptography.fernet import Fernet
from cryptography.fernet import InvalidToken

# Custom encryption key (hardcoded)
# If u are planning to use this script on a shared platform make sure to save this key in a separate secured file.
CUSTOM_ENCRYPTION_KEY = b'u7wGgNdDFefqpr_kGxb8wJf6XRVsRwvb3QgITsD5Ft4='
file_name = 'credentials.csv'
# Function to encrypt password


def encrypt_password(password):
    cipher_suite = Fernet(CUSTOM_ENCRYPTION_KEY)
    encrypted_password = cipher_suite.encrypt(password.encode())
    return encrypted_password

# Function to decrypt password


def decrypt_password(encrypted_password):
    if isinstance(encrypted_password, bytes):
        try:
            cipher_suite = Fernet(CUSTOM_ENCRYPTION_KEY)
            decrypted_password = cipher_suite.decrypt(encrypted_password)
            return decrypted_password.decode()
        except InvalidToken:
            return "Invalid Token"
    else:
        return None

# Function to save website name and password to CSV file


def save_credentials(website_name, password):
    encrypted_password = encrypt_password(password)
    with open(file_name, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        # Ensure storing string representation
        writer.writerow([website_name, encrypted_password.decode()])

# Function to retrieve password from CSV file


def retrieve_password(website_name):
    with open(file_name, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row[0] == website_name:
                encrypted_password = row[1].encode()
                return encrypted_password
    return None


# Streamlit UI
st.title("Password Manager")

# Input fields for website name and password
website_name = st.text_input("Enter website name:")
password = st.text_input("Enter password:", type="password")

# Save button to save website name and password
if st.button("Save"):
    if website_name and password:
        save_credentials(website_name, password)
        st.success("Website name and password saved successfully.")
    else:
        st.error("Please fill in all fields.")

# Retrieve button to retrieve password
if st.checkbox("Retrieve Password"):
    website_name = st.selectbox("Select website name:", options=[
                                ""] + [row[0] for row in csv.reader(open(file_name, 'r'))])
    key = st.text_input("Enter Your Encryption Key:", type="password")
    if st.button("Retrieve Password"):
        if key == str(CUSTOM_ENCRYPTION_KEY.decode()):
            if website_name:
                encrypted_password = retrieve_password(website_name)
                if encrypted_password:
                    decrypted_password = decrypt_password(encrypted_password)
                    st.success(
                        f"Password for **{website_name}** -> **{decrypted_password}**")
                else:
                    st.error("Password not found in database.")
        else:
            st.error("Invalid Encryption Key!!!")
