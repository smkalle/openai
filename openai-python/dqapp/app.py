from flask import Flask, render_template, request, jsonify
import psycopg2  # assuming you're using PostgreSQL as the database

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
    try:
        conn = psycopg2.connect(
            host=host,
            port=port,
            user=username,
            password=password,
            database=database
        )
        cur = conn.cursor()
        cur.execute('SELECT table_name FROM information_schema.tables WHERE table_schema = \'public\'')
        tables = [t[0] for t in cur.fetchall()]
        conn.close()
        return render_template('table.html', tables=tables)
    except psycopg2.Error as e:
        error_message = str(e)
        return render_template('index.html', error=error_message)

@app.route('/table', methods=['POST'])
def table():
    table_name = request.form['table']
    conn = psycopg2.connect(
        host=request.form['host'],
        port=request.form['port'],
        user=request.form['username'],
        password=request.form['password'],
        database=request.form['database']
    )
    cur = conn.cursor()
    cur.execute(f'SELECT column_name, data_type FROM information_schema.columns WHERE table_name = \'{table_name}\'')
    columns = [(c[0], c[1]) for c in cur.fetchall()]
    conn.close()
    return render_template('column.html', table=table_name, columns=columns)

@app.route('/validate', methods=['POST'])
def validate():
    table_name = request.form['table']
    conn = psycopg2.connect(
        host=request.form['host'],
        port=request.form['port'],
        user=request.form['username'],
        password=request.form['password'],
        database=request.form['database']
    )
    cur = conn.cursor()
    cur.execute(f'SELECT column_name, data_type FROM information_schema.columns WHERE table_name = \'{table_name}\'')
    columns = [(c[0], c[1]) for c in cur.fetchall()]
    conn.close()
    validations = {}
    for column in columns:
        column_name = column[0]
        validation = request.form.get(column_name)
        if validation:
            validations[column_name] = validation
    return jsonify(validations)

if __name__ == '__main__':
    app.run(debug=True)

