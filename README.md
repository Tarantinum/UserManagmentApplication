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
UserManagementApplication/

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

├── PresentationLayer/
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

## 🧪 Testing

### Run Tests

```bash
pytest
```

---

## 📧 Contact

- **Email**: tatabhra@gmail.com
- **LinkedIn**: [Taranom Bahiraee](https://linkedin.com/in/taranom-bahiraee-85a58232b)

---

If you found this project helpful, consider giving it a ⭐ on GitHub!
