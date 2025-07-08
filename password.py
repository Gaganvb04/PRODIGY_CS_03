import re

def check_password_strength(password):
    length_error = len(password) < 8
    lowercase_error = re.search(r"[a-z]", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    digit_error = re.search(r"\d", password) is None
    special_char_error = re.search(r"[!@#$%^&*()_+{}\[\]:;\"'<>,.?/~`\\|-]", password) is None

    errors = {
        "Too short (minimum 8 characters)": length_error,
        "Missing lowercase letter": lowercase_error,
        "Missing uppercase letter": uppercase_error,
        "Missing digit": digit_error,
        "Missing special character": special_char_error
    }

    failed = [msg for msg, err in errors.items() if err]
    passed = len(errors) - len(failed)

    # Determine strength level
    if passed == 5:
        strength = "Strong "
    elif passed >= 3:
        strength = "Moderate "
    else:
        strength = "Weak "

    return strength, failed

def main():
    print("=== Password Strength Checker ===\n")

    while True:
        password = input("Enter your password to check: ").strip()
        strength, feedback = check_password_strength(password)

        print(f"\nPassword Strength: {strength}")
        if feedback:
            print("Issues found:")
            for issue in feedback:
                print(f" - {issue}")
        else:
            print("Your password meets all the criteria.")

        again = input("\nCheck another password? (yes/no): ").strip().lower()
        if again not in ['yes', 'y']:
            print("Goodbye! Stay secure!")
            break

if __name__ == "__main__":
    main()
