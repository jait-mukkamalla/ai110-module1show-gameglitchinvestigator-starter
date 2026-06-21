# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.

   The game's objective is to guess the secret number as quickly as possible before running out of guesses. You select a difficulty to determine the number of guesses you are given and the range of numbers that will contain the secret number. You make positive integer guesses, and can use the hints to guide you if you wish. The game ends when you guess the secret number or run out of guess attempts.

- [ ] Detail which bugs you found.

   Here is a list of the bugs that I found:
   1. Incorrect starting value for number of used guesses
   2. Hint were always given in the wrong direction
   3. Negative score value(s)
   4. New game button did not work
   5. History did not reset when new game was pressed
   6. Incorrect/weird difficulty to guesses allowed pairings
   7. Incorrect/weird difficulty to number range pairings
   8. Secret number was not always within selected number range
   9. Secret number does not update when difficulty changed
   10. Guess button required two clicks for the guess to register in history
   11. Developer debug info was always one guess behind in showing real time data

- [ ] Explain what fixes you applied.

   Here are the fixes that correspond to the bugs above:
   1. Made number of guesses start at 0 in app.py
   2. Swapped the hint messages so they were correct
   3. Fixed a calculation/logic error causing negative score
   4. Fixed game state issue by setting state to 'playing' and made sure to reset the attributes correctly
   5. History fix was paired with the new game issue as I expected
   6. Changed key value pairs in the attempts_limit_map in app.py
   7. Changed difficulty to number range pairings inside get_range_for_difficulty function in logic_utils.py
   8. The randomly generated secret number is now given a lower and upper bound to ensure it is within range of selected difficulty
   9. Made the session state update its difficulty key every time the difficulty was changed to ensure proper boundary checks occurred
   10. Grouped up the guess and submit sections to ensure better response and proper history tracking
   11. Moved debug info to the bottom of the page so that it was accurate


## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

0. Pre-game: user selected game difficulty -> Hard
1. User enters a guess of 80
2. Game returns "Too High"
3. User enters a guess of 50
4. Game returns "Too Low"
5. User can keeping guessing until out of attempts
6. Score updates after every guess
7. Game ends after correct guess or no more attempts left
8. Click hint button to turn hints on/off
9. Use new game button to start a new game

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
tests\test_game_logic.py ...................                    [100%]

========================= 32 passed in 0.09s =========================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
