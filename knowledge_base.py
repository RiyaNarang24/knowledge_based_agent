"""
knowledge_base.py
This file defines the Knowledge Base (KB) used by the AI Agent.
It stores all the logical rules in propositional form.
"""

def create_knowledge_base():
    """
    Creates an initial set of rules for the agent.
    Each rule maps a disease (conclusion) to a list of symptoms (conditions).
    """
    kb = {
        "Flu": ["Fever", "Cough", "Fatigue"],
        "Cold": ["Sneezing", "Cough"],
        "Migraine": ["Headache", "Nausea"],
        "FoodPoisoning": ["Nausea", "Vomiting", "Fatigue"],
        "Allergy": ["Sneezing", "Watery Eyes"],
        "Malaria": ["Fever", "Chills", "Sweating"]
    }

    return kb
