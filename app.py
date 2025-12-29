import tkinter as tk
from tkinter import messagebox
import json
import os
from PIL import Image, ImageTk  # Pillow library, install with pip install pillow
# ----- DATA STORAGE -----
applications = []
DATA_FILE = "application.json"

# ----- FUNCTIONS -----
def save_applications():
    with open(DATA_FILE, "w") as file: # This means open application.json, "w" = write mode
        json.dump(applications, file, indent = 4) # Converts python list applications, save it into the file as json, indent=4 = spacing

def load_applications():
    global applications # Replace the global applications list
    if os.path.exists(DATA_FILE): # Prevent errors if the file doesnt exist yet
        with open(DATA_FILE, "r") as file: # Open the file in read mode
            applications = json.load(file) 

# This function runs when the button is clicked
def add_application():
    # Get text typed by the user in each input box
    company = company_entry.get()
    program = program_entry.get()
    date = date_entry.get()

    # Store application as a dictionary
    app = {
        "company" : company,
        "program" : program,
        "date" : date,
        "status" : "Applied"
    }

    # Add to the list
    applications.append(app)

    # Update the Listbox display
    refresh_listbox()

    save_applications()

    # Clear input boxes after adding
    company_entry.delete(0, tk.END) # .delete deletes text from the entry widget, start at index 0 and tk.END means the last character
    program_entry.delete(0, tk.END)
    date_entry.delete(0,tk.END)

def refresh_listbox():
    # Clears and redraws the Listbox so it always shows the latest data

    # Remove all existing items from Listbox
    listbox.delete(0, tk.END)

    # Add each application to the Listbox
    for index, app in enumerate(applications):
        listbox.insert(
            tk.END,
            f"{index}. {app["company"]} - {app["program"]} | {app["date"]} | {app["status"]}"
        )

def get_selected_index():
    selection = listbox.curselection() # Ask the Listbox which row is selected, return a tuple of indices
    if not selection: # Check if the user select nothing
        messagebox.showwarning( # Show a popup warning
            "Selection Error",
            "Please select an application first!"
        )
        return None # Stop the function immediately
    return selection[0] # Because curselection returns a tuple, [0] means the option selected

def mark_interview():
    index = get_selected_index() # Get the index
    if index is None: 
        return
    applications[index]["status"] = "Interview" # Update the status
    save_applications()
    refresh_listbox()

def delete_application():
    index = get_selected_index()
    if index is None:
        return
    
    comfirm = messagebox.askyesno("Comfirm delete",
                                  "Do you want to delete this item?" ) # Ask user to comfirm deletion
    if not comfirm:
        return
    
    applications.pop(index) # Remove from list
    save_applications()
    refresh_listbox()

def update_status():
    index = get_selected_index()
    if index is None:
        return
    
    applications[index]["status"] = status_var.get() # Update the status
    save_applications()
    refresh_listbox()


    



# Create the main window
root = tk.Tk()

# Set the title shown at the top of the window
root.title("Application Tracker")

# Set the window width x height
root.geometry("1000x800")

# ----- WINDOW IMAGE -----
bg_image = Image.open("background.png") # Load image file
bg_image = bg_image.resize((1000,800))
bg_photo = ImageTk.PhotoImage(bg_image)
bg_label = tk.Label(root, image = bg_photo)
bg_label.place(x=0,y=0, # Top left corner of the window
                relwidth = 1, relheight = 1 # Stretch image to fill the entire window
)

# ------- LABELS --------

# Create a text label that says company
# root means the label is inside the window
tk.Label(root, text="Company").grid(
    row = 0, # Row position in the gird
    column = 0,
    padx = 10, # Horizontal spacing around the label
    pady = 5, # Vertical
)

# Program text label
tk.Label(root, text="Program").grid(
    row = 1,
    column = 0,
    padx = 10,
    pady = 5
)

# Date applied text label
tk.Label(root, text="Date Applied").grid(
    row = 2,
    column = 0,
    padx = 10,
    pady = 5
)

# ----- INPUT BOXES -----

# Create an input box for the company name
# Entry widgets allow user to type text
company_entry = tk.Entry(root)

# Place the input box below the label
company_entry.grid(
    row = 0, 
    column = 1
)

# Program name
program_entry = tk.Entry(root)

program_entry.grid(
    row = 1,
    column = 1
)

# Date Applied 
date_entry = tk.Entry(root)

date_entry.grid(
    row = 2,
    column = 1
)

# ----- LISTBOX -----
# This Listbox display all applications
listbox = tk.Listbox(root, width = 90)
listbox.grid(
    row = 4,
    column = 0,
    columnspan = 2,
    pady = 10,
    padx = 10
)

# ----- STATUS DROPDOWN -----
status_var = tk.StringVar() # Creates a special Tkinter variable that automatically updates GUI elements when it changes
status_var.set("Applied") # Set default status when the app starts

status_menu = tk.OptionMenu( # Create a dropdown menu
    root, # The main window
    status_var, # The var the manu will update
    "Applied", "Interview", "Offer", "Rejected" # Choices
)

status_menu.grid(
    row = 5,
    column = 0,
    columnspan = 2,
    pady = 5
)

# ----- BUTTON -----
add_button = tk.Button(
    root, 
    text="Add Application",
    command = add_application
)
add_button.grid(
    row = 3,
    column = 0,
    columnspan = 2, # This means the button stretch accross 2 columns
    pady = 10
)

update_button = tk.Button(
    root,
    text="Update Status",
    command = update_status
)
update_button.grid(
    row = 6,
    column = 0,
    columnspan = 1,
    pady = 5
)

delete_button = tk.Button(
    root,
    text="Delete",
    command = delete_application
)
delete_button.grid(
    row = 6,
    column = 1,
    columnspan = 1,
    pady = 5
)

# ----- START THE APP -----
load_applications()
refresh_listbox()
root.mainloop()