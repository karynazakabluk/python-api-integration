# import library (for API requests)
import requests       

# API URL (person in space)
url = "http://api.open-notify.org/astros.json"

# sender request to API
response = requests.get(url)

# converterer response to JSON 
data = response.json()

# print total number of people in space
print("Det er", data["number"], "mennesker i verdensrommet akkurat nå.\n")

# counter for numbering
i = 1

# for loop through all people
for person in data["people"]:
    
    # get name
    navn = person["name"]
    
    # get spacecraft
    fartoy = person["craft"]
    
    # print result
    print(f"{i}. {navn} - {fartoy}")
    
    # increase counter
    i = i + 1