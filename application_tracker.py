# An app to track all your applications

applications = []
while True:
    # The main menu
    print("=======Main Menu=======")
    print("1. Add Application")
    print("2. View All Applications")
    print("3. Update Status")
    print("4. Delete Application")
    print("5. Exit")
    choice = input("Choose an option (1-5): ")

    if choice == "1":
            # Input details
        company = input("Company Name: ")
        program = input("Program: ")
        date = input("Date applied: ")
        status = "Applied"
        
        # Group them together
        app = [company, program, date, status]
        applications.append(app)

        print("Job added!")
        print(applications)

    elif choice == "2":
        # Check if empty
        if len(applications) == 0:
            print("No applications saved yet!")
        # Loop through the list
        else:
            for i, app in enumerate(applications):
                print(f"{i}. {app[0]} - {app[1]} - Applied on: {app[2]} | Status: {app[3]}")

    elif choice == "3":
        for i, app in enumerate(applications):
                print(f"{i}. {app[0]} - {app[1]} - Applied on: {app[2]} | Status: {app[3]}")
        app_index = int(input("Enter the index number to update: "))
        # Safety check
        if 0 <= app_index < len(applications):
            new_status = input("Enter new status: ")
            # Update new status
            applications[app_index][3] = new_status
            print("Status updated!")
            for i, app in enumerate(applications):
                    print(f"{i}. {app[0]} - {app[1]} - Applied on: {app[2]} | Status: {app[3]}")
        else: 
             print("Error: That number does not exist.")

    elif choice == "4":       
        for i, app in enumerate(applications):
            print(f"{i}. {app[0]} - {app[1]} - Applied on: {app[2]} | Status: {app[3]}")
        app_index = int(input("Enter the index number to delete: "))
        # Safety check
        if 0 <= app_index < len(applications):
            # Remove the application
            removed_app = applications.pop(app_index)
            print(f"Successfully deleted: {removed_app[0]}")
        else:
             print("Error: That number does not exist.")


    elif choice == "5":
        # Exit the loop
        print("Goodbye!")
        break


    
    

   




    