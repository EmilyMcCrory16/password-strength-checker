import string

def check_length(password):
    return len(password) >= 8

def check_uppercase(password):
    for char in password:
        if char.isupper():
            return True
    return False

def check_lowercase(password):
    for char in password:
        if char.islower():
             return True
    return False

def check_digit(password):
    for char in password:
        if char.isdigit():
            return True
    return False

def check_special(password):
  special_chars = string.punctuation
  for char in password:
      if char in special_chars:
          return True
  return False

def evaluate_strength(length_pass, uppercase_pass, lowercase_pass, digit_pass, special_pass):
    score = sum([length_pass, uppercase_pass, lowercase_pass, digit_pass, special_pass])

    if score == 5:
        return "Strong"
    elif 3 <= score < 5:
        return "Medium"
    else:
        return "Weak"

def main():
    print("Checking password strength...")
    password = input("Enter a password: ")
    
    length_pass = check_length(password)
    uppercase_pass = check_uppercase(password)
    lowercase_pass = check_lowercase(password)
    digit_pass = check_digit(password)
    special_pass = check_special(password)
    
    print("\nPassword Feedback:")

    if length_pass:
         print("✓ Password length is sufficient")
    else:
         print("✗ Password must be at least 8 characters long")

    if uppercase_pass:
        print("✓ Contains an uppercase letter")
    else:
        print("✗ Add at least one upercase letter")
    
    if lowercase_pass:
        print("✓ Contains a lowercase letter")
    else:
        print("✗ Add at least one lowercase letter")
    
    if digit_pass:
        print("✓ Contains a number")
    else:
        print("✗ Add at least one number")

    if special_pass:
        print("✓ Contains a special character")
    else:
        print("✗ Add at least one special charcter")
	

    strength = evaluate_strength(length_pass, uppercase_pass, lowercase_pass,         digit_pass, special_pass)
    print(f"\nOverall Password Strength: {strength}")


if __name__ == "__main__":
    main()
