def return_prompt_add_agent():
    return (
    "INSERT "
    "INTO "
    "agents (codeName, realName, location, status, missionsCompleted) "
    f"VALUES(%s, %s, %s, %s, %s);"
    )
def return_prompt_select_all():
    return "SELECT * FROM agents;"