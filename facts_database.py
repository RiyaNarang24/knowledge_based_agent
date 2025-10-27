"""
facts_database.py
This file stores and manages the list of possible facts (symptoms).
It helps to validate user input and maintain a structured database.
"""

def get_all_facts(kb):
    """
    Extracts all unique facts (symptoms) from the knowledge base.
    """
    all_facts = set()
    for symptoms in kb.values():
        all_facts.update(symptoms)
    return sorted(list(all_facts))


def validate_facts(user_facts, known_facts):
    """
    Ensures user-entered facts exist in the knowledge base.
    """
    valid = [fact for fact in user_facts if fact in known_facts]
    invalid = [fact for fact in user_facts if fact not in known_facts]
    return valid, invalid
