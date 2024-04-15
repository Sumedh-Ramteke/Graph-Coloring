from flask import Flask, render_template, jsonify
from graph_coloring import map_coloring_solver

# Create an instance of Flask
app = Flask(__name__)
# CORS(app)

# Route to render index.html template
@app.route("/")
def home():
    # Return template and data
    return render_template("index.html")

@app.route("/australia")
def australia():
    return render_template("australia.html")

@app.route("/india")
def india():
    # Return template and data
    return render_template("india.html")

@app.route("/get_australia_color")
def get_australia_color():
    return jsonify(map_coloring_solver(1))

@app.route("/get_india_color")
def get_india_color():
    return jsonify(map_coloring_solver(2))

#main
if __name__ == "__main__":
    app.run(host='localhost', debug=True)