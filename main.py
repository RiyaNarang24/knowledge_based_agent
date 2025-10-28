"""
main.py
Main controller of the Knowledge-Based AI Agent project.
"""

from knowledge_base import create_knowledge_base
from inference_engine import infer, partial_match
from facts_database import get_all_facts, validate_facts
from helper_functions import print_header, pretty_list_display, ask_user_input
from rule_editor import add_new_rule

def main():
    print_header("KNOWLEDGE-BASED AI AGENT USING PROPOSITIONAL LOGIC")

    kb = create_knowledge_base()

    while True:
        print("\nChoose an option:")
        print("1. View all known symptoms")
        print("2. Diagnose based on symptoms")
        print("3. Add new rule to knowledge base")
        print("4. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            print_header("LIST OF KNOWN SYMPTOMS")
            all_facts = get_all_facts(kb)
            pretty_list_display(all_facts)

        elif choice == "2":
            all_facts = get_all_facts(kb)
            user_facts = ask_user_input()
            valid, invalid = validate_facts(user_facts, all_facts)

            if invalid:
                print("\n⚠️ These symptoms are not in the knowledge base:")
                pretty_list_display(invalid)

            if not valid:
                print("\nNo valid symptoms entered.")
                continue

            # Exact match inference
            conclusions = infer(kb, valid)
            if conclusions:
                print_header("EXACT MATCH RESULTS")
                pretty_list_display(conclusions)
            else:
                print_header("NO EXACT MATCH FOUND")
                print("However, here are possible suggestions:")
                suggestions = partial_match(kb, valid)
                for disease, percent in suggestions.items():
                    print(f"{disease}: {percent}% match")

        elif choice == "3":
            kb = add_new_rule(kb)

        elif choice == "4":
            print("\n👋 Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
