from schema import DecisionOutput
from decision_engine import get_ai_decision


def get_user_input():
    product = input("Enter product: ")
    budget = input("Enter budget: ")
    priority = input("Enter priority (performance/battery/price): ")
    return product, budget, priority


# 👇 PUT IT HERE
def generate_decision(product, budget, priority):

    ai_output = get_ai_decision(product, budget, priority)

    return DecisionOutput(
        product=product,
        decision=ai_output["decision"],
        reason=ai_output["reason"],
        tradeoffs=ai_output["tradeoffs"],
        confidence=ai_output["confidence"]
    )


def main():
    product, budget, priority = get_user_input()
    result = generate_decision(product, budget, priority)

    print("\n--- Decision Output ---")
    print(result.model_dump_json(indent=2))   # ⚠️ updated for Pydantic v2


if __name__ == "__main__":
    main()