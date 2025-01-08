# InventoryManagementSystem


## Project Overview

This project involves building a **Backend API for Inventory Management** using **Django** and **Django REST Framework (DRF)**. The API allows users to manage inventory items by performing CRUD (Create, Read, Update, Delete) operations, track inventory levels, and manage users who interact with the system with templates html and some js functions.

The goal of this project is to simulate a real-world inventory management system, such as one that might be used in a retail store. The project implements user authentication, role-based permissions, and the ability to track inventory changes over time.

## Functional Requirements

### 1. **Inventory Item Management (CRUD)**

- **Create**: Add new inventory items to the system.
- **Read**: View details of existing inventory items.
- **Update**: Modify the details of inventory items (e.g., price, quantity).
- **Delete**: Remove inventory items from the system.
  
Each inventory item includes the following attributes:
- `Name`: The name of the inventory item.
- `Description`: A detailed description of the item.
- `Quantity`: The number of available units.
- `Price`: The price of a single unit.
- `Category`: A classification or type of product.
- `Date Added`: The date when the item was added to inventory.
- `Last Updated`: The date when the item was last modified.

### 2. **User Management (CRUD)**

- **Create**: Register a new user with a unique username, email, and password.
- **Read**: View user details.
- **Update**: Modify user information (password, email).
- **Delete**: Remove users from the system.

Only authenticated users can manage inventory items (add, update, delete). Permissions ensure that users can only manage their own inventory.

### 3. **View Inventory Levels**

Create an endpoint to display the current inventory levels:
- Show available quantities of each inventory item.
- Implement filtering options such as:
  - `Category`
  - `Price Range`
  - `Low Stock` (items with a quantity below a defined threshold)

### 4. **Track Inventory Changes**

- Log changes made to inventory quantities, such as restocking or sales.
- Provide an endpoint to view the inventory change history for each item, including:
  - The date of change
  - The type of change (e.g., restock or sale)
  - The user who made the change

## Technical Requirements

### 1. **Database**

- Use **Django ORM** for database interaction.
- Define models for **Inventory Items** and **Users**.
- Ensure that each inventory item is associated with the user managing it.

### 2. **Authentication**

- Use **Django’s built-in authentication system** to handle user registration and login.
- Implement **JWT (JSON Web Token)** for token-based authentication to secure API access.
- Only authenticated users can manage inventory items.

### 3. **API Design**

- Use **Django Rest Framework (DRF)** to create API endpoints.
- Follow **RESTful principles** by using the appropriate HTTP methods (GET, POST, PUT, DELETE).
- Implement proper **error handling** and return appropriate HTTP status codes:
  - `404` for "not found"
  - `400` for "bad request"

### 4. **Pagination and Sorting**

- Implement **pagination** to handle large datasets efficiently when retrieving inventory items.
- Provide **sorting options**:
  - Sort by `Name`, `Quantity`, `Price`, or `Date Added`.

### 5. **Deployment**

- Deploy the API on **Heroku** or **PythonAnywhere**.
- Ensure the API is **secure**, **performant**, and accessible in the deployed environment.

## API Endpoints

### Authentication

- **POST** `/auth/login/`: User login and CRF token generation.
- **POST** `/auth/register/`: User registration.

### Inventory Items

- **POST** `/inventory/`: Create a new inventory item.
- **GET** `/inventory/`: Get a list of all inventory items (supports pagination, filtering, and sorting).
- **GET** `/inventory/{id}/`: Get detailed information of a specific inventory item.
- **PUT** `/inventory/{id}/`: Update an existing inventory item.
- **DELETE** `/inventory/{id}/`: Delete an inventory item.

### Inventory Changes

- **GET** `/inventory/{id}/changes/`: View the change history for a specific inventory item.

## Installation

### Prerequisites

1. Python 3.x
2. Django 3.x or later
3. Django REST Framework (DRF)
4. PostgreSQL (or any other relational database)
5. `pip` (Python package installer)

### Steps to Run the Project Locally

1. **Clone the repository:**

   ```bash
   git clone https://github.com/AymanMakram/InventoryManagementSystem.git
   cd InventoryManagementSystem