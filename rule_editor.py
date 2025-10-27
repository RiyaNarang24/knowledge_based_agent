"""
rule_editor.py
Allows the user to add new rules (knowledge) dynamically.
Simulates how knowledge bases in AI can grow over time.
"""

def add_new_rule(kb):
    print("\nAdd a new rule to the knowledge base.")
    disease = input("Enter the name of the disease/conclusion: ").title()
    symptoms = input("Enter symptoms for this disease (comma separated): ").title().split(",")
    symptoms = [s.strip() for s in symptoms if s.strip()]

    if disease in kb:
        print(f"Rule for {disease} already exists. Updating its symptoms.")
        kb[disease].extend(symptoms)
        kb[disease] = list(set(kb[disease]))  # remove duplicates
    else:
        kb[disease] = symptoms

    print(f"✅ Rule added successfully for {disease}!")
    return kb
