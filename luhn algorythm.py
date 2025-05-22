# Luhn algorithm implementation
# The Luhn algorithm is a simple checksum formula used to validate a variety of identification numbers, such as credit card numbers.
# It was created by IBM scientist Hans Peter Luhn and is used to protect against accidental errors, not malicious attacks.
# The algorithm works by taking the number from right to left, doubling every second digit, and then summing all the digits.
# If the total modulo 10 is equal to 0, then the number is valid according to the Luhn formula.
# The algorithm is not a cryptographic hash function, and it is not suitable for protecting sensitive information.
# The Luhn algorithm is used in various applications, including credit card validation, IMEI number validation, and Canadian Social Insurance Number validation.
# The Luhn algorithm is not a secure method of validating numbers, and it should not be used for security purposes.
def verify_card_number(card_number):
    # Initialize the sum of odd digits to 0
    sum_of_odd_digits = 0
    # Reverse the card number to process it from right to left
    card_number_reversed = card_number[::-1]
    # Extract the odd digits
    odd_digits = card_number_reversed[::2]

    for digit in odd_digits:
        # Convert the digit to an integer and add it to the sum of odd digits
        sum_of_odd_digits += int(digit)


    sum_of_even_digits = 0
    # Extract the even digits
    # and double each digit
    even_digits = card_number_reversed[1::2]
   
    for digit in even_digits:
        # Convert the digit to an integer, double it, and add it to the sum of even digits
        # If the doubled number is greater than or equal to 10, add the digits of the result
        number = int(digit) * 2
        if number >= 10:
            number = (number // 10) + (number % 10)
        # Add the number to the sum of even digits
        sum_of_even_digits += number
    # Calculate the total sum of odd and even digits
    total = sum_of_odd_digits + sum_of_even_digits
    # Check if the total modulo 10 is equal to 0
    # If it is, the card number is valid
    # If it is not, the card number is invalid
    return total % 10 == 0

def main():
    # Example card numbers
    card_number = '4111-1111-4555-1141-5'
    card_translation = str.maketrans({'-': '', ' ': ''})
    # Remove spaces and dashes from the card number
    translated_card_number = card_number.translate(card_translation)
    # Check if the card number is valid
    if verify_card_number(translated_card_number):
        print('VALID!')
    # Check if the card number is invalid    
    else:
        print('INVALID!')

main()