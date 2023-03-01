# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("football_team_predictions")


def get_team_results():
    """
    User inputs team results from latest game
    """
    print("Enter the total yardages from the teams latest game")
    print("The input should consist of 11 numbers, seperated by a comma")
    print("Here is an example of a syntax input: 1,2,3,4,5,6,7,8,9,10,11\n")

    user_str = input("Enter here: \n")

    results_data = user_str.split(",")
    validate_input(results_data)


def validate_input(inputs):
    try:
        for num in inputs:
            int(num)
            if len(inputs) != 11:
                raise ValueError(
                    f"Expected 11 values, but received {len(inputs)}"
                )
    except ValueError as e:
        print(f"Invalid input: {e}, please enter all numbers\n")
        return False
    return True


get_team_results()
