def create_code_name():
    return input("Enter agent code name: ")

def create_real_name():
    return input("Enter agent real name: ")

def create_location():
    return input("Enter agent current location: ")

def create_status():
    statuses = ["Active", "Injured", "Missing", "Retired"]
    while True:
        status = input(f"Enter agent status ({', '.join(statuses)}): ")
        if status in statuses:
            return status
        print("Invalid status. Please enter one of the allowed values.")

def create_missions_completed():
    while True:
        try:
            missions = int(input("Enter number of missions completed: "))
            if missions >= 0:
                return missions
            else:
                print("Number must be zero or positive.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")