from flask import Flask, render_template, request

app = Flask(__name__)


def calculate(num1, num2, operation):
    """Perform the requested calculation."""

    if operation == "add":
        return num1 + num2

    elif operation == "subtract":
        return num1 - num2

    elif operation == "multiply":
        return num1 * num2

    elif operation == "divide":
        if num2 == 0:
            raise ValueError("Cannot divide by zero.")

        return num1 / num2

    raise ValueError("Invalid operation.")


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None

    if request.method == "POST":
        try:
            num1 = float(request.form["num1"])
            num2 = float(request.form["num2"])
            operation = request.form["operation"]

            result = calculate(num1, num2, operation)

        except ValueError as e:
            error = str(e)

        except (KeyError, TypeError):
            error = "Invalid input."

    return render_template(
        "index.html",
        result=result,
        error=error
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
