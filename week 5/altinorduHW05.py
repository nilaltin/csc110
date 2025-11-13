"""
Rock, Paper, Scissors — single round 

Author: Nil
Course: CSC110
Date: November 7, 2025 

Description:
    A single-round Rock-Paper-Scissors game where the user plays against the computer.
    The program:
      1) Introduces the rules.
      2) Prompts the user to enter r/p/s (any case) OR 0/1/2 (0=Rock, 1=Paper, 2=Scissors).
      3) Validates input once (no re-prompts, no loops).
      4) Randomly generates the computer's choice.
      5) Prints both choices and announces the winner or a draw.

Rules implemented:
    - Rock vs Scissors: Rock wins
    - Scissors vs Paper: Scissors win
    - Paper vs Rock: Paper wins

Notes/Constraints:
    - Uses ONLY topics from chapters 1, 2, 3, and 5:
      * functions, selection (if/elif/else), simple I/O, and random numbers
    - NO repetition (no loops), NO data structures (no lists/dicts/sets/tuples in logic).
    - Program ends naturally when main() returns (no sys.exit()).

Testing ideas (documented here because randomness makes fixed test cases awkward):
    - Try r, p, s (lower/upper), and 0, 1, 2.
    - Try an invalid input (e.g., 'x' or '9') and confirm it shows an error and stops.
"""

import random


def compChoice():
    """
    Return the computer's choice as a complete word: 'Rock', 'Paper', or 'Scissors'.
    Approach:
        - Generate a random integer in {0, 1, 2}.
        - Map 0->Rock, 1->Paper, 2->Scissors via if/elif (no data structures).
    """
    roll = random.randint(0, 2)
    if roll == 0:
        return "Rock"
    elif roll == 1:
        return "Paper"
    else:
        return "Scissors"


def userChoice(user_input):
    """
    Convert the user's raw input into a full word: 'Rock', 'Paper', or 'Scissors'.
    Accepts:
        - 'r' or 'R' => Rock
        - 'p' or 'P' => Paper
        - 's' or 'S' => Scissors
        - '0' => Rock, '1' => Paper, '2' => Scissors
    Returns:
        - 'Rock' / 'Paper' / 'Scissors' for valid input
        - None for invalid input (so main() can stop gracefully)
    """
    # Normalize whitespace first
    if user_input is None:
        return None
    cleaned = user_input.strip()

    # Accept single-letter inputs, any case
    if cleaned == 'r' or cleaned == 'R':
        return "Rock"
    elif cleaned == 'p' or cleaned == 'P':
        return "Paper"
    elif cleaned == 's' or cleaned == 'S':
        return "Scissors"

    # Accept numeric menu inputs (strings '0','1','2')
    elif cleaned == '0':
        return "Rock"
    elif cleaned == '1':
        return "Paper"
    elif cleaned == '2':
        return "Scissors"

    # Anything else is invalid
    else:
        return None


def game(user_pick, comp_pick):
    """
    Decide the outcome given two complete words: 'Rock'/'Paper'/'Scissors'.
    Returns a result string describing the winner or draw.
    """
    # Same choice => draw
    if user_pick == comp_pick:
        return "It's a draw. No winner."

    # Enumerate winning cases for the user with selection logic only
    if user_pick == "Rock" and comp_pick == "Scissors":
        return "You win! Rock smashes Scissors."
    elif user_pick == "Scissors" and comp_pick == "Paper":
        return "You win! Scissors cut Paper."
    elif user_pick == "Paper" and comp_pick == "Rock":
        return "You win! Paper covers Rock."

    # Otherwise, the computer has the winning pairing
    if comp_pick == "Rock" and user_pick == "Scissors":
        return "Computer wins! Rock smashes Scissors."
    elif comp_pick == "Scissors" and user_pick == "Paper":
        return "Computer wins! Scissors cut Paper."
    else:
        # comp_pick == "Paper" and user_pick == "Rock"
        return "Computer wins! Paper covers Rock."


def main():
    """
    Orchestrates the game:
      - Prints intro and rules
      - Gets user input once
      - Validates and maps it
      - Gets computer choice
      - Prints both choices and the result
    """
    print("Welcome to Rock, Paper, Scissors!")
    print("Enter r, p, or s (any case).")
    print("Alternatively, use 0 for Rock, 1 for Paper, or 2 for Scissors.")
    print("\nRules:")
    print("  - Rock vs Scissors : Rock wins (Rock smashes Scissors)")
    print("  - Scissors vs Paper: Scissors win (Scissors cut Paper)")
    print("  - Paper vs Rock    : Paper wins (Paper covers Rock)\n")

    raw = input("Your choice (r/p/s or 0/1/2): ")
    user_pick = userChoice(raw)

    # If invalid, print helpful message and end main() without continuing.
    if user_pick is None:
        print("\nInvalid input. Please enter r, p, s, or 0/1/2 next time.")
        # End naturally (no sys.exit, no return value needed).
        return

    comp_pick = compChoice()

    print(f"\nYou chose: {user_pick}")
    print(f"Computer chose: {comp_pick}")

    result = game(user_pick, comp_pick)
    print(result)


# Standard guard
if __name__ == "__main__":
    main()

# Written Report 
#
# 1) How did you approach this assignment? Where did you get stuck, if at all,
#    and how did you get unstuck?
#    - I first wrote out the requirements: four functions, random computer
#      choice, single input with validation, and selection-only logic (no loops
#      or data structures). I then planned the mapping from inputs (r/p/s or
#      0/1/2) to full words using if/elif chains to avoid lists/dicts.
#      The only potential sticking point was remembering not to re-prompt on
#      invalid input; I handled that by returning None from userChoice() and
#      stopping early in main().
#
# 2) How did you test your program? What doesn't work the way you might like,
#    such as features you'd like to add once you know more?
#    - I tested lowercase/uppercase letters and 0/1/2. I also tried invalid
#      entries like 'x' or '9' to confirm it stops with a helpful message.
#      Since there is randomness, each run may produce different outcomes,
#      which is expected. In the future, I’d add replay and input re-prompting
#      with loops, plus input error messages that highlight exactly what went
#      wrong, and maybe score-keeping across rounds.
#
# 3) What did you learn from this assignment? What would you do differently
#    next time?
#    - I practiced decomposing the problem into small functions and using
#      selection to map inputs and enforce the rules. Next time, once loops and
#      data structures are allowed, I’d add a replay menu, running scores, and
#      replace the long if/elif chains with cleaner mappings.
