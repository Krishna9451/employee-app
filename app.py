from flask import Flask, request, render_template_string

app = Flask(__name__)

employees = []

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Employee Manager</title>
</head>
<body>
    <h1>Employee Manager</h1>

    <form method="POST" action="/add">
        <input type="text" name="name" placeholder="Employee Name" required>
        <button type="submit">Add Employee</button>
    </form>

    <h2>Employee List</h2>
    <ul>
    {% for emp in employees %}
        <li>{{ emp }}</li>
    {% endfor %}
    </ul>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML, employees=employees)

@app.route("/add", methods=["POST"])
def add_employee():
    name = request.form["name"]
    employees.append(name)
    return home()

if __name__ == "__main__":
    app.run(debug=True)
