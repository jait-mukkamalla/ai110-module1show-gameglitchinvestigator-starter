# FIX: Refactored from app.py; fixed the range/difficulty pairings using agent mode.
def get_range_for_difficulty(difficulty: str):
    """Return the inclusive numeric range for a given difficulty level.

    Args:
        difficulty: One of ``"Easy"``, ``"Normal"``, or ``"Hard"``.
            Any unrecognised value falls back to the Normal range.

    Returns:
        A tuple ``(low, high)`` of integers representing the inclusive
        bounds of the guessing range for the requested difficulty.

    Examples:
        >>> get_range_for_difficulty("Easy")
        (1, 20)
        >>> get_range_for_difficulty("Hard")
        (1, 100)
        >>> get_range_for_difficulty("unknown")  # fallback
        (1, 50)
    """
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 50
    if difficulty == "Hard":
        return 1, 100
    return 1, 50


# FIX: Refactored from app.py; improved parsing to handle empty input, decimals,
# and non-numeric strings more gracefully using agent mode.
def parse_guess(raw: str, low: int = 1, high: int = 100):
    """Parse and validate raw user input into an integer guess.

    Rejects empty strings, decimal numbers, non-numeric strings, and values
    outside the allowed range before returning a structured result so callers
    never need to inspect raw input themselves.

    Args:
        raw: The raw string submitted by the user (e.g. from a form field).
        low: The minimum valid guess, inclusive. Defaults to ``1``.
        high: The maximum valid guess, inclusive. Defaults to ``100``.

    Returns:
        A 3-tuple ``(ok, guess_int, error_message)`` where:

        - ``ok`` (``bool``) – ``True`` when the input is valid.
        - ``guess_int`` (``int | None``) – The parsed integer on success,
          ``None`` on failure.
        - ``error_message`` (``str | None``) – A human-readable error string
          on failure, ``None`` on success.

    Examples:
        >>> parse_guess("42", 1, 100)
        (True, 42, None)
        >>> parse_guess("", 1, 100)
        (False, None, 'Enter a guess.')
        >>> parse_guess("3.5", 1, 100)
        (False, None, 'Enter a whole number, not a decimal.')
        >>> parse_guess("abc", 1, 100)
        (False, None, 'That is not a number.')
        >>> parse_guess("200", 1, 100)
        (False, None, 'Enter a number between 1 and 100.')
    """
    if raw is None or raw.strip() == "":
        return False, None, "Enter a guess."

    raw = raw.strip()

    if "." in raw:
        return False, None, "Enter a whole number, not a decimal."

    try:
        value = int(raw)
    except ValueError:
        return False, None, "That is not a number."

    if value < low or value > high:
        return False, None, f"Enter a number between {low} and {high}."

    return True, value, None


# FIX: Refactored from app.py; corrected the swapped hint messages using agent mode.
def check_guess(guess, secret):
    """Compare a player's guess to the secret number and return a verdict.

    Supports both numeric and string representations of the secret value.
    When a direct numeric comparison raises ``TypeError`` (e.g. mixed types),
    the function falls back to string comparison so the caller is insulated
    from type mismatches in different storage backends.

    Args:
        guess: The player's guess. Typically an ``int``, but any comparable
            type is accepted.
        secret: The target value the player is trying to match. Typically an
            ``int`` or a numeric string.

    Returns:
        A 2-tuple ``(outcome, message)`` where:

        - ``outcome`` (``str``) – One of ``"Win"``, ``"Too High"``, or
          ``"Too Low"``.
        - ``message`` (``str``) – A short, emoji-prefixed hint to display to
          the player.

    Examples:
        >>> check_guess(42, 42)
        ('Win', '🎉 Correct!')
        >>> check_guess(80, 42)
        ('Too High', '📉 Go LOWER!')
        >>> check_guess(10, 42)
        ('Too Low', '📈 Go HIGHER!')
    """
    if guess == secret:
        return "Win", "🎉 Correct!"

    try:
        if guess > secret:
            return "Too High", "📉 Go LOWER!"
        else:
            return "Too Low", "📈 Go HIGHER!"
    except TypeError:
        g = str(guess)
        if g == secret:
            return "Win", "🎉 Correct!"
        if g > secret:
            return "Too High", "📉 Go LOWER!"
        return "Too Low", "📈 Go HIGHER!"


# FIX: Refactored from app.py; fixed scoring issues using agent mode.
def update_score(current_score: int, outcome: str, attempt_number: int):
    """Calculate the new score after a guess attempt.

    On a win, awards ``100 - 10 * attempt_number`` points with a floor of
    ``10`` so even late wins are always rewarded. Incorrect guesses (too high
    or too low) each deduct 5 points. Unknown outcomes leave the score
    unchanged.

    Args:
        current_score: The player's score before this attempt.
        outcome: The verdict string returned by :func:`check_guess` —
            one of ``"Win"``, ``"Too High"``, or ``"Too Low"``.
        attempt_number: The 1-based index of the current attempt. A value of
            ``1`` on the first guess yields the maximum win bonus of 90 points.

    Returns:
        The updated score as an ``int``.

    Examples:
        >>> update_score(0, "Win", 1)
        90
        >>> update_score(90, "Too High", 2)
        85
        >>> update_score(85, "Win", 10)
        95
    """
    if outcome == "Win":
        points = 100 - 10 * attempt_number
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score
