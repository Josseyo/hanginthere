![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

**April 2024**

# Hang in there...
Hang in there is a traditional Hangman and Python terminal game which runs in Code Institute mock terminal on Heroku

## How to play

Play against the computer. A random word is generated and hidden. See if you can guess the hidden word before you run out of guesses and get hung...

* Enter a letter...
* Wrong guess...
* Correct 

## Features
### Existing Feautures

* Random word generator
* Play against computer
* Accept user input
* Maintains guessed letters
* Maintains correct and wrong guesses
* Input validation
    * You must enter a letter
    * You can not enter same letter twice

### Future Feautures
* Allow player to select theme of words
* Allow player to select shorter / longer words

## Data Model...

## Testing
**Manually tested:**
* Code validated through PEP8 linter without issues
* Tested in my gitpod terminal
* Tested in my (Code Institute) Heroku terminal

**Validator Testing:**
* PEP8

### Bugs
**Solved bugs**
* Upper case...

**Remaining bugs**

## Deployment
The steps for deployment

* Create a new Heroku app
* Add two buildpacks from the _Settings_ tab. The ordering is as follows:
1. `heroku/python`Creating the Heroku app
2. `heroku/nodejs`
(You must then create a _Config Var_ called `PORT`. Set this to `8000`)
* Link the Heroku app to my Github repository
* Click on **Deploy**

## Credit
* Tokyo Ed-tech https://youtu.be/z9YGr0eRfeQ?si=6iU2-78ies0um_DI
* Adding categories to word bank https://youtu.be/fqstJoazHCQ?si=T1ebkd0VLmCChvoA

-----
Happy gaming!