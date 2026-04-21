# 📦 Mini ERP System – Inventory & Sales Dashboard

A lightweight **ERP-style web application** designed to simulate real-world business workflows like inventory management, sales processing, and analytics.

---

## 🚀 Overview

This project demonstrates how businesses manage their day-to-day operations using a centralized system. It allows users to:

* Manage product inventory
* Process sales transactions
* Automatically update stock
* View business insights via dashboard

The goal was to **build a simplified ERP module** aligned with real industry use cases.

---

## ✨ Features

### 🧾 Product Management

* Add new products with price and quantity
* Delete products
* Automatic ID generation

### 📦 Inventory Tracking

* Real-time stock updates
* Low-stock highlighting (visual alert when quantity < 10)

### 💰 Sales System

* Record product sales
* Auto-reduce inventory after transaction
* Prevent sales if stock is insufficient

### 📊 Dashboard Analytics

* Total revenue calculation
* Total number of products
* Top-selling product insight

### 🎨 UI/UX

* Clean dashboard-style layout
* Responsive design
* Interactive buttons and alerts

---

## 🛠️ Tech Stack

| Layer    | Technology                 |
| -------- | -------------------------- |
| Backend  | Python (Flask)             |
| Database | SQLite                     |
| Frontend | HTML, CSS, JavaScript      |
| Styling  | Custom CSS (SaaS-style UI) |

---

## 📂 Project Structure

```
mini-erp/
│
├── app.py
├── database.db (auto-created)
├── .gitignore
├── README.md
│
├── frontend/
│   ├── index.html
│   ├── script.js
│   └── images/
```

---

## ⚙️ How to Run Locally

### 1. Clone the repository

```
git clone https://github.com/YOUR_USERNAME/mini-erp-system.git
cd mini-erp-system
```

### 2. Create virtual environment (optional but recommended)

```
python -m venv venv
venv\Scripts\activate   (Windows)
```

### 3. Install dependencies

```
pip install flask flask-cors
```

### 4. Run backend

```
python app.py
```

### 5. Run frontend

* Open `index.html` using **Live Server** (VS Code recommended)

---

## 🧪 How to Use

1. Add a product (name, price, quantity)
2. View products (inventory list)
3. Make a sale using product ID
4. Check updated stock automatically
5. Load dashboard to view:

   * Revenue
   * Product count
   * Top-selling product

---

## 🧠 Key Concepts Demonstrated

* CRUD operations (Create, Read, Delete)
* REST API development using Flask
* Database integration (SQLite)
* Business logic implementation (inventory + sales)
* Data consistency (stock updates after transactions)
* Frontend-backend communication (Fetch API)

---

## 💡 Why This Project?

Instead of building generic projects, this system was designed to:

> Simulate real-world ERP workflows used in businesses.

It reflects how companies manage:

* Inventory
* Transactions
* Business insights

---

## 🚧 Future Improvements

* Edit product functionality
* User authentication (login system)
* Advanced reporting & charts
* Deployment on cloud (Render / AWS)
* Role-based access (Admin/User)

---

## 📸 Screenshots (Optional)

*Add screenshots here if available*

---

## 🙌 Conclusion

This project helped in understanding how real-world enterprise systems work, especially in:

* Inventory management
* Transaction processing
* Data-driven decision making

---

## ⭐ If you like this project

Give it a star on GitHub!
