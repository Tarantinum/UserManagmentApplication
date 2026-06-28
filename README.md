# User Management Application

A desktop application for managing users, roles, and permissions — built with Python and SQLite, featuring JWT-based authentication and role-based access control.

---

## 🚀 Features

- **JWT Authentication**: Secure token-based authentication generated on login and verified on every protected action.
- **Role-Based Access Control**: Admin and standard user roles with enforced access at the business layer.
- **User Management**: Admins can activate and deactivate user accounts.
- **Secure Passwords**: All passwords hashed using MD5 before storage.
- **3-Layer Architecture**: Clean separation between Presentation, Business, and Data Access layers.
- **Performance Logging**: Decorator-based logging across all layers.

---

## 🛠️ Technologies Used

- **Language**: Python 3.11
- **GUI**: Tkinter
- **Database**: SQLite3
- **Authentication**: PyJWT
- **Testing**: unittest, pytest
- **Other**: hashlib, decorators, Response model pattern

---

## 📂 Project Structure

```text
UserManagmentApplication/

├── BusinessLayer/
│   ├── jwt_service.py
│   └── user_business_logic.py

├── Common/
│   ├── Decorators/
│   │   └── performance_logger.py
│   ├── Entities/
│   │   └── user.py
│   └── ResponseModels/
│       └── response.py

├── DataAccessLayer/
│   └── user_data_access.py

├── PeresntationLayer/
│   ├── Frames/
│   │   ├── home.py
│   │   ├── login.py
│   │   ├── register.py
│   │   └── user_management.py
│   └── main_view.py

└── Tests/
    ├── business_layer_tests/
    ├── data_access_layer_tests/
    └── presentation_layer_tests/
```

---

## 🔐 Authentication Flow

Login → credentials verified → JWT token generated (signed with secret key)

→ token stored in session

→ passed to BusinessLayer on every action

→ BusinessLayer decodes and verifies token independently

→ expired or invalid token

→ user redirected to login

---

## 🚀 Getting Started

### Prerequisites

- Python 3.6 or later
- pip

### Installation

#### 📥 Clone the Repository

```bash
git clone https://github.com/Tarantinum/UserManagmentApplication.git
```

#### 📂 Navigate to the Project Directory

```bash
cd UserManagmentApplication
```

#### 📦 Install Dependencies

```bash
pip install PyJWT
```

---

## 🖥️ Usage

### ▶️ Running the Application

```bash
python main.py
```

---

### Running Tests
Run the test suite to ensure everything is working:
```bash
pytest
```

--- 
## 🤝 Contributing
I welcome contributions to enhance the application! To contribute:
1. Fork the repository.
2. Create a new branch for your feature or fix:
   ```bash
   git checkout -b feature/YourFeatureName
   ```
3. Make your changes and commit them:
   ```bash
   git commit -m "Add feature description"
   ```
4. Push to your branch:
   ```bash
   git push origin feature/YourFeatureName
   ```
5. Open a pull request on GitHub.
---

## 📧 Contact

- **Email**: tatabhra@gmail.com
- **LinkedIn**: [Taranom Bahiraee](https://linkedin.com/in/taranom-bahiraee-85a58232b)

---
Thank you for checking out this project! If you found it helpful, please consider giving it a ⭐ on GitHub. Your support means a lot! 💖
