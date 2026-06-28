# User Management Application

A desktop application for managing users, roles, and permissions, built with Python and SQLite. The application implements JWT-based authentication, role-based access control (RBAC), and a clean three-layer architecture to ensure maintainability, scalability, and security.

## 🚀 Features

* **JWT Authentication**: Secure token-based authentication using JSON Web Tokens (JWT). Tokens are generated upon successful login and validated before every protected operation.
* **Role-Based Access Control (RBAC)**: Supports administrator and standard user roles with authorization enforced at the business layer.
* **User Management**: Administrators can create, activate, deactivate, and manage user accounts.
* **Secure Password Storage**: Passwords are hashed using the MD5 algorithm before being stored in the database.
* **Three-Layer Architecture**: Clear separation between Presentation Layer, Business Layer, and Data Access Layer.
* **Performance Logging**: Decorator-based performance monitoring for tracking execution times across application layers.
* **Database Persistence**: User information is stored and managed using SQLite.
* **Unit Testing**: Comprehensive test coverage for business logic, data access operations, and presentation components.

## 🛠️ Technologies Used

* **Programming Language**: Python 3.11
* **Database**: SQLite3
* **GUI Framework**: Tkinter
* **Authentication**: PyJWT
* **Testing Frameworks**: unittest, pytest
* **Libraries and Tools**:

  * `tkinter`: Builds the graphical user interface.
  * `sqlite3`: Handles database operations and data persistence.
  * `PyJWT`: Generates and validates JWT tokens.
  * `hashlib`: Hashes user passwords before storage.
  * `unittest`: Provides structured unit testing.
  * `pytest`: Supports advanced test execution and reporting.
  * `decorators`: Logs performance metrics and execution times.
  * `Response Class`: Standardizes responses between application layers.

## 📂 Project Structure

```text
UserManagementApplication/
├── BusinessLayer/
│   ├── jwt_service.py
│   └── user_business_logic.py
│
├── Common/
│   ├── Decorators/
│   │   └── performance_logger.py
│   ├── Entities/
│   │   └── user.py
│   └── ResponseModels/
│       └── response.py
│
├── DataAccessLayer/
│   └── user_data_access.py
│
├── PresentationLayer/
│   ├── Frames/
│   │   ├── home.py
│   │   ├── login.py
│   │   ├── register.py
│   │   └── user_management.py
│   └── main_view.py
│
└── Tests/
    ├── business_layer_tests/
    ├── data_access_layer_tests/
    └── presentation_layer_tests/
```

## 🔐 Authentication Flow

1. User enters login credentials.
2. Credentials are validated against stored user data.
3. A JWT token is generated and signed using a secret key.
4. The token is stored for the active session.
5. Protected operations pass the token to the Business Layer.
6. The Business Layer independently validates and decodes the token.
7. If the token is invalid or expired, access is denied and the user is redirected to the login page.

## 🚀 Getting Started

### Prerequisites

* Python 3.6 or later
* pip package manager

### Installation

1. Clone the repository:

```bash
git clone https://github.com/Tarantinum/UserManagmentApplication.git
cd UserManagmentApplication
```

2. Install required dependencies:

```bash
pip install PyJWT
```

### Running the Application

```bash
python main.py
```

### Running Tests

```bash
pytest
```

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch:

```bash
git checkout -b feature/YourFeatureName
```

3. Commit your changes:

```bash
git commit -m "Add feature description"
```

4. Push your branch:

```bash
git push origin feature/YourFeatureName
```

5. Open a Pull Request.

## 📧 Contact

If you have any questions or suggestions, feel free to contact me:

* **Email**: [tatabhra@gmail.com](mailto:tatabhra@gmail.com)
* **LinkedIn**: https://linkedin.com/in/taranom-bahiraee-85a58232b

---

⭐ If you found this project helpful, consider giving it a star on GitHub. Your support is greatly appreciated!
