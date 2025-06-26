import pandas as pd
from generate_invoice import *
from send_email import send_invoice

if __name__ == '__main__':
    client_data = pd.read_excel('client_invoice_data.xlsx')
    client_data["Invoice No"] = range(101, 101 + len(client_data))

    for index, client in client_data.iterrows():
        fill_the_data(client['Name'], client['Address'], client['Phone No.'], client['Email'], client['Due Date'],
                      client['Service'], client['Amount'], client['Discount'], client['Invoice No'])

    batch_convert_docx2pdf('Invoices', 'Invoices')

    for index, client in client_data.iterrows():
        send_invoice(client['Email'], client['Name'], f"Invoices/Invoice_{client['Invoice No']}.pdf")