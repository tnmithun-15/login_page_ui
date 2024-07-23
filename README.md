# login_page_ui
Basic Login Page UI using Customtkinter and tkinter 

Login Page
This is a simple login page built using Python's tkinter library along with PIL for image handling and customtkinter for enhanced UI components.

Requirements
Python 3.x
tkinter
PIL (Pillow)
customtkinter
Installation
To install the necessary libraries, run the following commands:

bash
Copy code
pip install pillow
pip install customtkinter
Files
login_page.py: This is the main file containing the code for the login page.
bg2.jpg: The background image used for the login page.
Code Explanation
Initialization
The script starts by importing the necessary modules: tkinter for the GUI, messagebox for pop-up messages, PIL.Image and ImageTk for image handling, and customtkinter for custom-styled widgets.

Creating the Main Window
The main window (root) is created as an instance of ctk.CTk.
The window title is set to 'Login Page'.
The window is made non-resizable.
The background color is set to white.
Adding the Background Image
The background image (bg2.jpg) is loaded using PIL.Image and resized to 500x500 pixels.
The image is converted to a PhotoImage object.
A CTkLabel is used to display the background image.
Creating the Login Frame
A frame (frame) is created to hold the login widgets.
The frame is styled with a background color, foreground color, height, width, and corner radius.
The frame is positioned using the grid layout manager.
Adding Widgets to the Frame
Welcome Label: A CTkLabel displaying a welcome message.
Email Entry: A CTkEntry for the user to enter their email/username.
Password Entry: A CTkEntry for the user to enter their password. The show parameter is set to '*' to hide the password characters.
Login Button: A CTkButton to trigger the login function when clicked.
Login Function
The login function retrieves the email and password entered by the user.
It checks if the email and password match the hardcoded credentials ('admin@mail.com' and 'admin').
Depending on the match, it shows appropriate message boxes for successful login, missing password, missing email, or incorrect credentials.
After each attempt, the email and password fields are cleared.
Running the Main Loop
root.mainloop() is called to start the GUI event loop.
Usage
To run the login page, simply execute the login_page.py script:

bash
Copy code
python login_page.py
A window will appear with a login form. Enter the credentials and click the "Login" button to see the results.

Notes:
Ensure bg2.jpg is in the same directory as login_page.py.
The login credentials are hardcoded for demonstration purposes. In a real application, you would check against a database or other secure storage.





![Screenshot 2024-07-23 160647](https://github.com/user-attachments/assets/c10ffd3b-527c-4b43-9633-81927bf19627)



