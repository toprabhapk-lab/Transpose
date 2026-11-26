
from flask import Flask, request, render_template_string

app = Flask(__name__)

# HTML page
html = """
<!DOCTYPE html>
<html>
<head>
    <title>Matrix Transpose</title>
</head>
<body style="background-color: #f0f8ff;">

    <h2 align="center">Matrix Transpose Calculator</h2>

    <form method="POST">
        <center>
            <p>Enter matrix elements row by row:</p>

            <textarea name="matrix" rows="5" cols="30"
            placeholder="1 2 3&#10;4 5 6" required></textarea>

            <br><br>
            <input type="submit" value="Find Transpose">
        </center>
    </form>

    {% if result %}
        <h3 align="center">Transpose of Matrix:</h3>
        <center>
            <pre>{{ result }}</pre>
        </center>
    {% endif %}

    {% if error %}
        <p align="center" style="color:red;">{{ error }}</p>
    {% endif %}

</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def transpose():

    result = ""
    error = ""

    if request.method == "POST":
        try:
            # Read matrix from the web page
            data = request.form["matrix"]

            # Convert input into a matrix
            matrix = [
                [int(x) for x in row.split()]
                for row in data.strip().splitlines()
            ]

            # Check equal number of columns
            if not matrix or any(len(row) != len(matrix[0])
                                 for row in matrix):
                raise ValueError("All rows must have equal columns.")

            # Find transpose
            transpose_matrix = []

            for j in range(len(matrix[0])):
                row = []
                for i in range(len(matrix)):
                    row.append(matrix[i][j])
                transpose_matrix.append(row)

            # Convert result into display format
            result = "\n".join(
                " ".join(map(str, row))
                for row in transpose_matrix
            )

        except ValueError as e:
            error = "Invalid matrix input: " + str(e)

    return render_template_string(
        html, result=result, error=error
    )


if __name__ == "__main__":
    app.run(debug=True)
