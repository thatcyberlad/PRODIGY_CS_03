import re


def password_complexity(password):
    length = len(password)
    uppercase = bool(re.search(r'[A-Z]', password))
    lowercase = bool(re.search(r'[a-z]', password))
    numbers = bool(re.search(r'[0-9]', password))
    special_chars = bool(re.search(r'[!@#$%^&*()-_=+]', password))

    complexity_score = sum([length >= 8, uppercase, lowercase, numbers, special_chars])

    if complexity_score == 5:
        return "Strong password"
    elif complexity_score >= 3:
        return "Medium password"
    elif complexity_score >= 1:
        return "Weak password"
    else:
        return "Password must contain at least one of uppercase, lowercase, number, or special character and have a minimum length of 8 characters"


# Example usage
password = input("Enter your password: ")
print(password_complexity(password))
