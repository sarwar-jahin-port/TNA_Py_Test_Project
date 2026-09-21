# E-Commerce CLI System (Version 1\)

## Comprehensive Team Blueprint & Execution Guide

---

## 1\. Executive Summary & Project Goal

The **E-Commerce CLI System** is a lightweight, function-based terminal application built in Python. It provides a complete e-commerce workflow—including user authentication, product catalog browsing, inventory management, shopping cart operations, discount applications, and sales reporting.

### Core Architecture Principles

* **Pure Procedural Paradigm:** No Object-Oriented Programming (OOP) classes or instances. All logic is organized using pure functions and standard Python data structures.  
* **Separation of Concerns:** Functional modules process data and return results; they **never** perform direct terminal input or print operations (`input()` / `print()`).  
* **Centralized I/O:** The CLI Orchestrator (`main.py`) serves as the single point of contact for user input and terminal output.  
* **In-Memory Storage:** Initial data and application state live in `db.py` during execution.

---

## 2\. System Architecture & Component Mapping

                               ┌─────────────────────────┐

                               │         db.py           │

                               │   (In-Memory Storage)   │

                               └────────────┬────────────┘

                                            │

                               ┌────────────▼────────────┐

                               │         main.py         │

                               │    (CLI Orchestrator)   │

                               └────────────┬────────────┘

                                            │

        ┌───────────────────────────────────┼───────────────────────────────────┐

        ▼                                   ▼                                   ▼

┌─────────────────┐               ┌─────────────────┐               ┌─────────────────┐

│     auth.py     │               │   catalog.py    │               │    orders.py    │

│ (User & Access) │               │ (Products/Stock)│               │ (Cart & Orders) │

└─────────────────┘               └─────────────────┘               └─────────────────┘

---

## 3\. Standardized Data Structures & Schema

All modules communicate strictly using Python standard data types (lists, dictionaries, and sets).

| Entity | Python Data Structure | Example Schema |
| :---- | :---- | :---- |
| **Users Database** | `list[dict]` | `[{"id": 1, "username": "admin", "password": "123", "role": "admin"}]` |
| **Catalog Database** | `list[dict]` | `[{"id": 101, "name": "Keyboard", "price": 2000.0, "stock": 10}]` |
| **Shopping Cart** | `list[dict]` | `[{"id": 101, "name": "Keyboard", "price": 2000.0, "qty": 2}]` |
| **Order History** | `list[dict]` | `[{"order_id": 5001, "user_id": 2, "items": [...], "total": 4000.0}]` |
| **Allowed Roles** | `set` | `{"admin", "customer"}` |

---

## 4\. Team Member Roles & Technical Responsibilities

### Member 1: User Authentication & Access Control (`auth.py`)

* **Core Responsibilities:** User authentication, credential validation, and role permission checks.  
* **Functions to Build:**  
  * `login(users_db, username, password) -> dict | None`: Iterates over user records to verify credentials. Returns the user dict if valid; otherwise `None`.  
  * `check_permission(user_role, allowed_roles) -> bool`: Checks if `user_role` exists in the `allowed_roles` set using fast set membership lookup.

---

### Member 2: Product Catalog & Inventory (`catalog.py`)

* **Core Responsibilities:** Inventory availability filtering, product search, and stock updates.  
* **Functions to Build:**  
  * `get_available_products(catalog) -> list`: Filters and returns items where `stock > 0`.  
  * `search_products(catalog, keyword) -> list`: Performs a case-insensitive search matching `keyword.lower()` against product names.  
  * `update_stock(catalog, product_id, quantity) -> bool`: Decrements stock by `quantity` for the given product ID upon checkout.

---

### Member 3: Cart Calculation & Order Processing (`orders.py`)

* **Core Responsibilities:** Subtotal calculation, threshold-based discount application, and order generation.  
* **Functions to Build:**  
  * `calculate_cart_total(cart) -> float`: Calculates the raw subtotal (`sum(item["price"] * item["qty"])`).  
  * `apply_discount(total, rate=0.10) -> float`: Applies a percentage discount if the subtotal exceeds a specific threshold (e.g., $5,000).  
  * `create_order(user, cart) -> dict`: Compiles user information, cart contents, and final total into an order record dictionary.

---

### Member 4 (Lead): CLI Orchestrator & Storage (`db.py` & `main.py`)

* **Core Responsibilities:** Terminal interface navigation, menu control flow, I/O routing, and sales summary reporting.  
* **Files & Functions to Build:**  
  * `db.py`: Stores initial mock datasets for users, products, roles, and order history.  
  * `main.py` \-\> `main_menu()`: Controls the terminal loop (`while True`) for user interaction across Browsing, Cart, and Admin options.  
  * `generate_sales_report(orders_list)`: Aggregates complete order history to compute total revenue and sales statistics.

---

## 5\. **Recommended Git Workflow Strategy**

1. ## **Branch Naming Standard (`feature/<scope>/<developer_name>`)**

   * ## Keeping standard prefixes like `feature/` alongside the dev's name ensures clarity on who owns the branch and what feature it belongs to.

   * ## Examples:

     * ## `feature/auth/sarwar`

2. ## **Branching Off `dev`**

   * ## `dev` serves as the continuous integration branch.

   * ## Developers create their feature branches directly off `dev` and push their work there.

3. ## **Pull Request (PR) & Mandatory Code Reviews**

   * ## Code is pushed to GitHub, and a PR is opened targeting **`dev`** (never directly to `main`).

   * ## A minimum of **1 peer approvals** is required before merging into `dev`.

4. ## **Release Cutover (`dev` \-\> `main`)**

   * ## Once all team features are merged and Version 1 is tested and confirmed stable on `dev`, a final Pull Request is created from **`dev` to `main`**.

## 6\. Testing & Final Verification Checklist

Prior to project submission, perform the following validation steps:

1. Run the system end-to-end: `python main.py`.  
2. Test user login with customer and admin roles.  
3. Search for products, add items to cart, verify stock reduction, and complete an order.  
4. Verify overall commit structure and branch graph: `git log --graph --oneline`.