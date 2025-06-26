import smtplib
import time
from email.message import EmailMessage
from fileinput import filename
from pathlib import Path

def send_invoice(to_email,client_name,invoice_path):
    msg = EmailMessage()
    msg['Subject'] = "Your Invoice from Shiv Shakti Pvt. Ltd."
    msg['From'] = 'shreyashpatel1001@gmail.com'
    msg['To'] = to_email

    msg.set_content(f"""
    Hi {client_name},

    Please find attached your invoice.

    Let me know if you have any questions.

    Best regards,
    Shiv Shakti Pvt. Ltd.
    """)

    with open(invoice_path, 'rb') as invoice:
        file_data = invoice.read()
        msg.add_attachment(file_data, maintype='application', subtype='pdf',filename=Path(invoice_path).name)

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login("shreyashpatel1001@gmail.com","fvcu vyax jldg gnlj")
        server.send_message(msg)

    print(f'Message Sent Successfully to {client_name}.')
    with open("send_log.csv", "a") as log:
        log.write(f"{to_email}, Sent, {invoice_path}\n")

    time.sleep(2)