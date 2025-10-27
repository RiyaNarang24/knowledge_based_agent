"""
inference_engine.py
This file contains the core reasoning logic of the AI agent.
It applies propositional logic to infer conclusions from facts.
"""

def infer(kb, facts):
    """
    Perform simple forward-chaining inference:
    If all conditions of a rule are present in the given facts,
    the corresponding conclusion (disease) is inferred.
    """
    conclusions = []

    for disease, symptoms in kb.items():
        matched = [s for s in symptoms if s in facts]
        if len(matched) == len(symptoms):
            conclusions.append(disease)

    return conclusions


def partial_match(kb, facts):
    """
    Suggest diseases that partially match the given symptoms.
    This helps when not all symptoms are entered.
    """
    suggestions = {}
    for disease, symptoms in kb.items():
        matched = [s for s in symptoms if s in facts]
        if matched:
            match_percent = (len(matched) / len(symptoms)) * 100
            suggestions[disease] = round(match_percent, 2)
    return suggestions
