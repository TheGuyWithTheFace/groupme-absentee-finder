#!/bin/python3
import urllib.request
import json

GROUPME_API = "https://api.groupme.com/v3"

def main():
    # gather required background information
    user_token = input("Please enter your API Token: ")
    group = select_group(user_token)
    group_id = group["group_id"]

# lists user's groups, asks for user to select a specific group, returns it.
def select_group(user_token):
    # Get list of groups
    groups = make_request(GROUPME_API, "/groups", user_token)
    names = [group["name"] for group in groups]

    # print groups for user to select
    for i in range(len(names)):
        print("[" + str(i) + "] " + names[i])
    selected_index = int(input("Please enter the number of your selected group: "))

    # return selected group
    return groups[selected_index]

# fetches resource at URL, converts JSON response to useful Object
def make_request(base_url, additional_url, token):

    # Hit url, get raw response
    url = base_url + additional_url + "?token=" + token
    response = urllib.request.urlopen(url)

    # Convert raw response to usable JSON object
    response_as_string = response.readall().decode('utf-8')
    obj = json.loads(response_as_string)
    return obj["response"]

# only true if the program was called via the command line.
if __name__ == "__main__":
    main()
