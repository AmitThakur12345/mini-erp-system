const API = "http://127.0.0.1:5000";

function addProduct() {
    fetch(API + "/add_product", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
            name: document.getElementById("name").value,
            price: document.getElementById("price").value,
            quantity: document.getElementById("qty").value
        })
    }).then(() => loadProducts());
}

function loadProducts() {
    fetch(API + "/products")
    .then(res => res.json())
    .then(data => {
        let table = document.getElementById("productTable");
        table.innerHTML = "";

        data.forEach(p => {
            let lowStock = p.quantity < 10 ? "low-stock" : "";

            table.innerHTML += `
                <tr class="${lowStock}">
                    <td>${p.id}</td>
                    <td>${p.name}</td>
                    <td>${p.price}</td>
                    <td>${p.quantity}</td>
                    <td>
                        <button class="delete-btn" onclick="deleteProduct(${p.id})">
                            Delete
                        </button>
                    </td>
                </tr>
            `;
        });
    });
}

function makeSale() {
    fetch(API + "/sale", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
            product_id: document.getElementById("pid").value,
            quantity: document.getElementById("sqty").value
        })
    })
    .then(res => res.json())
    .then(data => {
        alert(data.message || data.error);
        loadProducts();
    });
}

function loadDashboard() {
    fetch(API + "/dashboard")
    .then(res => res.json())
    .then(data => {
        document.getElementById("dash").innerText =
            "Revenue: " + data.revenue +
            " | Products: " + data.total_products +
            " | Top Selling: " + (data.top_product || "N/A");
    });
}

function searchProducts() {
    let input = document.getElementById("search").value.toLowerCase();

    fetch(API + "/products")
    .then(res => res.json())
    .then(data => {
        let list = document.getElementById("productList");
        list.innerHTML = "";

        data
        .filter(p => p.name.toLowerCase().includes(input))
        .forEach(p => {
            let lowStock = p.quantity < 10 ? "⚠️ Low Stock" : "";
            let className = p.quantity < 10 ? "low-stock" : "";

            list.innerHTML += `
                <li class="${className}">
                    ID: ${p.id} | ${p.name} | Qty: ${p.quantity}
                    <button onclick="deleteProduct(${p.id})">Delete</button>
                </li>`;
        });
    });
}

function deleteProduct(id) {
    fetch(API + "/delete_product/" + id, {
        method: "DELETE"
    })
    .then(res => res.json())
    .then(data => {
        alert(data.message);
        loadProducts();
    });
}

loadProducts();