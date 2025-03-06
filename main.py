import streamlit as st
import random
import string

def password_generator(length, use_digits, use_special_chars):
    characters = string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def main():
    st.title("Password Generator App")
    length = st.slider("Password Length", 4, 24, 8)
    use_digits = st.checkbox("Use Digits")
    use_special_chars = st.checkbox("Use Special Characters")
    if st.button("Generate Password"):
        is_password = password_generator(length, use_digits, use_special_chars)
        st.success(f'Your password is:   {is_password}')

main()
st.write("This password generator app was created by Tayyab Fayyaz")