# 🧠 Knowledge-Based AI Agent using Propositional Logic

This project demonstrates how an **AI agent** can reason using **Propositional Logic** and a **Knowledge Base**.  
The system can diagnose diseases from given symptoms, and new rules can be added dynamically.

---

## 🎯 Objective
To design a simple AI reasoning system that:
- Stores knowledge in the form of rules (If symptoms → disease)
- Accepts user facts (symptoms)
- Infers conclusions logically
- Allows users to expand knowledge over time

---

## ⚙️ Technologies Used
- Python (Only Core Concepts)
- Rule-based Inference (Forward Chaining)

---

## 🧩 Features
- View all known symptoms
- Diagnose diseases from symptoms
- Partial match suggestions
- Add new rules dynamically
- Modular codebase (multiple Python files)

---

## 🧠 Working Principle
1. The **Knowledge Base** stores rules like:
   - If Fever, Cough, Fatigue → Flu  
   - If Nausea, Vomiting → Food Poisoning  
2. The **Inference Engine** checks if the user’s facts satisfy any rule.
3. If yes → that conclusion is inferred.
4. If not → similar matches are shown.

---

## ▶️ How to Run
```bash
python main.py
