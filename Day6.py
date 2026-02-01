#Day 6 Task: Write a function that checks if a password meets complexity rules.

# Ask the user for a password, and check to make sure the password fulfills complexity requirements:
# It needs to be at least 20 characters long.
# It needs to have both upper and lower case letters.
# It needs to have at least 1 number.
# It needs to have at least 1 special character.
def main():
    password = input("What is the password you would like to test? ")
    good_len = len(password) >= 20
    has_letters = check_letter_complexity(password)
    has_numbers = check_numbers(password)
    has_spec_char = check_special_char(password)

    if good_len and has_letters and has_numbers and has_spec_char:
        print("Congratulations! You have a strong password.")
        return
    if not good_len:
        print("Your password is too short.")
       
    if not has_letters:
        print("You need both upper and lower case letters in your password.")
     
    if not has_numbers:
        print("Your password needs to include at least 1 number.")
        
    if not has_spec_char:
        print("Your password needs to include at least 1 special character.")

#Check password for both upper and lower case letters
def check_letter_complexity(password):
    return any(letter.isupper() for letter in password) and any(letter.islower() for letter in password)

#Check password for the presence of at least 1 number
def check_numbers(password):
    return any(char.isdigit() for char in password)

#Check password for the presence of at least 1 special character
def check_special_char(password):
    special_chars = set(" !\"#$%&'()*+,-./:;<=>?@[\]^_`{\|}~")
    return any(letter in special_chars for letter in password)

if __name__ == "__main__":
    main()

# Lessons learned today:
# The any() function is a boolean check to see if any item in an iterable is True. In this case, the 
# iterable is the password string that gets passed to the function. 