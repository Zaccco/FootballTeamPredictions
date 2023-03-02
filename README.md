# American Football Predictions

This american football predictor takes in results from different playing positions for a set team during the season and then tries to predict numbers on upcoming games. The program is run through Python and uses Google Sheets as the basis for storing the numbers.

Users can input yardage results from any team they choose and after more and more inputs, users can see more accurately get estimates on how well/poorly the team will succeed in future games. 

[Here you can find the link to view my project](https://football-predictions.herokuapp.com/)

## Flow Chart

### User input section

* When the program runs, the user will have to input game numbers from the latest game.
* This input will then be checked to see if it's valid (11 numbers, seperated by comma, CSV).
* If the input is valid, the input will be sent to the results page on Google Sheets and appended on a new row.

### Predictions section

* After the user has made an input. The program will run predictions on the next game.
* It will take in the values for every category in the sheet based on three different criterias.
* These criterias are:
    * The 3 latest games
    * The 5 latest games
    * All season, so however many games has been played so far.
* The program will take these three criteras and make an average out of all three of them (producing 3 numbers) and then take the average out of those three numbers.
* The reason for this is to both get an impact in the prediction with the team's recent form (latest 3 and 5 games) but also results for the entire season.
* These predicted numbers will finally be imported into the predictions sheet.

## Future features

* One feature I would like to add in the future would be to have multiple teams run through this program and the sheet. With that information you could even more accurately predict matchups and results by comparing the two teams that are playing.
* Another feature would be to further design the spreadsheet so that for example you could see how many games have been played, not just by counting the rows, but have it be displayed and appended to the sheet when a user makes a new input.

## Testing

I have manually tested this project by doing the following:
* Passed the code through a PEP8 linter and confirmed there are no problems, except for one line being too long.
    * I tried to fix this by either doing a "\" but that didn't work within the (). And when I tried to do it before the () it gave me a syntax error. 
    * My mentor also said that it was okay to leave it like that for this project.
* Given invalid inputs: strings instead of numbers and out of bounds inputs.
* Tested in my local terminal and the Code Institute Heroku terminal.

## Bugs

### Solved Bugs

* I had a bug where during a for loop inside a function, and to test the function I used a print statement. However I accidently put the print statement inside the for loop meaning that it printed on every instance. 
    * But then by moving it outside the loop, it only printed once.
* The biggest bug I had was I accidently put some numbers way below the other ones in my spreadsheet. And so when I tried to access the "real" numbers, I received a "ValueError, Invalid literal for int with base 10" because the cells around my "accidental" numbers where empty and the program tried to access the wrong ones.
    * The bug was solved as soon as I removed my accidental numbers.

### Remaining Bugs

* Sometimes I would experience that the program would "crash" before inporting the prediction numbers. However I could not figure out why this happened, and by rerunning the program the program would normally run as expected.

## Deployment

This project was deployed using Code Institute's mock terminal for Heroku.

* Steps for deployment:
    * Fork or clone this repository
    * Create a new Heroku app
    * Set the buildpacks to Python and NodeJS in that order
    * Link the Heroku app to the repository
    * Click on deploy

## Credits

A lot of inspiration for this project was taken from the Code Institute example project called "Love Sandwiches".