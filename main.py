#Alalysis of the patient triage levels
# Rules are structured to mimic Triage levels (1 is highest priority).
rules = [
    # R1: Level 1 (Resuscitation) - Immediate life-saving intervention
    {"vitals": "Unstable", "triage_level": 1, "status": "Critical", "action": "Immediate Trauma Bay/OR."},
    {"complaint": "Unresponsive", "triage_level": 1, "status": "Critical", "action": "Immediate Trauma Bay/OR."},
    
    # R2: Level 2 (Emergent) - High risk, needs prompt evaluation
    {"complaint": "Chest Pain", "age": "> 60", "triage_level": 2, "status": "Emergent", "action": "Fast-Track to ECG and Monitoring."},
    {"complaint": "Severe Fracture", "vitals": "Stable", "triage_level": 2, "status": "Emergent", "action": "Pain meds and STAT X-ray."},
    
    # R3: Level 3 (Urgent) - Needs treatment, but can wait
    {"vitals": "Stable", "resources": "Complex Labs/Imaging", "triage_level": 3, "status": "Urgent", "action": "Standard ED Bed."},
    
    # R4: Level 4 (Non-Urgent) - Requires minimal resources
    {"complaint": "Minor Cold/Flu", "pain": "<= 3", "triage_level": 5, "status": "Non-Urgent", "action": "Fast-Track Clinic or Home Care Advice."},

     # R5: Pediatric Exception (Elevating priority for young patients)
    {"age": "< 5", "vitals": "Stable", "triage_level": 3, "status": "Urgent", "action": "Pediatric Bed. Reassess within 1 hour."},
    
    # R6: Default Action
    {"triage_level": 4, "status": "Non-Life-Threatening", "action": "Standard Waiting Area. Reassess Vitals if wait > 2 hours."}
]

# 2. INFERENCE ENGINE (Handles numerical and categorical facts)
def assess_triage(patient_id, facts):
    """
    Runs forward chaining on the rules to find the appropriate triage level and action.
    """
    print(f"\n--- Triage Assessment for Patient {patient_id} ---")
    
    for rule in rules:
        is_match = True
        
        for key, value in rule.items():
            if key in facts and key not in ["triage_level", "status", "action"]:
                fact_value = facts[key]
                rule_condition = value

                if isinstance(rule_condition, str) and ('<' in rule_condition or '>' in rule_condition or '=' in rule_condition):
                    op = rule_condition[0:2].strip() if rule_condition[1] in ('=', '<', '>') else rule_condition[0]
                    threshold = float(''.join(filter(str.isdigit, rule_condition)))
                    
                    try:
                        fact_num = float(fact_value)
                        
                        if op == '>=':
                            if not (fact_num >= threshold): is_match = False
                        elif op == '<=':
                            if not (fact_num <= threshold): is_match = False
                        elif op == '<':
                            if not (fact_num < threshold): is_match = False
                        elif op == '>':
                            if not (fact_num > threshold): is_match = False
                            
                    except ValueError:
                        is_match = False
                
                # Simple categorical string match
                elif fact_value != rule_condition:
                    is_match = False
                
                if not is_match:
                    break
        
        if is_match:
            print(f"**Triage Level: {rule['triage_level']} ({rule['status']})**")
            print(f"*Recommended Action:* {rule['action']}")
            print(f"(Rule Matched: R{rules.index(rule) + 1})")
            return
            
    # Default Rule Fired (R6 if placed last)
    default_rule = rules[-1]
    print(f"**Triage Level: {default_rule['triage_level']} ({default_rule['status']})**")
    print(f"*Recommended Action:* {default_rule['action']}")


# Scenario 1: Immediate Life Threat (R1)
facts1 = {
    "age": 45,
    "complaint": "Severe Bleeding",
    "vitals": "Unstable",
    "pain": 10,
    "resources": "Immediate Surgery"
}

# Scenario 2: High Risk/Elderly (R2)
facts2 = {
    "age": 65,
    "complaint": "Chest Pain",
    "vitals": "Stable",
    "pain": 7,
    "resources": "ECG/Labs"
}

# Scenario 3: Pediatric Exception (R5)
facts3 = {
    "age": 3,
    "complaint": "High Fever",
    "vitals": "Stable",
    "pain": 4,
    "resources": "Basic Labs"
}

# Scenario 4: Non-Urgent (R4)
facts4 = {
    "age": 28,
    "complaint": "Minor Cold/Flu",
    "vitals": "Stable",
    "pain": 2,
    "resources": "None"
}


assess_triage("P-101", facts1)
assess_triage("P-102", facts2)
assess_triage("P-103", facts3)
assess_triage("P-104", facts4)