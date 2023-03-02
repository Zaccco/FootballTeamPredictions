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
        print("The input should consist of 11 numbers, seperated by a comma\n")

        user_str = input("Enter the game numbers here:\n")

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


def apply_team_results(results, sheet):
    """
    Inputs the user input into the google sheet that we expect,
    for example team1results, team2results and so on...
    """
    update_sheet = SHEET.worksheet(sheet)
    update_sheet.append_row(results)
    print(f"{sheet} updated successfully!")


def make_predicitons_for_last_three_games(num):
    """
    Takes the average number from the last three games in each category
    """
    prediction_page = SHEET.worksheet("team1results").get_all_values()
    last_three_rows = prediction_page[-3:]
    prediction_list = []

    i = 0
    while i <= 2:
        prediction_list.append(int(last_three_rows[i][num]))
        i += 1
    average = sum(prediction_list) / 3
    average_last_three = int(average)
    return average_last_three


def make_predicitons_for_last_five_games(num):
    """
    Takes the average number from the last five games in each category
    """
    prediction_page = SHEET.worksheet("team1results").get_all_values()
    last_five_rows = prediction_page[-5:]
    prediction_list = []

    i = 0
    while i <= 4:
        prediction_list.append(int(last_five_rows[i][num]))
        i += 1
    average = sum(prediction_list) / 5
    average_last_five = int(average)
    return average_last_five


def make_predicitons_for_all_season(num):
    """
    Takes the average number from all season, or all the numbers inputed
    by the user to the spreadsheet in each category
    """
    prediction_page = SHEET.worksheet("team1results").get_all_values()
    all_season = prediction_page[1:]
    prediction_list = []

    for i in range(len(all_season)):
        prediction_list.append(int(all_season[i][num]))

    average = sum(prediction_list) / len(all_season)
    average_all_season = int(average)
    return average_all_season


def calculating_average(index):
    """
    Calculates the average number out of the 3 prior functions to get a
    predicted number in each category for the upcoming game, taking into
    consideration both short term and long term form.
    """
    average_last_three = make_predicitons_for_last_three_games(index)
    average_last_five = make_predicitons_for_last_five_games(index)
    average_all_season = make_predicitons_for_all_season(index)

    total_average = (average_last_three + average_last_five + average_all_season)/3
    return int(total_average)


def create_final_predictions_list():
    """
    Creates a list out of the calculating average function so that it is
    appendable to the spreadsheet.
    """
    final_list = []
    for i in range(11):
        final_list.append(calculating_average(i))
    return final_list


def main():
    """
    Function that runs all other functions
    """
    data = get_team_results()
    # Turns user data from a string to an integer
    team_results = [int(num) for num in data]
    apply_team_results(team_results, "team1results")
    print("Updating predictions page for next game...")
    apply_team_results(create_final_predictions_list(), "team1prediction")


main()
