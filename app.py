from flask import Flask, render_template, request, jsonify
from datetime import date

app = Flask(__name__)

# Initialize counter and the last date it was updated
counter = {'count': 0, 'date': date.today().isoformat()}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/increment', methods=['POST'])
def increment():
    global counter
    current_date = date.today().isoformat()
    if counter['date'] != current_date:
        counter['count'] = 0
        counter['date'] = current_date

    counter['count'] += 1
    return jsonify(count=counter['count'])

@app.route('/reset', methods=['POST'])
def reset():
    global counter
    counter['count'] = 0
    counter['date'] = date.today().isoformat()
    return jsonify(count=counter['count'])

if __name__ == '__main__':
    app.run(debug=True)
