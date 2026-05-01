# decision_engine.py
import json

def get_ai_decision(product, budget, priority):

    # Simulated AI logic (smart decision rules)

    if product.lower() == "laptop":
        if priority == "performance":
            decision = "Dell Inspiron 15"
            reason = "Good performance within budget"
        elif priority == "battery":
            decision = "MacBook Air M1"
            reason = "Excellent battery life"
        else:
            decision = "HP 15s"
            reason = "Best value for money"

    elif product.lower() == "phone":
        if priority == "battery":
            decision = "Samsung M34"
            reason = "Strong battery backup"
        else:
            decision = "Redmi Note 12"
            reason = "Balanced features"

    else:
        decision = "Generic Product"
        reason = "Based on basic preferences"

    return {
        "decision": decision,
        "reason": reason,
        "tradeoffs": ["May compromise on other features"],
        "confidence": "Medium"
    }