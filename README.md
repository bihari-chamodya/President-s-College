President's College Minuwangoda
 
  Project Documentation

 project Structure
 
project-folder/
│── static/
│   ├── css/
│   │   ├── style.css
│   │── templates/
│   ├── index.html   # Home page (Locked after login(stlogin.py))
│   │   ├── about.html     #About page
│   │   ├── contact.html   #Contact page 
│   │   ├── unit.html      #Clubs & Societies page 
│   ├── admin.html   # Admin Dashboard (Locked after login(tlogin.py))
│   │   ├── marks.html          #Student Marks Management page
│   │   ├── achievements.html   #Student Progress & Achievements page
│   │   ├── attendance.html     #Student Attendance page
│   │   ├── report.html         #Student Report Generator page
│── stlogin.py      # Handles student login
│── tlogin.py       # Handles admin login
│   │
│── README.md


python

Description:
This project is a Python-based user authentication system using a modern GUI for login
and signup functionality. The system uses an SQLite database for user management and
ensures secure password handling with the bcrypt library.

Open-Source Libraries and Frameworks Used


1. CustomTkinter
• Purpose: Provides a modern and customizable GUI framework based on tkinter.
It enhances the look and feel of traditional GUIs and offers additional customization
options.
• Source: GitHub Repository
• License: MIT License
• Usage in Project: Used to build the user interface, including buttons, entry fields,
frames, and labels.

2. Pillow (PIL Fork)
• Purpose: A powerful image processing library used for loading and manipulating
images.
• Source: Pillow Documentation
• License: Historical Permission Notice and Disclaimer (HPND) License
• Usage in Project: Used to load and display the login image in the GUI.

3. bcrypt
• Purpose: A library for hashing and verifying passwords using the Blowfish cipher. It
ensures secure storage of user credentials in the database.
• Source: GitHub Repository
• License: Apache License 2.0
• Usage in Project: Used to hash passwords during user registration and verify them
during login.

4. SQLite3
• Purpose: A lightweight database engine included in Python’s standard library for
managing persistent data.
• Source: SQLite Official Site
• License: Public Domain
• Usage in Project: Used to store and retrieve user credentials securely in a local
database.

5. Webbrowser Module
• Purpose: Opens web pages in the default browser.
• Source: Python Standard Library
• License: PSF License (Python Software Foundation)
• Usage in Project: Used to redirect users to the home.html page after successful
login.

6. Tkinter
• Purpose: Python’s standard GUI toolkit used as a base for creating graphical user
interfaces.
• Source: Python Standard Library
• License: PSF License (Python Software Foundation)
• Usage in Project: Provides the base GUI framework, which is further enhanced
using customtkinter.

ALERT

8. SweetAlert2
• Purpose: Used to display stylish and customizable alert dialogs in the project.
• Website: SweetAlert2
• License: MIT License

CSS & JS

9. Bootstrap
• Purpose: Provides responsive design and prebuilt CSS and JavaScript components.
• Website: Bootstrap
• License: MIT License


Backend: Python 

Frontend: HTML, CSS, JavaScript

Database: SQLite3 (admin.db , users.db)
