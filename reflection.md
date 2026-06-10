# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?

  The first time I ran the game, I immediately noticed that the number of attempts was at 1 instead of 0. I also noticed that the number of allowed guesses and range of possible numbers for the varying difficulties did not align properly. Once I started guessing numbers, I noticed that a lot of things (such as the guess counter and score) were not behaving in the intended manner. As for the UI and features, it was quite similar to the tinker lab in terms of appearance.

- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
  
  I noticed at least 7 bugs while looking through and testing the game:
  1. The number of user guess attempts started at 1 instead of zero, and it was also not updating at more guesses were made.
  2. The hints given were in the wrong direction every time.
  3. The score attribute for each game played did not really make any sense.
  4. The new game button was not working, and this prevented guesses from being made for another game.
  5. The history transferred from game to game, possibly as a result of the aforementioned error (#6)
  6. The number of guesses allowed in a game of ___ difficulty did not align with name of the difficulty. (ie. normal difficulty got 8 guesses but easy only got 6 guesses)
  7. Same as error #7, but this time with the range of possible numbers that can be guessed. (ie. normal mode had a smaller range of numbers compared to hard difficulty, but it should be the other way around)

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| | | | |
| | | | |
| | | | |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
