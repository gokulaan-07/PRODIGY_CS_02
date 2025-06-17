import re

def check_password_strength(password):
    length_error = len(password) < 8
    lowercase_error = re.search(r"[a-z]", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    digit_error = re.search(r"\d", password) is None
    special_char_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    # Score system
    score = 5 - sum([length_error, lowercase_error, uppercase_error, digit_error, special_char_error])

    if score == 5:
        strength = "Very Strong"
    elif score == 4:
        strength = "Strong"
    elif score == 3:
        strength = "Moderate"
    elif score == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"

    # Feedback
    feedback = []
    if length_error:
        feedback.append("Password must be at least 8 characters.")
    if lowercase_error:
        feedback.append("Add lowercase letters.")
    if uppercase_error:
        feedback.append("Add uppercase letters.")
    if digit_error:
        feedback.append("Add numbers.")
    if special_char_error:
        feedback.append("Add special characters (e.g., !, @, #, $).")

    return strength, feedback


# Example usage
if __name__ == "__main__":
    password = input("Enter a password to check strength: ")
    strength, suggestions = check_password_strength(password)

    print(f"\nPassword Strength: {strength}")
    if suggestions:
        print("Suggestions to improve:")
        for suggestion in suggestions:
            print(f"- {suggestion}")
