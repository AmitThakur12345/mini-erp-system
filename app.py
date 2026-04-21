from flask import Flask, request, jsonify
import sqlite3
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Connect to SQLite
conn = sqlite3.connect('database.db', check_same_thread=False)
cursor = conn.cursor()

# Create tables
cursor.execute('''
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    price REAL,
    quantity INTEGER
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER,
    quantity INTEGER,
    total REAL
)
''')

conn.commit()

# ➕ Add Product
@app.route('/add_product', methods=['POST'])
def add_product():
    data = request.json

    if not data.get('name') or not data.get('price') or not data.get('quantity'):
        return jsonify({"error": "Missing fields"}), 400

    cursor.execute(
        "INSERT INTO products (name, price, quantity) VALUES (?, ?, ?)",
        (data['name'], float(data['price']), int(data['quantity']))
    )
    conn.commit()
    return jsonify({"message": "Product added"})

# 📦 Get Products
@app.route('/products', methods=['GET'])
def get_products():
    cursor.execute("SELECT * FROM products")
    rows = cursor.fetchall()

    products = []
    for row in rows:
        products.append({
            "id": row[0],
            "name": row[1],
            "price": row[2],
            "quantity": row[3]
        })

    return jsonify(products)

# 💰 Make Sale
@app.route('/sale', methods=['POST'])
def make_sale():
    data = request.json

    cursor.execute("SELECT * FROM products WHERE id=?", (data['product_id'],))
    product = cursor.fetchone()

    if not product:
        return jsonify({"error": "Product not found"}), 404

    if product[3] < int(data['quantity']):
        return jsonify({"error": "Not enough stock"}), 400

    total = product[2] * int(data['quantity'])

    # Insert sale
    cursor.execute(
        "INSERT INTO sales (product_id, quantity, total) VALUES (?, ?, ?)",
        (data['product_id'], data['quantity'], total)
    )

    # Update stock
    new_qty = product[3] - int(data['quantity'])
    cursor.execute(
        "UPDATE products SET quantity=? WHERE id=?",
        (new_qty, data['product_id'])
    )

    conn.commit()

    return jsonify({
        "message": "Sale successful",
        "total": total
    })

# 📊 Dashboard (UPGRADED)
@app.route('/dashboard', methods=['GET'])
def dashboard():
    # Total revenue
    cursor.execute("SELECT SUM(total) FROM sales")
    revenue = cursor.fetchone()[0] or 0

    # Total products
    cursor.execute("SELECT COUNT(*) FROM products")
    total_products = cursor.fetchone()[0]

    # 🔥 Top selling product
    cursor.execute("""
        SELECT product_id, SUM(quantity) as total_sold
        FROM sales
        GROUP BY product_id
        ORDER BY total_sold DESC
        LIMIT 1
    """)
    top = cursor.fetchone()

    top_product = None

    if top:
        cursor.execute("SELECT name FROM products WHERE id=?", (top[0],))
        name = cursor.fetchone()
        if name:
            top_product = name[0]

    return jsonify({
        "revenue": revenue,
        "total_products": total_products,
        "top_product": top_product or "N/A"
    })

# 🗑️ Delete Product
@app.route('/delete_product/<int:id>', methods=['DELETE'])
def delete_product(id):
    cursor.execute("DELETE FROM products WHERE id=?", (id,))
    conn.commit()
    return jsonify({"message": "Product deleted"})

# 🧹 Clear DB (for demo)
@app.route('/clear', methods=['GET'])
def clear_db():
    cursor.execute("DELETE FROM products")
    cursor.execute("DELETE FROM sales")
    conn.commit()
    return jsonify({"message": "Database cleared"})

# Run app
if __name__ == '__main__':
    app.run(debug=True)