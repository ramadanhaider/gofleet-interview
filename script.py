#define keywords 
High_priority = {'Urgent','Critical','Immediate'}

TEAMS = {
    "High": {
        "agents": ["SeniorAgent1", "SeniorAgent2", "SeniorAgent3"],
        "last_index": -1,
    },
    "Low":{"agents": ["GeneralAgent1", "GeneralAgent2", "GeneralAgent3"],
        "last_index": -1,
        }
}

def determine_priority(request):
    #user specified priority
    if "priority" in request and request["priority"] in TEAMS:
        return request["priority"]
    
    content = f"{request.get('subject', '')} {request.get('body', '')}".lower()
    for keyword in High_priority:
        if keyword in content:
            return "high"
    else:
        return "low"
    

def assign_priority(priority):
    team = TEAMS(priority)
    team["last_index"] = (team["last_index"] + 1) % len(team["agents"])
    return team["agents"][team["last_index"]]


priority = determine_priority(request=False)
agent = assign_priority(priority=False)
        
print(f"Request Priority:{priority}, Assigned to:{agent}")

