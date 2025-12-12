Label Print – Manual & Access-Ready Crude Ticket Label Generator

A lightweight Python application designed to generate printable labels for crude oil tickets at the refinery.
The program currently runs in manual entry mode, allowing operators to type in transporter, ticket, lease, well, and product information.
It is also fully prepared for a future upgrade to Microsoft Access database mode, so the program can auto-populate label data directly from refinery Access tables.

This is one of the daily-use automation tools developed to streamline real-world operations at an oil refinery.

🚀 Features
✔ Manual Mode (default)

Enter data such as:

Transporter

Ticket #

Lease #

Well Name

Field Name

Lease Operator

API Gravity

The program outputs structured label data ready for printing.

✔ Access Mode (optional upgrade)

When enabled, the program:

Connects to a Microsoft Access .accdb database

Runs the query defined in config.ini

Auto-fills the same label fields
(Access mode can be enabled later — manual mode works today.)

✔ Config-Driven

Switch between modes without touching the code:

mode = manual


or

mode = access

📁 Folder Structure
label_print/
│
├── app.py                 # Main application
├── config.ini             # Manual vs Access mode configuration
├── README.md              # Project documentation
├── requirements.txt       # Python dependencies
│
├── templates/
│   └── label_template.txt # Optional print template
│
└── db/
    └── crude_data.accdb   # (Optional) Access database for future mode

⚙️ Configuration

The program behavior is controlled by config.ini.

Manual Mode (default)
[SETTINGS]
mode = manual

Access Mode (future optional)
[SETTINGS]
mode = access
db_path = db/crude_data.accdb
query = SELECT API, Well, Batch, Operator FROM Labels WHERE ID=1;

▶️ How to Run

Open a terminal or PowerShell

Navigate to the project folder:

cd label_print


Run:

python app.py


Follow the prompts for manual entry.

🔌 Access Mode Requirements (if enabled later)

Microsoft Access Database Engine (32-bit or 64-bit version must match Python)

pyodbc installed

A valid .accdb file located under db/

Once enabled, the program uses the query in config.ini to retrieve data.

🛠 Installation

Clone the repository:

git clone https://github.com/sbrooks25222/label_print.git


Install dependencies:

pip install -r requirements.txt

📦 Building an EXE (optional)

Once everything is working, you can package it using PyInstaller:

pyinstaller --onefile app.py


The EXE will appear inside a dist/ folder.

🧭 Purpose

This tool was built to:

Reduce manual errors when writing labels

Speed up crude oil ticket processing

Prepare for full automation via Access databases

Solve a real operational problem inside an active refinery

It demonstrates practical Python skills and automation capabilities.

🤝 Future Enhancements

Full Access database integration

CSV export for audit trails

Thermal label printer formatting

GUI (desktop app) for improved operator workflow
