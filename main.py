import streamlit as st
import random
import string
import re

# Function to generate a password
def password_generator(length, use_digits, use_special_chars):
    characters = string.ascii_letters

    # Add digits to the character set if selected
    if use_digits:
        characters += string.digits
    # Add special characters to the character set if selected
    if use_special_chars:
        characters += string.punctuation
    # Generate the password
    is_password = ''.join(random.choice(characters) for _ in range(length))
    return is_password

# Function to check password strength
def password_checking(is_password):
    # Check if the password meets various criteria
    length_check = len(is_password) >= 8
    uppercase_check = bool(re.search(r"[A-Z]", is_password))
    lowercase_check = bool(re.search(r"[a-z]", is_password))
    digit_check = bool(re.search(r"\d", is_password))
    special_char_check = bool(re.search(r"[@#$%&()_\-!<>/?[\]{}*]", is_password))  # Special characters check

    # Count failed conditions
    checks = [length_check, uppercase_check, lowercase_check, digit_check, special_char_check]
    failed_checks = checks.count(False)

    # Determine password strength
    if failed_checks == 0:
        return "🔥 Strong Password 💪✅"
    elif failed_checks <= 2:
        return "⚠️ Moderate Password"
    else:
        return "❌ Weak Password"

# Main function to run the Streamlit app
def main():
    st.title("🔐 Password Generator & Strength Checker")

    # Streamlit UI for the Password generator 
    st.header("🛠 Generate a Secure Password")

    # User inputs for password generation
    length = st.slider("Password Length", 4, 24, 8)
    use_digits = st.checkbox("Use Digits (0-9)")
    use_special_chars = st.checkbox("Use Special Characters (!@#$%&)")

    # Generate password button
    if st.button("🔄 Generate Password"):
        is_password = password_generator(length, use_digits, use_special_chars)
        st.success(f'Your password is:   {is_password}')

    # Section to check password strength
    st.header("🔎 Check Password Strength")

    # User input for password strength checking
    is_password = st.text_input("Enter the Password", type="password")
    
    # Check strength button
    if st.button("✅ Check Strength"):
        result = password_checking(is_password)
        st.write(result)

    st.write("---")
    st.write("👨‍💻 **This password generator app was created by Tayyab Fayyaz**")

# Run the main function
main()
