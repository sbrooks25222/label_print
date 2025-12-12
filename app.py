import configparser
import pyodbc

def load_config():
    config = configparser.ConfigParser()
    config.read("config.ini")
    return config

def get_manual_data():
    print("\n--- Manual Entry Mode ---")
    transporter = input("Transporter: ")
    ticket = input("Ticket#: ")
    lease_number = input("Lease#: ")
    well_name = input("Well Name: ")
    field_name = input("Field Name: ")
    lease_operator = input("Lease Operator: ")
    api_gravity = input("API Gravity: ")
    return {
        "Transporter": transporter,
        "Ticket": ticket,
        "Lease#": lease_number,
        "Well Name": well_name,
        "Field Name": field_name,
        "Lease Operator": lease_operator,
        "API Gravity": api_gravity
    }

def get_access_data(config):
    db_path = config["ACCESS"]["database_path"]
    table_name = config["ACCESS"]["table_name"]

    conn = pyodbc.connect(
        r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};"
        f"DBQ={db_path};"
    )
    cursor = conn.cursor()

    ticket_number = input("Enter Ticket# to look up: ")

    query = f"SELECT * FROM {table_name} WHERE Ticket = ?"
    cursor.execute(query, (ticket_number,))
    row = cursor.fetchone()

    if row:
        return {
            "Transporter": row.Transporter,
            "Ticket": row.Ticket,
            "Lease#": row.LeaseNumber,
            "Well Name": row.WellName,
            "Field Name": row.FieldName,
            "Lease Operator": row.LeaseOperator,
            "API Gravity": row.APIGravity
        }
    else:
        print("Ticket not found.")
        return None

def main():
    config = load_config()
    mode = config["SETTINGS"]["mode"]

    if mode == "manual":
        data = get_manual_data()
    elif mode == "access":
        data = get_access_data(config)
        if data is None:
            return
    else:
        print("Invalid mode in config.ini")
        return

    print("\n--- Label Data ---")
    for key, value in data.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()
