# PasswordChecker
Checks password length and strength, logs invalid attempts, and displays previous failed entries.

This program prompts the user to enter a password and checks if its length is within the valid range of 6 to 10 characters.
If the length is invalid, it logs the date, time, and the reason (either "password < 6" or "password > 10") in a log file called password_log_Gerson and asks the user to re-enter the password.
Once a valid password length is entered, the program then checks if the password contains:
Only letters (alphabetic), in which case it outputs "Password weak - only contains letters."
Only numbers (numeric), in which case it outputs "Password weak - only contains numbers."
A combination of letters and numbers in which case it outputs "Your password is strong."
Additionally, the program outputs the contents of the log file to the screen, displaying all previous invalid password entries.
