from flask import Flask, render_template, request, send_file
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import os

app = Flask(__name__)

def generate_pdf(name, account):
    filename = "statement.pdf"
    doc = SimpleDocTemplate(filename)
    styles = getSampleStyleSheet()

    elements = []
    elements.append(Paragraph("Bank Statement", styles['Title']))
    elements.append(Spacer(1, 12))
    elements.append(Paragraph(f"Name: {name}", styles['Normal']))
    elements.append(Paragraph(f"Account No: {account}", styles['Normal']))

    doc.build(elements)
    return filename

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    name = request.form['name']
    account = request.form['account']

    file = generate_pdf(name, account)
    return send_file(file, as_attachment=True)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
