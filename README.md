# Password Complexity Checker<br>
A simple Python script that evaluates the strength of a password based on common security best practices. It checks for length, uppercase and lowercase letters, digits, and special characters, then gives user-friendly feedback.

# Features<br>
**Checks password strength based on:**<br>
Minimum length (8 characters)<br>
Uppercase letters<br>
Lowercase letters<br>
Numbers<br>
Special characters<br>
**Gives a strength rating:** Weak, Moderate, or Strong<br>
Explains what criteria are missing<br>
Supports multiple checks in one run<br>
**Password Strength Levels**<br>
Strength	Requirements Met<br>
Strong 	All 5 criteria satisfied<br>
Moderate 	3–4 criteria satisfied<br>
Weak 	Less than 3 criteria satisfied<br>

**Requirements**<br>
Python 3.x<br>
No external libraries needed (re is built-in)

**How to Run**<br>
Clone the repository:<br>
git clone https://github.com/your-username/password-checker.git<br>
cd password-checker<br>
**Run the script:**<br>
python password_checker.py

**Example Output:**<br>
=== Password Strength Checker ===

Enter your password to check: gagan

Password Strength: Weak <br>
Issues found:<br>
 - Too short (minimum 8 characters)<br>
 - Missing uppercase letter<br>
 - Missing digit<br>
 - Missing special character

Check another password? (yes/no): yes<br>
Enter your password to check: Gagan#03

Password Strength: Strong <br>
Your password meets all the criteria.

Check another password? (yes/no): no<br>
Goodbye! Stay secure!

**Author**
Gagan V B<br>
www.linkedin.com/in/gaganvb04
