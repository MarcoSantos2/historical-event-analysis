from flask import Flask, render_template_string, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    with open("index.html") as file:
        content = file.read()
    return render_template_string(content)

@app.route('/data')
def data():
    # This will be replaced with actual data fetching from the database
    return jsonify([])

if __name__ == '__main__':
    app.run(debug=True)
