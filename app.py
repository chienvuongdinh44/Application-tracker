import tkinter as tk
# ----- DATA STORAGE -----
applications = []

# Create the main window
root = tk.Tk()

# Set the title shown at the top of the window
root.title("Application Tracker")

# Set the window width x height
root.geometry("600x400")

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

# ----- FUNCTIONS -----
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
            f"{index}. {app["company"]} - {app["program"]} | {app["status"]}"
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




# ----- START THE APP -----
root.mainloop()