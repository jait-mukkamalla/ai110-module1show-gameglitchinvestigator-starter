#FIX: Made logic_utils.py available for import so its contents can be used for tests
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from logic_utils import check_guess

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
