from DAL import DAL,help_DAL
import help_manager
from agent import Agent

def add_agent():
    prompt = help_DAL.return_prompt_add_agent()
    value = create_new_agent()
    DAL.send_query(prompt,value)
    print("agent added")
    return True

def show_agent():
    query = help_DAL.return_prompt_select_all()
    DAL.get_query(query)
    print("agent")
    return True

def update_agent():
    print("the agent is update")
    return True

def remove_agent():
    print("the agent is delete")
    return True

def logout():
    print("you is out")
    return False

def create_new_agent():
    code_name = help_manager.create_code_name()
    real_name = help_manager.create_real_name()
    location = help_manager.create_location()
    status = help_manager.create_status()
    missions_completed = help_manager.create_missions_completed()
    new_agent = Agent(code_name,real_name,location,status,missions_completed)
    return new_agent