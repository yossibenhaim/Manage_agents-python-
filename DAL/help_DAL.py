def return_prompt_add_agent(codeName, realName, location, status, missionsCompleted):
    return (
    "INSERT "
    "INTO "
    "agents(codeName, realName, location, status, missionsCompleted) "
    f"VALUES({codeName}, {realName}, {location}, {status}, {missionsCompleted});"
    )
