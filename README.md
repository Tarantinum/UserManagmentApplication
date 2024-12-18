# User Management Application

Welcome to the **User Management Application** repository! This project provides a comprehensive solution for managing user data, roles, and permissions effectively, offering both a user-friendly interface and robust backend functionality.

## 🚀 Features
- **User Management**: Create, update, and delete user accounts effortlessly.
- **Role-Based Access Control (RBAC)**: Assign and manage roles with granular permissions.
- **Search and Filter**: Quickly locate user records through intuitive search and filter options.
- **Secure Authentication**: Ensures data security through industry-standard practices.
- **Responsive Design**: Optimized for a seamless experience across devices.

## 🛠️ Technologies Used
- **Programming Language**: Python
- **Database**: SQLite
- **Frontend**: Tkinter
- **Tools and Libraries**: 
  - `tkinter`: For building the graphical user interface, including frames, buttons, labels, and user input fields.
  - `sqlite3`: For database operations, handling user data persistence and queries.
  - `unittest`: For testing the application's components and functionality.
  - `hashlib`: For password hashing using the MD5 algorithm.
  - `os`: For file and path operations, especially in test database management.
  - `pytest`: For running and managing tests with detailed reporting.
  - `decorators`: For performance logging and monitoring function execution.
  - `Response class`: For standardizing API responses across the application layers.
  - `unittest`: A built-in Python testing framework used for writing and running test cases. It helps ensure the correctness of individual components of the application. Features include:
    - **Test Discovery**: Automatically identifies test methods.
    - **Assertions**: Provides methods like `assertEqual`, `assertIsNotNone`, and `assertTrue` to validate test conditions.
    - **Fixtures**: Includes `setUp` and `tearDown` for initializing and cleaning up resources before and after each test.
    - **Test Organization**: Enables grouping tests into test classes for better modularity.



## 📂 Project Structure
```
UserManagementApplication/
├── BusinessLayer/
│   └── user_business_logic.py
├── Common/
│   └── Entities/
│       └── user.py
├── DataAccessLayer/
│   └── user_data_access.py
├── PresentationLayer/
│   └── Frames/
│       ├── home.py
│       ├── login.py
│       └── user_management.py
└── Tests/
    ├── business_layer_tests/
    │   └── test_user_business_logic.py
    ├── data_access_layer_tests/
    │   └── test_user_data_access.py
    └── presentation_layer_tests/
        └── test_frames.py
```

## 🚀 Getting Started

### Prerequisites
1. Install Python (version 3.6 or later).
2. Ensure `sqlite3` is installed (comes with Python).

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Tarantinum/UserManagmentApplication.git
   ```
2. Navigate to the project directory:
   ```bash
   cd UserManagmentApplication
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt  # If applicable
   ```

### Running the Application
Run the application using the following command:
```bash
python main.py
```

### Running Tests
Run the test suite to ensure everything is working:
```bash
pytest
```

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

## 📧 Contact
If you have any questions or suggestions, feel free to contact me:  
- **Email**: tatabhra@gmail.com  
- **LinkedIn**: [Taranom Bahiraee](https://linkedin.com/in/taranom-bahiraee-85a58232b)


---
Thank you for checking out this project! If you found it helpful, please consider giving it a ⭐ on GitHub. Your support means a lot! 💖
