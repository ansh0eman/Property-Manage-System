import sqlite3
from rich.console import Console
from rich.prompt import Prompt

console = Console()

class Database:
    def __init__(self,db_file):
        self.db_file=db_file
        self.conn=sqlite3.connect(self.db_file)
        self.cur=self.conn.cursor()
    
    def create_landowner(self):
        self.cur.execute('''CREATE TABLE if not exists Landowner  (
        landowner_id INT PRIMARY KEY,
        first_name VARCHAR(50),
        last_name VARCHAR(50),
        email VARCHAR(100),
        phone_number VARCHAR(20)
    );''')
        self.conn.commit()
        
    def insert_into_landowner(self):
        id=Prompt.ask("Enter landowner id: ")
        fname=Prompt.ask("Enter first name: ")
        lname=Prompt.ask("Enter last name: ")
        email=Prompt.ask("Enter email: ")
        pno=Prompt.ask("Enter phone number")
        self.cur.execute('''INSERT INTO landowner (landowner_id, first_name, last_name, email, phone_number) VALUES (?, ?, ?, ?, ?);''', (id, fname, lname, email, pno))

    def create_property(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS Property (
        property_id INT PRIMARY KEY,
        property_type VARCHAR(50),
        address VARCHAR(255),
        city VARCHAR(100),
        state VARCHAR(100),
        postal_code VARCHAR(20),
        country VARCHAR(100),
        description VARCHAR(100),
        amenities VARCHAR(100),
        rental_status VARCHAR(50),
        ownership_status VARCHAR(50),
        landowner_id INT,
        FOREIGN KEY (landowner_id) REFERENCES Landowner(landowner_id)
        );''')
        self.conn.commit()

    def insert_into_property(self):
        property_id = Prompt.ask("Enter property id: ")
        property_type = Prompt.ask("Enter property type: ")
        address = Prompt.ask("Enter address: ")
        city = Prompt.ask("Enter city: ")
        state = Prompt.ask("Enter state: ")
        postal_code = Prompt.ask("Enter postal code: ")
        country = Prompt.ask("Enter country: ")
        description = Prompt.ask("Enter description: ")
        amenities = Prompt.ask("Enter amenities: ")
        rental_status = Prompt.ask("Enter rental status: ")
        ownership_status = Prompt.ask("Enter ownership status: ")
        landowner_id = Prompt.ask("Enter landowner id: ")
        self.cur.execute('''INSERT INTO Property (property_id, property_type, address, city, state, postal_code, country, description, amenities, rental_status, ownership_status, landowner_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);''', (property_id, property_type, address, city, state, postal_code, country, description, amenities, rental_status, ownership_status, landowner_id))
        self.conn.commit()
    
    def create_lease(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS Lease (
        lease_id INT PRIMARY KEY,
        property_id INT,
        start_date DATE,
        end_date DATE,
        rent_amount DECIMAL(10, 2),
        payment_schedule VARCHAR(50),
        lease_terms TEXT,
        FOREIGN KEY (property_id) REFERENCES Property(property_id)
        );''')
        self.conn.commit()

    def insert_into_lease(self):
        lease_id = Prompt.ask("Enter lease id: ")
        property_id = Prompt.ask("Enter property id: ")
        start_date = Prompt.ask("Enter start date (YYYY-MM-DD): ")
        end_date = Prompt.ask("Enter end date (YYYY-MM-DD): ")
        rent_amount = Prompt.ask("Enter rent amount: ")
        payment_schedule = Prompt.ask("Enter payment schedule: ")
        lease_terms = Prompt.ask("Enter lease terms: ")
        self.cur.execute('''INSERT INTO Lease (lease_id, property_id, start_date, end_date, rent_amount, payment_schedule, lease_terms) VALUES (?, ?, ?, ?, ?, ?, ?);''', (lease_id, property_id, start_date, end_date, rent_amount, payment_schedule, lease_terms))
        self.conn.commit()
        
    def create_tenant(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS Tenant (
            tenant_id INT PRIMARY KEY,
            first_name VARCHAR(50),
            last_name VARCHAR(50),
            email VARCHAR(100),
            phone_number VARCHAR(20),
            date_of_birth DATE,
            move_in_date DATE,
            move_out_date DATE,
            lease_id INT,
            FOREIGN KEY (lease_id) REFERENCES Lease(lease_id)
        );''')
        self.conn.commit()

    def insert_into_tenant(self):
        tenant_id = Prompt.ask("Enter tenant id: ")
        first_name = Prompt.ask("Enter first name: ")
        last_name = Prompt.ask("Enter lastname: ")
        email = Prompt.ask("Enter email: ")
        phone_number = Prompt.ask("Enter phone number: ")
        date_of_birth = Prompt.ask("Enter date of birth (YYYY-MM-DD): ")
        move_in_date = Prompt.ask("Enter move-in date (YYYY-MM-DD): ")
        move_out_date = Prompt.ask("Enter move-out date (YYYY-MM-DD): ")
        lease_id = Prompt.ask("Enter lease id: ")
        self.cur.execute('''INSERT INTO Tenant (tenant_id, first_name, last_name, email, phone_number, date_of_birth, move_in_date, move_out_date, lease_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);''', (tenant_id, first_name, last_name, email, phone_number, date_of_birth, move_in_date, move_out_date, lease_id))
        self.conn.commit()
        
    def create_rent_payment(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS RentPayment (
            payment_id INT PRIMARY KEY,
            lease_id INT,
            payment_date DATE,
            amount DECIMAL(10, 2),
            payment_method VARCHAR(50),
            transaction_id VARCHAR(100),
            FOREIGN KEY (lease_id) REFERENCES Lease(lease_id)
        );''')
        self.conn.commit()

    def insert_into_rent_payment(self):
        payment_id = Prompt.ask("Enter payment id: ")
        lease_id = Prompt.ask("Enter lease id: ")
        payment_date = Prompt.ask("Enter payment date (YYYY-MM-DD): ")
        amount = Prompt.ask("Enter amount: ")
        payment_method = Prompt.ask("Enter payment method: ")
        transaction_id = Prompt.ask("Enter transaction id: ")
        self.cur.execute('''INSERT INTO RentPayment (payment_id, lease_id, payment_date, amount, payment_method, transaction_id) VALUES (?, ?, ?, ?, ?, ?);''', (payment_id, lease_id, payment_date, amount, payment_method, transaction_id))
        self.conn.commit()
        
    def create_maintenance_request(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS MaintenanceRequest (
            request_id INT PRIMARY KEY,
            property_id INT,
            tenant_id INT,
            request_date DATE,
            description TEXT,
            status VARCHAR(50),
            assigned_to VARCHAR(100),
            FOREIGN KEY (property_id) REFERENCES Property(property_id),
            FOREIGN KEY (tenant_id) REFERENCES Tenant(tenant_id)
        );''')
        self.conn.commit()

    def insert_into_maintenance_request(self):
        request_id = Prompt.ask("Enter request id: ")
        property_id = Prompt.ask("Enter property id: ")
        tenant_id = Prompt.ask("Enter tenant id: ")
        request_date = Prompt.ask("Enter request date (YYYY-MM-DD): ")
        description = Prompt.ask("Enter description: ")
        status = Prompt.ask("Enter status: ")
        assigned_to = Prompt.ask("Enter assigned to: ")
        self.cur.execute('''INSERT INTO MaintenanceRequest (request_id, property_id, tenant_id, request_date, description, status, assigned_to) VALUES (?, ?, ?, ?, ?, ?, ?);''', (request_id, property_id, tenant_id, request_date, description, status, assigned_to))
        self.conn.commit()
        
    def create_document(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS Document (
            document_id INT PRIMARY KEY,
            property_id INT,
            document_type VARCHAR(50),
            document_name VARCHAR(255),
            upload_date DATE,
            file_path VARCHAR(255),
            FOREIGN KEY (property_id) REFERENCES Property(property_id)
        );''')
        self.conn.commit()

    def insert_into_document(self):
        document_id = Prompt.ask("Enter document id: ")
        property_id = Prompt.ask("Enter property id: ")
        document_type = Prompt.ask("Enter document type: ")
        document_name = Prompt.ask("Enter document name: ")
        upload_date = Prompt.ask("Enter upload date (YYYY-MM-DD): ")
        file_path = Prompt.ask("Enter file path: ")
        self.cur.execute('''INSERT INTO Document (document_id, property_id, document_type, document_name, upload_date, file_path) VALUES (?, ?, ?, ?, ?, ?);''', (document_id, property_id, document_type, document_name, upload_date, file_path))
        self.conn.commit()

    def calculate_rent_payment(self):
        lease_id = Prompt.ask("Enter lease id: ")
        start_date = Prompt.ask("Enter start date (YYYY-MM-DD): ")
        end_date = Prompt.ask("Enter end date (YYYY-MM-DD): ")

        self.cur.execute('''SELECT rent_amount, payment_schedule FROM Lease WHERE lease_id = ?;''', (lease_id,))
        row = self.cur.fetchone()
        if row:
            rent_amount, payment_schedule = row
            total_payment = 0

            # Calculate the duration of the lease in months
            start_year, start_month = map(int, start_date.split('-'))
            end_year, end_month = map(int, end_date.split('-'))
            total_months = (end_year - start_year) * 12 + (end_month - start_month) + 1

            # Calculate total payment based on payment schedule
            if payment_schedule == 'Monthly':
                total_payment = total_months * rent_amount
            elif payment_schedule == 'Quarterly':
                total_payment = (total_months // 3) * rent_amount
            elif payment_schedule == 'Annually':
                total_payment = (total_months // 12) * rent_amount

            return total_payment
        else:
            console.print("Lease not found.")
            return None

    def search_property(self):
        property_type = Prompt.ask("Enter property type (leave blank for any): ")
        city = Prompt.ask("Enter city (leave blank for any): ")
        state = Prompt.ask("Enter state (leave blank for any): ")

        query = "SELECT * FROM Property WHERE 1=1"
        params = []

        if property_type:
            query += " AND property_type = ?"
            params.append(property_type)
        if city:
            query += " AND city = ?"
            params.append(city)
        if state:
            query += " AND state = ?"
            params.append(state)

        self.cur.execute(query, tuple(params))
        properties = self.cur.fetchall()
        return properties

    def transfer_property_ownership(self):
        property_id = Prompt.ask("Enter property ID: ")
        new_landowner_id = Prompt.ask("Enter new landowner ID: ")

        try:
            self.cur.execute("UPDATE Property SET landowner_id = ? WHERE property_id = ?", (new_landowner_id, property_id))
            self.conn.commit()
            console.print("Property ownership transferred successfully.")
        except sqlite3.Error as e:
            console.print(f"Error transferring property ownership: {e}")

    def display_data(self):
        table_name = Prompt.ask("Enter table name: ")
        self.cur.execute(f"SELECT * FROM {table_name};")
        rows = self.cur.fetchall()
        if rows:
            console.print(f"Data from {table_name}:\n")
            console.table(rows)
        else:
            console.print(f"No data found in {table_name}.")

    def insert(self):
        self.insert_into_landowner()
        self.insert_into_property()
        self.insert_into_lease()
        self.insert_into_tenant()
        self.insert_into_maintenance_request()
        self.insert_into_rent_payment()
        self.create_document()
        

    def create(self):
        self.create_landowner()
        self.create_property()
        self.create_lease()
        self.create_tenant()
        self.create_rent_payment()
        self.create_maintenance_request()
        self.create_document()
        
    def menu(self):
        while True:
            console.print("\n=== Property Management System ===")
            console.print("1. Creation")
            console.print("2. Testing")
            console.print("3. Display")
            console.print("4. Exit")
            choice = int(Prompt.ask("Enter choice: "))

            if choice == 1:
                console.print("\n=== MENU ===")
                console.print("1. Insert Landowner")
                console.print("2. Insert Property")
                console.print("3. Insert Lease")
                console.print("4. Insert Tenant")
                console.print("5. Insert Rent Payment")
                console.print("6. Insert Maintenance Request")
                console.print("7. Insert Document")
                console.print("8. Exit")
                choice2 = int(Prompt.ask("Enter choice: "))

                if choice2 == 1:
                    self.create_landowner()
                    self.insert_into_landowner()
                elif choice2 == 2:
                    self.create_property()
                    self.insert_into_property()
                elif choice2 == 3:
                    self.create_lease()
                    self.insert_into_lease()
                elif choice2 == 4:
                    self.create_document()
                    self.insert_into_tenant()
                elif choice2 == 5:
                    self.create_rent_payment()
                    self.insert_into_rent_payment()
                elif choice2 == 6:
                    self.create_maintenance_request()
                    self.insert_into_maintenance_request()
                elif choice2 == 7:
                    self.create_document()
                    self.insert_into_document()
                elif choice2 == 8:
                    console.print("Exiting...")
                    break
                else:
                    console.print("Invalid choice")

            elif choice == 2:
                console.print("\n=== MENU-TESTING ===")
                console.print("1. Calculate rent payment")
                console.print("2. Search property")
                console.print("3. Transfer ownership")
                console.print("4. Exit")
                choice3 = int(Prompt.ask("Enter choice: "))

                if choice3 == 1:
                    total_payment = self.calculate_rent_payment()
                    if total_payment is not None:
                        console.print(f"Total rent payment: ${total_payment}")
                elif choice3 == 2:
                    properties = self.search_property()
                    if properties:
                        console.print("Properties found:")
                        console.table(properties)
                    else:
                        console.print("No properties found.")
                elif choice3 == 3:
                    self.transfer_property_ownership()
                elif choice3 == 4:
                    console.print("Exiting...")
                    break
                else:
                    console.print("Invalid choice")
            
            elif(choice==3):
                self.display_data()
            elif(choice==4):
                console.print("Exiting...")
                break
            else:
                console.print("Invalid choice")


def main():
    system = Database('PMS')
    system.menu()


if __name__ == "__main__":
    main()

#This program was made by Swastik Garg using the click module in Python for creating the command line interface. The code was also structured into classes and functions for better organization and maintainability. This program is designed to handle property management operations like insertion, deletion, updating, searching, and calculating rent payments. The program uses a SQLite database for storing and retrieving data.

#You can use this program to insert landowners, properties, leases, tenants, maintenance requests, rent payments, and documents into the database. You can also perform tests like calculating rent payments, searching for properties, and transferring property ownership. The program also includes a display data option to show all data in a table format.

#The code for this program can be found on GitHub at the following link: https://github.com/SwastikGarg/Property-Management-System.

#You can use this code as a starting point and modify it according to your requirements. Remember to replace the database connection string with your own SQLite database path.