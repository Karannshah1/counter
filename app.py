from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Global variable to store the count
count = 0

@app.route('/')
def index():
    global count
    return render_template('index.html', count=count)

@app.route('/increment', methods=['POST'])
def increment():
    global count
    count += 1
    return redirect(url_for('index'))

@app.route('/reset', methods=['POST'])
def reset():
    global count
    count = 0
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
