#FIX: Made logic_utils.py available for import so its contents can be used for tests
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from logic_utils import check_guess, update_score, get_range_for_difficulty, parse_guess

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

# --- Refactor: get_range_for_difficulty moved to logic_utils with corrected ranges ---

def test_easy_range():
    assert get_range_for_difficulty("Easy") == (1, 20)

def test_normal_range():
    assert get_range_for_difficulty("Normal") == (1, 50)

def test_hard_range():
    assert get_range_for_difficulty("Hard") == (1, 100)

def test_hard_range_larger_than_normal():
    _, hard_high = get_range_for_difficulty("Hard")
    _, normal_high = get_range_for_difficulty("Normal")
    assert hard_high > normal_high

def test_unknown_difficulty_defaults():
    assert get_range_for_difficulty("Unknown") == (1, 50)

# --- Refactor: parse_guess moved to logic_utils with improved input handling ---

def test_parse_valid_integer():
    ok, value, err = parse_guess("42")
    assert ok is True and value == 42 and err is None

def test_parse_strips_whitespace():
    ok, value, _ = parse_guess("  7  ")
    assert ok is True and value == 7

def test_parse_empty_string():
    ok, _, err = parse_guess("")
    assert ok is False and "guess" in err.lower()

def test_parse_none():
    ok, _, err = parse_guess(None)
    assert ok is False and err is not None

def test_parse_whitespace_only():
    ok, _, _ = parse_guess("   ")
    assert ok is False

def test_parse_decimal_is_rejected():
    ok, _, err = parse_guess("3.9")
    assert ok is False and "decimal" in err.lower(), f"Expected decimal error, got: {err}"

def test_parse_non_numeric_string():
    ok, _, err = parse_guess("abc")
    assert ok is False and err == "That is not a number."

# EDGE CASES BELOW WRITTEN FOR CHALLENGE #1

def test_parse_letters_then_numbers_is_rejected():
    ok, _, err = parse_guess("abc12")
    assert ok is False and err == "That is not a number."

def test_parse_numbers_then_letters_is_rejected():
    ok, _, err = parse_guess("12abc")
    assert ok is False and err == "That is not a number."

def test_parse_negative_number_is_rejected():
    ok, _, err = parse_guess("-5")
    assert ok is False and err is not None

def test_parse_zero_is_rejected():
    ok, _, err = parse_guess("0")
    assert ok is False and err is not None

def test_parse_just_over_max_is_rejected():
    ok, _, err = parse_guess("101")
    assert ok is False and err is not None

def test_parse_very_large_number_is_rejected():
    ok, _, err = parse_guess("999999999999")
    assert ok is False and err is not None
