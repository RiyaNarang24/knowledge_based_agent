"""
helper_functions.py
Contains utility functions for clean input/output formatting.
"""

def print_header(title):
    print("\n" + "="*60)
    print(title.center(60))
    print("="*60)


def pretty_list_display(items):
    for item in items:
        print(f"• {item}")


def ask_user_input():
    """
    Takes user symptoms as input and returns a list.
    """
    print("\nEnter your symptoms (comma separated):")
    user_input = input("> ").title().split(",")
    facts = [x.strip() for x in user_input if x.strip()]
    return facts
