def vacuum_agent(location,status):
    if status == "Dirty":
        return "Clean"
    elif location == "A":
        return "Move Right"
    else:
        return "Move Left"


location = input("Enter A/B:").upper()
status = input("Enter status (Dirty/Clean):").capitalize()

action = vacuum_agent(location,status)

print("Location:",location)
print("Status:",status)
print("Action:",action)
