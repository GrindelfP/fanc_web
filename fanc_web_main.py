from flask import Flask, render_template, request
from calculation.calculation import calculate
from operators.operators_dictionariy_and_list import operators_symbol_list
from utility.greetings import operators_as_strings
from utility.input_validation import input_validation

app = Flask(__name__)



@app.route("/")
def main_page() -> "html":
    operators_list = operators_as_strings()

    return render_template("main.html",
                           the_title="Fantastic Calculator V2.0",
                           operators=operators_list,
                           operators_list_length=len(operators_list),
                           operators_symbol_list=operators_symbol_list)


@app.route("/calculate", methods=["POST"])
def do_calculation() -> "html":
    first_number = request.form["first_number"]
    operator = request.form["operator"]
    second_number = request.form["second_number"]
    errors = input_validation(first_number, operator, second_number)
    title = "Here are your result:"
    if errors:
        result = " ".join(errors)
    else:
        result = calculate(first_number, operator, second_number)

    return render_template("result.html",
                           the_title=title,
                           the_result=result)


if __name__ == '__main__':
    app.run(debug=True, threaded=True)
