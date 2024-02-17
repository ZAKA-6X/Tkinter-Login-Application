Tkinter Login Application:

This Python script implements a simple login application using Tkinter for the GUI and ttkbootstrap for styling. It validates user input for email and password according to specified criteria and provides feedback on validity. Upon successful validation, it prints the entered username and password and displays a welcome message.
Dependencies

    Python 3.x
    Tkinter
    ttkbootstrap

Description

The script creates a Tkinter window styled with ttkbootstrap, titled "Window-6X" and with dimensions 600x600 pixels. It includes the following components:

    Label: Displays the title "Fire Code" with a custom font.
    Entry: Two entry fields for username and password input.
    Button: Submit button triggering the send() function for validation.
    Label: Displays output messages regarding email and password validity.

The send() function validates the entered email and password according to specific criteria:

    Email validation checks for proper formatting and domain existence.
    Password validation ensures it meets length and complexity requirements, avoiding common patterns like "password" or sequential numbers.
    If both email and password pass validation, it prints the entered username and password and displays a "Welcome Back" message. Otherwise, it provides feedback on the invalid input.

Instructions

    Launch the application by running the script.
    Enter a username and password.
    Click the "Submit" button to validate the input.
    Review the output message for validation feedback.
