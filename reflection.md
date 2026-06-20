# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?

  The first time I ran the game, I immediately noticed that the number of attempts was at 1 instead of 0. I also noticed that the number of allowed guesses and range of possible numbers for the varying difficulties did not align properly. Once I started guessing numbers, I noticed that a lot of things (such as the guess counter and score) were not behaving in the intended manner. As for the UI and features, it was quite similar to the tinker lab in terms of appearance.

- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
  
  I noticed at 8 bugs while looking through and testing the game:
  1. The number of user guess attempts started at 1 instead of zero, and it was also not updating at more guesses were made.
  2. The hints given were in the wrong direction every time.
  3. The score attribute for each game played did not really make any sense.
  4. The new game button was not working, and this prevented guesses from being made for another game.
  5. The history transferred from game to game, possibly as a result of the aforementioned error (#4)
  6. The number of guesses allowed in a game of ___ difficulty did not align with name of the difficulty. (ie. normal difficulty got 8 guesses but easy only got 6 guesses)
  7. Same as error #7, but this time with the range of possible numbers that can be guessed. (ie. normal mode had a smaller range of numbers compared to hard difficulty, but it should be the other way around)
  8. Problem with the secret number not being within the number range of the selected difficulty. Secret doesn't update when mode changes.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

|   Input   | Expected Behavior |  Actual Behavior  | Console Output / Error |
|-----------|-------------------|-------------------|------------------------|
| None      | Attempts = 0      | Attempts = 1      | N/A                    |
| 60        | Hint: too high    | Hint: too low     | N/A                    |
| 89        | Score: (pos. num) | Score: -10        | N/A                    |
| New game  | Start new game    | Nothing happened  | When attempting a guess: says game already won, start new game|
| New game  | History is empty  | Old history stays | N/A                    |
| Easy mode | 8 guesses allowed | 6 guesses allowed | N/A                    |
| Hard mode | Num range 0-100   | Num range 1-50    | N/A                    |
| 32        | Secret num is 32  | Secret num is 86  | N/A                    |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?

  I used Claude Code as an integrated AI tool in VS Code to help debug, fix, test, and document code during this project.

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

  Claude suggested to make the functions within logic_utils.py available for import in the pytest test cases file by inserting the file path. I was unsure if this would work, but ran the current test cases in the file at time and found that the fix worked and all the test cases were passing.

  Another useful fix that Claude suggested was to reset the history, score, etc. and set the game state to playing when starting a new games so that the new game feature would actually work. This was a result of me asking Claude to figure out why the new game button was not working. I play tested the game multiple times to ensure the button was functional.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

  When I first tried to find a fix to allow for the refactored functions to be imported into the test cases file, Claude suggested adding two new files to the project root: conftest.py and pytest.ini. I was unsure if this would work and did not want to create any new files, so I re-prompted Claude to find a different solution. I ended up with the solution I mentioned in the previous question.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?

  If it was a bug inside of one of the refactored functions inside of logic_utils.py, I designed test cases for core logic and edge cases for each function with the assistance of Claude. I then inspected each test case to ensure it was written correctly and ran the tests in the terminal to make sure everything worked as intended.
  If it was a bug in app.py, I had to run the game in order to check the correctness of the fixes. I always played at least 5 games to ensure that the new code was working in various scenarios. I did work with Claude to see if these tests could also be automated, but that ended up being a little complex and was not very useful in the end.

- Describe at least one test you ran (manual or using pytest) and what it showed you about your code.

  The first two test cases that were ran using pytest were to check that the hint messages were fixed. One test cases made sure that a low guess was paired with a "HIGHER" hint message, and the other test case made sure that a high guess was paired with a "LOWER" hint message. This same test was then manually done by running the game and playing after it had passed the pytest test cases.

- Did AI help you design or understand any tests? How?

  AI helped me design a lot of the test cases after I had given it some info about what logic and edge cases to check. It was very useful to just state my thoughts to the AI and allow it to make the test cases for me. It helped me save a lot of time. This process also helped me spot more functional logic and edge cases to test due to the descriptive names of each test case.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
