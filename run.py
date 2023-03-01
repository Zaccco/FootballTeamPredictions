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
    while True:
        print("Enter the total yardages from the teams latest game")
        print("The input should consist of 11 numbers, seperated by a comma")
        print("Here's an example of a syntax input: 1,2,3,4,5,6,7,8,9,10,11\n")

        user_str = input("Enter here: \n")

        results_data = user_str.split(",")

        if validate_input(results_data):
            break
    return results_data


def validate_input(inputs):
    """
    Make sure that user input is valid and how we expect it
    """
    try:
        for num in inputs:
            int(num)
            # If user has not made 11 number inputs, raise a ValueError
            if len(inputs) != 11:
                raise ValueError(
                    f"Expected 11 values, but received {len(inputs)}"
                )
    except ValueError as e:
        print(f"Invalid input: {e}, please enter only 11 numbers\n")
        return False
    return True


def apply_team_results(data, sheet):
    """
    Inputs the user input into the google sheet that we expect
    """
    update_sheet = SHEET.worksheet(sheet)
    update_sheet.append_row(data)


data = get_team_results()
# Turns user data from a string to an integer
team_results = [int(num) for num in data]