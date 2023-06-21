# Secret of Ravan

### Challenge Description

Ram discovers that Ravan has a single weakness, and to defeat him, Ram needs to know this weakness.<br />
Ram learns that the secret to Ravan's weakness is hidden in a locked box, which can only be opened with a special password.<br />
Vibhishan knows that the password is a combination of 8 characters that include numbers, letters and special characters, but he only knows 6 of them.<br />
Can you find the password through brute force so that Ram can open the box?<br />
Write a Python program for brute-forcing.

##### Instructions -
- The locked box is provided as a zipped folder named `The_secret.zip`. (Use the pyzipper library in Python to extract it)
- Some of the code for the brute force program is already provided in the Python file named `Task - 02.py`.
- Submit the commented code, the extracted file containing the hint, and a README file explaining the approach. (Note: The explanation carries significant weightage.)
 

##### To do -
- First, install pyzipper by running the following command in the terminal:
```
pip install pyzipper
```
(Refer to the library's documentation by clicking [here](https://pypi.org/project/pyzipper/)).
- The known passowrd is: 
```
n_^{*}`W{*}5
```
(Here `{*}` represents the missing character that needs to be found, while the other 6 characters are known)
- Use the provided list inside the Python file for brute-forcing the characters.

### Explanation:
- I used two for loops over the characters array, each corresponding to 4th and 7th characters in password.
- Using pyzipper module, i try to unzip the given zipped folder using the password found above.
- If its correct password, it unzips the folder, and prints the password in terminal and program is exited. else, it goes to next iteration.

