from flask import Flask, render_template, flash, redirect, url_for
from flask_wtf import FlaskForm
from flask import request
from wtforms import StringField, IntegerField
from wtforms.validators import InputRequired

app = Flask(__name__)
app.secret_key = 'secret'

# Mock database connection
conn = {
    'host': '',
    'port': ''
}

# Mock table data
tables = [
    {
        'name': 'orders',
        'columns': ['order_id', 'customer_name', 'order_date'],
        'data': [
            {'order_id': 1, 'customer_name': 'John Doe', 'order_date': '2022-01-01'},
            {'order_id': 2, 'customer_name': 'Jane Smith', 'order_date': '2022-01-02'},
            {'order_id': 3, 'customer_name': 'Bob Johnson', 'order_date': '2022-01-03'}
        ]
    },
    {
        'name': 'products',
        'columns': ['product_id', 'product_name', 'price'],
        'data': [
            {'product_id': 1, 'product_name': 'Product A', 'price': 10.99},
            {'product_id': 2, 'product_name': 'Product B', 'price': 20.99},
            {'product_id': 3, 'product_name': 'Product C', 'price': 30.99}
        ]
    }
]
import sqlite3
from collections import namedtuple

Table = namedtuple('Table', ['name', 'columns', 'rows'])
Column = namedtuple('Column', ['name', 'type'])
Row = namedtuple('Row', ['values'])

def create_connection(db_type, host, port, username, password):
    # Create a mock database connection
    conn = sqlite3.connect(':memory:')
    return conn

def get_tables(conn):
    # Generate mock data for each table
    customers_data = [
        Row(['John Smith', '123 Main St', 'Anytown, USA', '555-1234']),
        Row(['Jane Doe', '456 Elm St', 'Sometown, USA', '555-5678']),
        Row(['Bob Johnson', '789 Oak St', 'Yourtown, USA', '555-9012'])
    ]
    orders_data = [
        Row(['1', '2023-02-01', 'John Smith', 'Red Widget', '10', '100.00']),
        Row(['2', '2023-02-02', 'Jane Doe', 'Green Widget', '20', '200.00']),
        Row(['3', '2023-02-03', 'Bob Johnson', 'Blue Widget', '30', '300.00'])
    ]

    # Define the schema for each table
    customers_columns = [
        Column('Name', 'TEXT'),
        Column('Address', 'TEXT'),
        Column('CityStateZip', 'TEXT'),
        Column('Phone', 'TEXT')
    ]
    orders_columns = [
        Column('OrderID', 'INTEGER'),
        Column('OrderDate', 'DATE'),
        Column('CustomerName', 'TEXT'),
        Column('Product', 'TEXT'),
        Column('Quantity', 'INTEGER'),
        Column('Price', 'REAL')
    ]

    # Create a list of tables
    customers = Table('Customers', customers_columns, customers_data)
    orders = Table('Orders', orders_columns, orders_data)
    tables = [customers, orders]

    return tables

class ConnectionForm(FlaskForm):
    host = StringField('Host', validators=[InputRequired()])
    port = IntegerField('Port', validators=[InputRequired()])

@app.route('/', methods=['GET', 'POST'])
def home():
    form = ConnectionForm()
    if form.validate_on_submit():
        conn['host'] = form.host.data
        conn['port'] = form.port.data
        flash('Connected successfully', 'success')
        return redirect(url_for('tables'))
    return render_template('home.html', form=form)

@app.route('/tables', methods=['GET', 'POST'])
def tables():
    if not conn['host'] or not conn['port']:
        flash('Please enter connection information', 'danger')
        return redirect(url_for('home'))
    return render_template('tables.html', tables=tables)

@app.route('/connect', methods=['POST'])
def connect():
    db_type = request.form['db_type']
    host = request.form['host']
    port = request.form['port']
    username = request.form['username']
    password = request.form['password']

    # Create a mock database connection
    conn = create_connection(db_type, host, port, username, password)

    # Get the list of tables for the selected database
    tables = get_tables(conn)

    return render_template('tables.html', tables=tables)


if __name__ == '__main__':
    app.run(debug=True)

