# Hospital-Triage-Expert-System
This project implements a Rule-Based Expert System using Python to automate the critical initial decision-making process in a hospital's Emergency Department (ED). The system mimics the judgmental knowledge of a senior triage nurse or physician, translating established medical protocols  into explicit IF-THEN rules.

The primary goal is to quickly and consistently assign a Triage Level (1-5) to an incoming patient and recommend the appropriate immediate resource allocation (e.g., Trauma Bay, Standard Bed, Fast-Track Clinic).

Key Features
Rule-Based Reasoning: Utilizes Forward Chaining to process patient facts against a defined Knowledge Base.

Prioritization Logic: Rules are structured hierarchically, prioritizing life-saving interventions (Level 1: Critical) over non-urgent issues (Level 5).

Exception Handling: Includes specific rules for complex scenarios, such as the automatic escalation of priority for pediatric patients (Rule R5).

Categorical and Numerical Fact Processing: Handles both string inputs (Vitals_Stability: "Unstable") and numerical comparisons (Pain_Level_1_10: <= 3).

Expert System Components
The system is split into two main logical parts:

1. The Knowledge Base (rules list)
This is a list of Python dictionaries, where each dictionary represents an IF-THEN rule.

IF (Antecedent): Patient characteristics (e.g., "vitals": "Unstable")

THEN (Consequent): The decision and action (e.g., "triage_level": 1, "action": "Immediate Trauma Bay/OR.")

2. The Inference Engine (assess_triage function)
This function contains the core logic that takes a set of patient facts and iterates through the rule list. It fires (executes) the first rule where all antecedent conditions match the provided facts, and then stops, providing the definitive triage recommendation.


Usage and How to Run
Requirements
Python 3.x (No external libraries required)

Execution Steps
Save the provided code into a file named TriageExpertSystem.py.

Open your terminal or command prompt.

Run the script:

Bash:
python TriageExpertSystem.py