Number Guessing Game (Java)

A simple console-based game where the computer picks a random number
between 1 and 100, and the player has to guess it. After each guess, the
program tells you whether your guess was too high, too low, or correct, and
finally reports how many attempts it took.

How It Works


The program generates a random number between 1 and 100 (inclusive).
You repeatedly enter guesses.
After each guess, you're told:

"Too low! Try again." — if your guess is smaller than the number.
"Too high! Try again." — if your guess is larger than the number.
"Congratulations! ..." — if you guessed correctly, along with the
total number of attempts it took.



The game ends automatically once you guess the correct number.


Requirements


Java Development Kit (JDK) 8 or later installed.


Compilation

bashjavac NumberGuessingGame.java

Running

bashjava NumberGuessingGame

Sample Output

Welcome to the Number Guessing Game!
Guess the number between 1 and 100:
Enter your guess: 50
Too high! Try again.
Enter your guess: 25
Too low! Try again.
Enter your guess: 37
Too high! Try again.
Enter your guess: 31
Congratulations! You guessed the number in 4 attempts.

Known Limitations


No input validation. If you type something that isn't an integer
(e.g. letters or symbols), sc.nextInt() will throw an
InputMismatchException and crash the program. Wrapping the read in a
try/catch, or checking sc.hasNextInt() first, would make it more robust.
No range validation. Entering a number outside 1-100 (e.g. -5 or
500) is accepted and simply evaluated as too low/too high - the program
doesn't warn you that it's out of the valid range.
Single game per run. Once you guess correctly, the program ends. There's
no option to play again without restarting the program manually.
No guess limit or difficulty levels. The game doesn't cap the number of
attempts or offer easy/medium/hard ranges.


Possible Improvements


Add input validation to handle non-integer input gracefully.
Add a "Play again?" loop so multiple rounds can be played in one run.
Track and display the best score (fewest attempts) across games.
Add difficulty levels (e.g. smaller/larger number ranges, limited attempts).
Give hints like "you're getting warmer" based on how close the guess is.


License

Feel free to use, modify, and share this program for learning purposes.
