# Fire Code Validator GUI:

This Python code creates a visually appealing and secure login form using Tkinter and ttkbootstrap. It incorporates robust validation features for both email and password fields, ensuring user data integrity.

Key features:

    Visually appealing interface: Designed with the "solar" theme from ttkbootstrap for a modern and engaging look.
    
    Email validation: Verifies email address format and checks domain existence for accurate input.
    
    Strong password enforcement: Requires passwords to meet minimum length, complexity, and uniqueness criteria to enhance security.
    
    Clear feedback: Provides informative messages to the user regarding input validity, guiding them towards successful login.
    
    User-friendly layout: Presents input fields and feedback in a clear and intuitive manner.
    
    Potential for expansion: Provides a solid foundation for further development, such as integrating with databases or other functionalities.

Code structure:

    Import necessary modules: tkinter, ttkbootstrap, re, and socket.
    
    Define validation functions: is_valid_email and is_valid_password to check email and password format, respectively.
    
    Create the main window: Using ttkbootstrap's Window class for a stylish interface.
    
    Add title and input fields: Label for the title, frames for input, and entries for username and password.
    
    Implement submit button: Triggers the send function when clicked.
    
    Handle validation and feedback: Inside send, validate email and password, provide feedback through a label, and print valid credentials if successful.
    Run the main loop: Keeps the window open and responsive to user interactions.
