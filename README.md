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
│   └── basic-invoice.docx      # Word template with placeholders
├── client_invoice_data.xlsx    # Input file with all client data
├── send_email.py               # Script to send emails
├── generate_invoice.py         # Script to fill data and create .docx
├── convert_docx_to_pdf.py      # Batch converter for .docx → .pdf
├── main.py                     # Orchestrates the 3-phase process
└── README.md                   # This file
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

In `send_email.py`, use:
```python
server.login("your_email@example.com", "your_app_password")
```

(Use an App Password if using Gmail 2FA)

3. **Run the pipeline**

```bash
python main.py
```

---

## 📝 Input Excel Format (`client_invoice_data.xlsx`)

| Name       | Email                | Address         | Phone No.       | Service            | Amount | Discount | Due Date   |
|------------|----------------------|------------------|------------------|---------------------|--------|----------|------------|
| John Doe   | john@example.com     | 123 Street Name  | +91-9876543210   | Web Development     | 15000  | 1000     | 2025-06-25 |

---

## 📬 Output Example

Each client receives an email with their customized PDF invoice. File names are like:
```
Invoices/Invoice_101.pdf
Invoices/Invoice_102.pdf
...
```

---

## 📌 Author

**[Your Name]**  
GitHub: [codenoob7](https://github.com/yourusername)  
Email: shreyashpatel1001@gmail.com  
MIT License ©️ 2025

---

> ⭐ If this project helped you, please consider giving it a star on GitHub!
