from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/connect', methods=['POST'])
def connect():
    db_type = request.form['db_type']
    host = request.form['host']
    port = request.form['port']
    username = request.form['username']
    password = request.form['password']
    database = request.form['database']
    connection_info = {
        'type': db_type,
        'host': host,
        'port': port,
        'username': username,
        'password': password,
        'database': database
    }
    return jsonify(connection_info)

if __name__ == '__main__':
    app.run(debug=True)

