Application Tracker (GUI Version)

A lightweight desktop application built with Python and Tkinter to help you track job, internship, or university applications in one place.
This version features a graphical user interface (GUI) with persistent local storage.

🚀 Features

Add applications with:

Company / Institution

Program / Role

Date applied

Track application status:

Applied

Interview

Offer

Rejected

Update status via dropdown menu

Delete applications with confirmation

Automatic saving using a local JSON file

Simple, clean Tkinter-based UI

Background image support (optional)

🖥️ Tech Stack

Python 3

Tkinter (standard Python GUI library)

Pillow (PIL) for image handling

JSON for local data storage

All libraries used are standard or widely adopted in Python desktop development.

📦 Installation & Setup
1. Clone the repository
git clone https://github.com/chienvuongdinh44/Application-tracker.git
cd Application-tracker

2. Install dependencies

Pillow is required:

pip install pillow


Verify installation:

python3 -c "from PIL import Image; print('Pillow installed')"

▶️ Running the App

From the project directory:

python3 app.py


The application window will open immediately.

🗂️ Data Storage

Application data is stored locally in:

application.json


Data is automatically loaded on startup and saved on every change.

⚠️ This file is local only and not synced unless you explicitly commit it.

🖼️ Background Image (Optional)

If using a background image:

Place the image in the project folder

Update this line in app.py:

bg_image = Image.open("background.png")


Ensure the file exists to avoid runtime errors.

📁 Project Structure
Application-tracker/
│
├── app.py
├── application.json
├── background.png   (optional)
├── README.md
└── .gitignore

📌 Notes

This is a desktop application, not a web app

Designed for personal use and learning purposes

Compatible with macOS, Windows, and Linux (Python 3 required)
