from DAL import DAL,help_DAL

def add_agent():
    prompt = help_DAL.return_prompt_add_agent("1","1","1","1","1")
    DAL.send_query(prompt)
    print("agent added")
    return True

def show_agent():
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