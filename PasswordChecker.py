#Gerson Antunes
#PasswordChecker


import datetime

def main():
    # Define the minimum and maximum allowed password lengths (Constants)
    MIN_PASSWORD_LENGTH = 6
    MAX_PASSWORD_LENGTH = 10

    # Display the program title and developer information
    print("PasswordChecker developed by: Gerson.")

    # Open the log file to record invalid passwords
    output_file = open("password_log_Gerson.txt", "w")

    # Prompt the user to enter a password
    password = input("Enter your password: ")

    # Get the length of the password
    password_length = len(password)

    # Validate password length and log invalid entries
    while password_length < MIN_PASSWORD_LENGTH or password_length > MAX_PASSWORD_LENGTH:
        # Log the invalid password attempt with the current date and time
        current_date_and_time = datetime.datetime.today()
        if password_length < MIN_PASSWORD_LENGTH:
            output_file.write(f"{current_date_and_time}, password < 6\n")
            print("Password is too short. Must be between 6 and 10 characters.")
        elif password_length > MAX_PASSWORD_LENGTH:
            output_file.write(f"{current_date_and_time}, password > 10\n")
            print("Password is too long. Must be between 6 and 10 characters.")

        # Prompt for re-entry of the password
        password = input("Please re-enter your password: ")
        password_length = len(password)

    # Determine the strength of the password
    if password.isalpha():
        message = f"The password has {password_length} characters and is weak - only contains letters."
    elif password.isnumeric():
        message = f"The password has {password_length} characters and is weak - only contains numbers."
    else:
        message = f"The password has {password_length} characters and is strong."

    # Print the message about the password strength
    print(message)

    # Close the log file after password validation
    output_file.close()

    # Read and output the log file content to the screen
    print("\nLog file contents:")
    with open("password_log_Gerson.txt", "r") as file:
        for line in file:
            print(line.strip())


# Call the main function to run the program
main()