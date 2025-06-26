import printer
import magager

def menu():

    printer.show_menu()
    run = True

    while run:
        choice = input("enter a number \n")
        actions = {
            "1": magager.add_agent,
            "2": magager.show_agent,
            "3": magager.update_agent,
            "4": magager.remove_agent,
            "5": magager.logout
        }
        run = actions.get(choice)()

