# app.py
import streamlit as st
from knowledge_base import load_kb, save_kb
from inference_engine import infer_with_explanation
from rule_editor import add_rule_to_kb
from facts_database import get_all_facts, validate_facts

st.set_page_config(page_title="Knowledge-Based AI Agent", layout="centered")

st.title("🧠 Knowledge-Based AI Agent (Propositional Logic)")
st.write("A simple rule-based reasoning app — add facts, add rules, see step-by-step inference.")

# Load or initialize KB (stored as a JSON file by knowledge_base)
kb = load_kb()

# Sidebar: KB actions
st.sidebar.header("Knowledge Base")
if st.sidebar.button("Reload KB"):
    kb = load_kb()
    st.sidebar.success("Knowledge base reloaded.")

st.sidebar.markdown("**Add a new rule**")
with st.sidebar.form("new_rule_form", clear_on_submit=True):
    new_conditions = st.text_input("Conditions (comma separated)", placeholder="Fever, Cough")
    new_conclusion = st.text_input("Conclusion (single)", placeholder="Flu")
    submit_rule = st.form_submit_button("Add rule")
    if submit_rule:
        if not new_conditions.strip() or not new_conclusion.strip():
            st.sidebar.error("Please enter both conditions and conclusion.")
        else:
            conds = [c.strip().title() for c in new_conditions.split(",") if c.strip()]
            conc = new_conclusion.strip().title()
            kb = add_rule_to_kb(kb, conds, conc)
            save_kb(kb)
            st.sidebar.success(f"Rule added: If {', '.join(conds)} → {conc}")

# Show KB rules
st.subheader("Knowledge Base Rules")
if kb:
    for i, rule in enumerate(kb, start=1):
        st.markdown(f"**R{i}.** If _{', '.join(rule['if'])}_ → **{rule['then']}**")
else:
    st.info("Knowledge base is empty. Add rules from the sidebar.")

st.markdown("---")

# Main interaction: diagnose / infer
st.subheader("Run Inference")
all_facts = get_all_facts(kb)
st.write("Known facts (from KB):")
st.write(", ".join(all_facts))

entered = st.text_input("Enter observed facts / symptoms (comma separated)", placeholder="Fever, Cough")
if st.button("Infer"):
    facts = [f.strip().title() for f in entered.split(",") if f.strip()]
    valid, invalid = validate_facts(facts, all_facts)
    if invalid:
        st.warning("Some entered facts are not in knowledge base facts list: " + ", ".join(invalid))
    if not valid:
        st.info("No valid facts entered. Use some known facts or add new rules that include them.")
    else:
        results = infer_with_explanation(kb, valid)
        if not results["conclusions"]:
            st.info("No exact conclusion could be derived. Showing partial matches & suggestions below.")
            if results["partial"]:
                st.subheader("Partial matches (percent match)")
                for d, p in sorted(results["partial"].items(), key=lambda x: -x[1]):
                    st.write(f"- **{d}** — {p}% match")
            else:
                st.write("No suggestions available.")
        else:
            st.success("Conclusions derived:")
            for c in results["conclusions"]:
                st.write(f"- **{c}**")
            st.subheader("Reasoning steps")
            for step in results["explanation"]:
                st.write(f"- {step}")
