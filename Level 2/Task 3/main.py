"""
Created by: Shingai Dzinotyiweyi
Write a Python script that interacts with an external API to fetch and display data
(e.g., weather, cryptocurrency prices).

Task 3: API Integration
✅ - Use the requests library to make GET requests to an API.
✅ - Parse and display the fetched data in a user-friendly format.
✅ - Handle errors, such as failed requests or invalid responses.
"""
import requests

user_input = input("Enter a GitHub username: ")

def search_user(username):
    """
    Searches the username on GitHub and prints the results about the user
    """
    url = f"https://api.github.com/users/{username}"

    try:
        response = requests.get(url)


        if response.status_code == 200:
            result = response.json()
            print(f"{response.status_code}: User Found!\n"
                  f"\n---------------------------------\n")

            print(f"Username: {result['login']}\n"
                  f"Name: {result['name']}\n"
                  f"Followers: {result['followers']}\n"
                  f"Following: {result['following']}\n"
                  f"GitHub Profile: {result['html_url']}\n"
                  f"\n---------------------------------\n",)

        else:
            print(f"{response.status_code}: User not found...\n"
                  f"\n---------------------------------\n")
    except Exception as error:
        print("An error occurred:", error)


search_user(user_input)