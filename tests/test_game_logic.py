#FIX: Made logic_utils.py available for import so its contents can be used for tests
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from logic_utils import check_guess, update_score

# --- Bug fix: hint messages were swapped ---

def test_too_high_message_says_go_lower():
    # When guess exceeds secret, the hint must direct the player downward
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message, f"Expected 'LOWER' in hint for too-high guess, got: {message}"

def test_too_low_message_says_go_higher():
    # When guess is below secret, the hint must direct the player upward
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message, f"Expected 'HIGHER' in hint for too-low guess, got: {message}"

# --- Bug fix: secret was cast to str on even attempts, causing lexicographic comparison ---

def test_numeric_comparison_not_lexicographic():
    # "9" > "10" lexicographically but 9 < 10 numerically.
    # check_guess must use numeric ordering so guess=9, secret=10 → Too Low (not Too High).
    outcome, _ = check_guess(9, 10)
    assert outcome == "Too Low", f"Expected 'Too Low' for 9 vs 10, got: {outcome}"

def test_integer_secret_wins_correctly():
    # Ensuring an exact int match is still recognised as a win (guards against type coercion regression)
    outcome, _ = check_guess(42, 42)
    assert outcome == "Win"

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"

# --- Bug fix: attempts should start at 0, so first real guess is attempt_number=1 ---

def test_first_attempt_win_scores_correctly():
    # attempt_number=1 means 100 - 10*1 = 90 bonus; old bug used +1 giving only 80
    score = update_score(100, "Win", 1)
    assert score == 190, f"Expected 190 (100 + 90), got: {score}"

# --- Bug fix: score should start at 100 so deductions make sense ---

def test_wrong_guess_deducts_from_starting_score():
    # Starting score of 100, one wrong guess → 95
    score = update_score(100, "Too Low", 1)
    assert score == 95, f"Expected 95 after first wrong guess, got: {score}"

def test_too_high_deducts_from_starting_score():
    # Starting score of 100, a Too High guess → 95
    score = update_score(100, "Too High", 1)
    assert score == 95, f"Expected 95 after first Too High guess, got: {score}"

# --- Bug fix: update_score logic errors ---

def test_too_high_always_deducts_on_even_attempt():
    # Even-numbered attempts used to add 5 points — should always subtract
    score = update_score(100, "Too High", 2)
    assert score == 95, f"Expected 95 for even attempt Too High, got: {score}"

def test_too_high_always_deducts_on_odd_attempt():
    score = update_score(100, "Too High", 3)
    assert score == 95, f"Expected 95 for odd attempt Too High, got: {score}"

def test_win_formula_no_off_by_one():
    # Win on attempt 5: 100 - 10*5 = 50 bonus; old bug gave 100 - 10*6 = 40
    score = update_score(0, "Win", 5)
    assert score == 50, f"Expected 50, got: {score}"

def test_win_minimum_points():
    # Very late win should give at least 10 points, never go negative bonus
    score = update_score(0, "Win", 15)
    assert score == 10, f"Expected minimum 10 bonus points, got: {score}"
