temps = []

while True:
    value = input("Enter temperature ('done' to stop): ")

    if value == "done":
        break

    temps.append(float(value))

# Calculate temperature summary
def summarize(temps):
    result = {
        "minimum": min(temps),
        "maximum": max(temps),
        "average": sum(temps) / len(temps)
    }

    return result


print(summarize(temps))