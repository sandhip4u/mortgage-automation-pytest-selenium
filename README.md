
# 🏠 Mortgage Automation Testing Framework

This project is a real-world, GitHub-ready **Mortgage Loan Automation Test Suite** built using **Python, Selenium, and Pytest**.  
It simulates end-to-end scenarios such as login, mortgage application, payment calculation, document upload, and reporting.

---

## 🚀 Tech Stack

- 🐍 Python 3.x
- 🧪 Pytest
- 🕷 Selenium WebDriver
- 🧾 Pytest-HTML (for reporting)
- 🐳 (Optional) Docker
- 🛠️ (Optional) Jenkins / GitHub Actions

---

## 📂 Project Structure

```
mortgage_automation/
├── tests/                      # Test cases
│   ├── test_login.py
│   ├── test_mortgage_application.py
│   └── test_payment_validation.py
│
├── pages/                      # Page Object Model (POM) classes
│   ├── login_page.py
│   ├── home_page.py
│   ├── mortgage_form_page.py
│   └── upload_page.py
│
├── utils/                      # Config and WebDriver setup
│   ├── driver_setup.py
│   └── config.py
│
├── test_data/                  # Test data (JSON, Excel, etc.)
│   └── loan_data.json
│
├── reports/                    # Pytest HTML report output
│
├── conftest.py                 # Pytest fixtures
├── requirements.txt            # Python dependencies
├── pytest.ini                  # Pytest config
└── README.md                   # This file
```

---

## 🧪 Key Test Scenarios

✅ `test_login.py` – Validates user login using Page Object Model  
✅ `test_mortgage_application.py` – Fills mortgage loan form and submits it  
✅ `test_payment_validation.py` – Validates monthly EMI calculation  
✅ Document upload and confirmation (planned)

---

## ⚙️ Setup Instructions

### 1. 🔁 Clone the repository
```bash
git clone https://github.com/your-username/mortgage-automation-pytest-selenium.git
cd mortgage-automation-pytest-selenium
```

### 2. 🐍 Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
```

### 3. 📦 Install dependencies
```bash
pip install -r requirements.txt
```

### 4. 🚗 Run tests and generate report
```bash
pytest tests/ --html=reports/report.html
```

---

## 📊 Sample Report

The `pytest-html` plugin generates a user-friendly HTML report after each test run.  
Output: `reports/report.html`

---

## 🐳 Optional: Docker (Coming Soon)

Run tests inside a container:
```bash
docker build -t mortgage-tests .
docker run mortgage-tests
```

---

## 📦 CI/CD

- GitHub Actions or Jenkins pipeline can be integrated to run tests on every push or PR.

---

## 👨‍💻 Author

**Sandeep Vemula**  
Senior Consultant | SDET | Test Automation | Python | Selenium | Mortgage Domain  

---

## ⭐ License

This project is open-source and available under the MIT License.
"# mortgage-automation-pytest-selenium" 
