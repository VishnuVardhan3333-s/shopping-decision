from flask import Flask, render_template, request
from decision_engine import get_ai_decision
from schema import DecisionOutput

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        product = request.form["product"]
        budget = request.form["budget"]
        priority = request.form["priority"]

        ai_output = get_ai_decision(product, budget, priority)

        result = DecisionOutput(
            product=product,
            decision=ai_output["decision"],
            reason=ai_output["reason"],
            tradeoffs=ai_output["tradeoffs"],
            confidence=ai_output["confidence"]
        )

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)