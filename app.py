from flask import Flask, request, render_template

app = Flask(__name__)

PROBLEMS = {
    ("easy", "algebra"): "What is 2 + 2?",
    ("medium", "geometry"): "What is the area of a circle with radius 5?",
    ("hard", "number_theory"): "Find all primes less than 100 that are congruent to 1 mod 4.",
    ("easy", "combinatorics"): "How many ways can you arrange 3 books on a shelf?",
}

@app.route("/", methods=["GET", "POST"])
def home():
    problem = None
    if request.method == "POST":
        difficulty = request.form.get("difficulty")
        style = request.form.get("style")
        problem = PROBLEMS.get((difficulty, style), "No problem found for this selection.")
    return render_template("index.html", problem=problem)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)