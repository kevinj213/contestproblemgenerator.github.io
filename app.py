from flask import Flask, render_template_string, request

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Math Contest Problem Trainer</title>
    <style>
        body {
            background: linear-gradient(135deg, #e0eafc, #cfdef3);
            font-family: 'Segoe UI', Arial, sans-serif;
            margin: 0;
            padding: 0;
            min-height: 100vh;
        }
        .container {
            background: white;
            max-width: 400px;
            margin: 60px auto;
            padding: 32px 24px;
            border-radius: 16px;
            box-shadow: 0 8px 32px rgba(0,0,0,0.12);
        }
        h1 {
            text-align: center;
            color: #2d3a4b;
            margin-bottom: 24px;
        }
        label {
            display: block;
            margin: 12px 0 6px;
            color: #2d3a4b;
        }
        select, button {
            width: 100%;
            padding: 8px;
            margin-bottom: 16px;
            border-radius: 6px;
            border: 1px solid #bfc9d1;
            font-size: 1rem;
        }
        button {
            background: #4f8cff;
            color: white;
            border: none;
            cursor: pointer;
            font-weight: bold;
            transition: background 0.2s;
        }
        button:hover {
            background: #2563eb;
        }
        .result {
            margin-top: 24px;
            padding: 16px;
            background: #f1f5fa;
            border-radius: 8px;
            color: #2d3a4b;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Math Contest Problem Trainer</h1>
        <form method="post">
            <label for="difficulty">Difficulty:</label>
            <select name="difficulty" id="difficulty" required>
                <option value="">Select...</option>
                <option value="easy">Easy</option>
                <option value="medium">Medium</option>
                <option value="hard">Hard</option>
            </select>
            <label for="style">Style:</label>
            <select name="style" id="style" required>
                <option value="">Select...</option>
                <option value="algebra">Algebra</option>
                <option value="geometry">Geometry</option>
                <option value="number_theory">Number Theory</option>
                <option value="combinatorics">Combinatorics</option>
            </select>
            <button type="submit">Get Problem</button>
        </form>
        {% if problem %}
        <div class="result">
            <strong>Sample Problem:</strong>
            <p>{{ problem }}</p>
        </div>
        {% endif %}
    </div>
</body>
</html>
"""

# Dummy problems for demonstration
PROBLEMS = {
    ("easy", "algebra"): "What is 2 + 2?",
    ("medium", "geometry"): "What is the area of a circle with radius 5?",
    ("hard", "number_theory"): "Find all primes less than 100 that are congruent to 1 mod 4.",
    ("easy", "combinatorics"): "How many ways can you arrange 3 books on a shelf?",
    # Add more as needed
}

@app.route("/", methods=["GET", "POST"])
def home():
    problem = None
    if request.method == "POST":
        difficulty = request.form.get("difficulty")
        style = request.form.get("style")
        problem = PROBLEMS.get((difficulty, style), "No problem found for this selection.")
    return render_template_string(HTML_TEMPLATE, problem=problem)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)