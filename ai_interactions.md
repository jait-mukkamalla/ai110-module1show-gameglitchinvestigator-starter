# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Test Generation (SF7)

> Document how you used AI to help generate or improve tests.

> I am reformatting this section to make it more readable and easier to answer
1.  Edge case: invalid alphanumeric input(s)

- Prompt used: 
    Can you generate two test cases in @tests/test_game_logic.py  at the bottom of the file to ensure that       alphanumeric input (letters then numbers for one, numbers then letters for the other) is deemed invalid by parse_guess

- AI-suggested tests:
    def test_parse_letters_then_numbers_is_rejected():
        ok, _, err = parse_guess("abc12")
        assert ok is False and err == "That is not a number."

    def test_parse_numbers_then_letters_is_rejected():
        ok, _, err = parse_guess("12abc")
        assert ok is False and err == "That is not a number."

- Did it pass: Yes

-   Reasoning: 
    The only valid input for a guess should be an integer, but a user might enter both numbers and letters resulting in an invlaid input.


2.  Edge case: invalid negative and 0 inputs

- Prompt used: 
    Can you generate two test cases to test negtaive and 0 input respectively to make sure they are deemed invalid. Put them at the bottom of @tests/test_game_logic.py

- AI-suggested tests:
    def test_parse_negative_number_is_rejected():
        ok, _, err = parse_guess("-5")
        assert ok is False and err is not None

    def test_parse_zero_is_rejected():
        ok, _, err = parse_guess("0")
        assert ok is False and err is not None

- Did it pass: Yes

-   Reasoning:
    Non-positive input will never be included within the 3 varying difficulty to number range pairings, so I should write tests to ensure that my code will re-prompt the user for input if negative numbers or 0 are entered.


3.  Edge case: invalid large integer input(s)

- Prompt used: 
    Can you generate two test cases to deal with overly large input (101 and a really big integer) and add them at the bottom of the test cases file

- AI-suggested tests:
    def test_parse_just_over_max_is_rejected():
        ok, _, err = parse_guess("101")
        assert ok is False and err is not None

    def test_parse_very_large_number_is_rejected():
        ok, _, err = parse_guess("999999999999")
        assert ok is False and err is not None

- Did it pass: Yes

-   Reasoning:
    Overly large positive integer guesses are outside of the valid number ranges, so I should ensure they are identified as invalid input and that the user it prompted to enter a different guess.

---

## Linting & Style (SF9)

> Document your use of AI for linting or code style improvements.

**Prompt used:**

```
<!-- Paste the prompt you gave the AI -->
```

**Linting output before:**

```
<!-- Paste relevant linter warnings/errors -->
```

**Changes applied:**

<!-- Describe what you changed based on the AI's suggestions -->

