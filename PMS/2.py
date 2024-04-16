import sqlite3
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt
from rich.text import Text
from rich import print

console = Console()

class Database:
    def __init__(self,PMS):
        self.PMS=PMS
        self.conn=sqlite3.connect(self.PMS)
        self.cur=self.conn.cursor()
        self.logged_in = False
        self.console=Console()
        
    def input_sample_data(self):
        # Sample data
        self.create()
        landowner_data = [
            (1, 'John', 'Doe', 'john.doe@example.com', '+1234567890'),
            (2, 'Jane', 'Smith', 'jane.smith@example.com', '+1987654321')
        ]

        property_data = [
            (1, 'House', '123 Main St', 'Springfield', 'IL', '62701', 'USA', 'Cozy 2-bedroom house', 'Furnished, parking', 'Occupied', 'Owned', 1),
            (2, 'Apartment', '456 Elm St', 'Riverside', 'CA', '92501', 'USA', 'Modern 1-bedroom apartment', 'Gym, pool', 'Vacant', 'Owned', 2)
        ]

        lease_data = [
            (1, 1, '2024-01-01', '2025-01-01', 1200.00, 'Monthly', 'No pets allowed. No smoking.'),
            (2, 2, '2024-02-01', '2024-08-01', 1500.00, 'Bi-weekly', 'Pets allowed with additional fee.')
        ]

        tenant_data = [
            (1, 'Michael', 'Johnson', 'michael.j@example.com', '+1122334455', '1990-05-15', '2024-01-01', '2025-01-01', 1),
            (2, 'Emily', 'Brown', 'emily.b@example.com', '+1567890123', '1985-08-20', '2024-02-01', '2024-08-01', 2)
        ]

        rent_payment_data = [
            (1, 1, '2024-01-05', 1200.00, 'Credit Card', 'CC123456789'),
            (2, 2, '2024-02-15', 750.00, 'Bank Transfer', 'BT987654321')
        ]

        maintenance_request_data = [
            (1, 1, 1, '2024-03-10', 'Leaky faucet in the kitchen', 'Pending', 'Plumber'),
            (2, 2, 2, '2024-04-01', 'Broken light fixture in the living room', 'In Progress', 'Maintenance Staff')
        ]

        document_data = [
            (1, 1, 'Lease Agreement', 'Lease_123', '2024-01-01', '/documents/lease_123.pdf'),
            (2, 2, 'Tenant Application', 'Application_456', '2024-02-01', '/documents/application_456.pdf')
        ]

        # Inserting sample data into the Landowner table
        self.cur.executemany('''INSERT INTO Landowner (landowner_id, first_name, last_name, email, phone_number) VALUES (?, ?, ?, ?, ?);''', landowner_data)

        # Inserting sample data into the Property table
        self.cur.executemany('''INSERT INTO Property (property_id, property_type, address, city, state, postal_code, country, description, amenities, rental_status, ownership_status, landowner_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);''', property_data)

        # Inserting sample data into the Lease table
        self.cur.executemany('''INSERT INTO Lease (lease_id, property_id, start_date, end_date, rent_amount, payment_schedule, lease_terms) VALUES (?, ?, ?, ?, ?, ?, ?);''', lease_data)

        # Inserting sample data into the Tenant table
        self.cur.executemany('''INSERT INTO Tenant (tenant_id, first_name, last_name, email, phone_number, date_of_birth, move_in_date, move_out_date, lease_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);''', tenant_data)

        # Inserting sample data into the RentPayment table
        self.cur.executemany('''INSERT INTO RentPayment (payment_id, lease_id, payment_date, amount, payment_method, transaction_id) VALUES (?, ?, ?, ?, ?, ?);''', rent_payment_data)

        # Inserting sample data into the MaintenanceRequest table
        self.cur.executemany('''INSERT INTO MaintenanceRequest (request_id, property_id, tenant_id, request_date, description, status, assigned_to) VALUES (?, ?, ?, ?, ?, ?, ?);''', maintenance_request_data)

        # Inserting sample data into the Document table
        self.cur.executemany('''INSERT INTO Document (document_id, property_id, document_type, document_name, upload_date, file_path) VALUES (?, ?, ?, ?, ?, ?);''', document_data)
                
        landowner_data_additional = [
            (3, 'Sarah', 'Johnson', 'sarah.j@example.com', '+1122334455'),
            (4, 'Robert', 'Williams', 'robert.w@example.com', '+1567890123')
        ]

        property_data_additional = [
            (3, 'Condo', '789 Oak St', 'Hill Valley', 'CA', '95420', 'USA', 'Spacious 3-bedroom condo', 'Balcony, parking', 'Occupied', 'Owned', 3),
            (4, 'Townhouse', '101 Pine St', 'Springfield', 'IL', '62702', 'USA', 'Charming 2-bedroom townhouse', 'Garden, garage', 'Vacant', 'Owned', 4),
            (5, 'Apartment', '456 Elm St', 'Rivertown', 'NY', '12345', 'USA', 'Modern 2-bedroom apartment', 'Fitness center, rooftop terrace', 'Occupied', 'Owned', 1),
            (6, 'House', '789 Willow Ave', 'Mountain View', 'CA', '94040', 'USA', 'Spacious 4-bedroom house', 'Garden, pool', 'Vacant', 'Owned', 2)
        ]

        lease_data_additional = [
            (3, 3, '2024-03-01', '2025-03-01', 1800.00, 'Monthly', 'No smoking allowed.'),
            (4, 4, '2024-04-01', '2024-10-01', 2000.00, 'Monthly', 'Pets allowed with deposit.')
        ]

        tenant_data_additional = [
            (3, 'David', 'Miller', 'david.m@example.com', '+1987654321', '1992-07-20', '2024-03-01', '2025-03-01', 3),
            (4, 'Jessica', 'Taylor', 'jessica.t@example.com', '+1234567890', '1988-04-10', '2024-04-01', '2024-10-01', 4)
        ]

        rent_payment_data_additional = [
            (3, 3, '2024-03-05', 1800.00, 'Bank Transfer', 'BT1122334455'),
            (4, 4, '2024-04-15', 2000.00, 'Credit Card', 'CC987654321')
        ]

        maintenance_request_data_additional = [
            (3, 3, 3, '2024-04-10', 'Heating system not working', 'Pending', 'HVAC Technician'),
            (4, 4, 4, '2024-04-20', 'Leaky roof in the bedroom', 'In Progress', 'Roofing Contractor')
        ]

        document_data_additional = [
            (3, 3, 'Lease Agreement', 'Lease_789', '2024-03-01', '/documents/lease_789.pdf'),
            (4, 4, 'Tenant Application', 'Application_101', '2024-04-01', '/documents/application_101.pdf'),
            (5, 5, 'Insurance Certificate', 'Insurance_456', '2024-03-15', '/documents/insurance_456.pdf'),
            (6, 6, 'Property Inspection Report', 'Inspection_789', '2024-04-15', '/documents/inspection_789.pdf')

        ]

        # Inserting additional sample data into the Landowner table
        self.cur.executemany('''INSERT INTO Landowner (landowner_id, first_name, last_name, email, phone_number) VALUES (?, ?, ?, ?, ?);''', landowner_data_additional)

        # Inserting additional sample data into the Property table
        self.cur.executemany('''INSERT INTO Property (property_id, property_type, address, city, state, postal_code, country, description, amenities, rental_status, ownership_status, landowner_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);''', property_data_additional)

        # Inserting additional sample data into the Lease table
        self.cur.executemany('''INSERT INTO Lease (lease_id, property_id, start_date, end_date, rent_amount, payment_schedule, lease_terms) VALUES (?, ?, ?, ?, ?, ?, ?);''', lease_data_additional)

        # Inserting additional sample data into the Tenant table
        self.cur.executemany('''INSERT INTO Tenant (tenant_id, first_name, last_name, email, phone_number, date_of_birth, move_in_date, move_out_date, lease_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);''', tenant_data_additional)

        # Inserting additional sample data into the RentPayment table
        self.cur.executemany('''INSERT INTO RentPayment (payment_id, lease_id, payment_date, amount, payment_method, transaction_id) VALUES (?, ?, ?, ?, ?, ?);''', rent_payment_data_additional)

        # Inserting additional sample data into the MaintenanceRequest table
        self.cur.executemany('''INSERT INTO MaintenanceRequest (request_id, property_id, tenant_id, request_date, description, status, assigned_to) VALUES (?, ?, ?, ?, ?, ?, ?);''', maintenance_request_data_additional)

        # Inserting additional sample data into the Document table
        self.cur.executemany('''INSERT INTO Document (document_id, property_id, document_type, document_name, upload_date, file_path) VALUES (?, ?, ?, ?, ?, ?);''', document_data_additional)


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
        id=input('enter landowner id: ')
        fname=input('enter first name: ')
        lname=input('enter last name: ')
        email=input('enter email: ')
        pno=input('enter phone number')
        self.cur.execute('''INSERT INTO Landowner (landowner_id, first_name, last_name, email, phone_number) VALUES (?, ?, ?, ?, ?);''', (id, fname, lname, email, pno))

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
        property_id = input('Enter property id: ')
        property_type = input('Enter property type: ')
        address = input('Enter address: ')
        city = input('Enter city: ')
        state = input('Enter state: ')
        postal_code = input('Enter postal code: ')
        country = input('Enter country: ')
        description = input('Enter description: ')
        amenities = input('Enter amenities: ')
        rental_status = input('Enter rental status: ')
        ownership_status = input('Enter ownership status: ')
        landowner_id = input('Enter landowner id: ')
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
        lease_id = input('Enter lease id: ')
        property_id = input('Enter property id: ')
        start_date = input('Enter start date (YYYY-MM-DD): ')
        end_date = input('Enter end date (YYYY-MM-DD): ')
        rent_amount = input('Enter rent amount: ')
        payment_schedule = input('Enter payment schedule: ')
        lease_terms = input('Enter lease terms: ')
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
        tenant_id = input('Enter tenant id: ')
        first_name = input('Enter first name: ')
        last_name = input('Enter last name: ')
        email = input('Enter email: ')
        phone_number = input('Enter phone number: ')
        date_of_birth = input('Enter date of birth (YYYY-MM-DD): ')
        move_in_date = input('Enter move-in date (YYYY-MM-DD): ')
        move_out_date = input('Enter move-out date (YYYY-MM-DD): ')
        lease_id = input('Enter lease id: ')
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
        payment_id = input('Enter payment id: ')
        lease_id = input('Enter lease id: ')
        payment_date = input('Enter payment date (YYYY-MM-DD): ')
        amount = input('Enter amount: ')
        payment_method = input('Enter payment method: ')
        transaction_id = input('Enter transaction id: ')
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
        request_id = input('Enter request id: ')
        property_id = input('Enter property id: ')
        tenant_id = input('Enter tenant id: ')
        request_date = input('Enter request date (YYYY-MM-DD): ')
        description = input('Enter description: ')
        status = input('Enter status: ')
        assigned_to = input('Enter assigned to: ')
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
        document_id = input('Enter document id: ')
        property_id = input('Enter property id: ')
        document_type = input('Enter document type: ')
        document_name = input('Enter document name: ')
        upload_date = input('Enter upload date (YYYY-MM-DD): ')
        file_path = input('Enter file path: ')
        self.cur.execute('''INSERT INTO Document (document_id, property_id, document_type, document_name, upload_date, file_path) VALUES (?, ?, ?, ?, ?, ?);''', (document_id, property_id, document_type, document_name, upload_date, file_path))
        self.conn.commit()

    def calculate_rent_payment(self):
        lease_id = input("Enter lease id: ")

        # Fetch the lease information from the database
        self.cur.execute('''SELECT rent_amount, payment_schedule, start_date, end_date FROM Lease WHERE lease_id = ?;''', (lease_id,))
        row = self.cur.fetchone()

        if row:
            rent_amount, payment_schedule, start_date, end_date = row
            total_payment = 0
            
            # Calculate the duration of the lease in months
            start_year, start_month, start_day = map(int, start_date.split('-'))
            end_year, end_month, end_day = map(int, end_date.split('-'))
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
            print("Lease not found.")
            return None

        
    
    
    def delete_existing_property(self):
        property_id = input("Enter property ID to delete: ")
        try:
            self.cur.execute("DELETE FROM Property WHERE property_id = ?", (property_id,))
            self.conn.commit()
            print("Property deleted successfully.")
        except sqlite3.Error as e:
            print("Error deleting property:", e)

    def transfer_property_ownership(self):
        property_id = input("Enter property ID: ")
        new_landowner_id = input("Enter new landowner ID: ")

        try:
            self.cur.execute("UPDATE Property SET landowner_id = ? WHERE property_id = ?", (new_landowner_id, property_id))
            self.conn.commit()
            print("Property ownership transferred successfully.")
        except sqlite3.Error as e:
            print("Error transferring property ownership:", e)

    def display_data(self):
        table_name = input("Enter table name: ")
        self.cur.execute(f"SELECT * FROM {table_name};")
        rows = self.cur.fetchall()
        if rows:
            print(f"Data from {table_name}:")
            for row in rows:
                print(row)
        else:
            print(f"No data found in {table_name}.")
            
    def login(self):
        username = input("Enter username: ")
        password = input("Enter password: ")

        # Check if username and password are correct (you can implement your own authentication logic)
        if username == "admin" and password == "admin":
            print("Login successful!")
            self.logged_in = True
        else:
            print("Invalid username or password. Please try again.")

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
        
    def view_existing_property(self):
        landowner_id = input("Enter landowner ID: ")
        self.cur.execute('''SELECT * FROM Property WHERE landowner_id = ?;''', (landowner_id,))
        properties = self.cur.fetchall()
        if properties:
            print("Existing properties:")
            for prop in properties:
                print(prop)
        else:
            print("No properties found for this landowner.")
            
    def view_tenant_details(self):
        landowner_id = input("Enter landowner ID: ")
        # Retrieve properties owned by the specified landowner
        self.cur.execute('''SELECT property_id FROM Property WHERE landowner_id = ?;''', (landowner_id,))
        owned_properties = self.cur.fetchall()
        
        if owned_properties:
            # Extract property IDs from the fetched properties
            property_ids = [prop[0] for prop in owned_properties]
            # Query tenants associated with the owned properties
            self.cur.execute('''SELECT * FROM Tenant WHERE lease_id IN (SELECT lease_id FROM Lease WHERE property_id IN ({seq}))'''.format(seq=','.join(['?']*len(property_ids))), property_ids)
            tenants = self.cur.fetchall()
            
            if tenants:
                print("Tenant details for properties owned by landowner ID", landowner_id, ":")
                for tenant in tenants:
                    print(tenant)
            else:
                print("No tenants found for properties owned by landowner ID", landowner_id)
        else:
            print("No properties found for landowner ID", landowner_id)
            
    def view_documents(self):
        landowner_id = input("Enter landowner ID: ")
        # Retrieve properties owned by the specified landowner
        self.cur.execute('''SELECT property_id FROM Property WHERE landowner_id = ?;''', (landowner_id,))
        owned_properties = self.cur.fetchall()
        
        if owned_properties:
            # Extract property IDs from the fetched properties
            property_ids = [prop[0] for prop in owned_properties]
            # Query documents associated with the owned properties
            self.cur.execute('''SELECT * FROM Document WHERE property_id IN ({seq})'''.format(seq=','.join(['?']*len(property_ids))), property_ids)
            documents = self.cur.fetchall()
            
            if documents:
                print("Documents for properties owned by landowner ID", landowner_id, ":")
                for doc in documents:
                    print(doc)
            else:
                print("No documents found for properties owned by landowner ID", landowner_id)
        else:
            print("No properties found for landowner ID", landowner_id)
            
    def view_documents_tenant(self):
        tenant_id = input("Enter tenant ID: ")
        
        # Check if there are any leases associated with the tenant ID
        self.cur.execute('''SELECT property_id FROM Lease WHERE tenant_id = ?;''', (tenant_id,))
        leased_properties = self.cur.fetchall()
        
        if leased_properties:
            # Extract property IDs from the leased properties
            property_ids = [prop[0] for prop in leased_properties]
            # Query documents associated with the leased properties
            self.cur.execute('''SELECT * FROM Document WHERE property_id IN ({seq})'''.format(seq=','.join(['?']*len(property_ids))), property_ids)
            documents = self.cur.fetchall()
            
            if documents:
                print("Documents for properties leased by tenant ID", tenant_id, ":")
                for doc in documents:
                    print(doc)
            else:
                print("No documents found for properties leased by tenant ID", tenant_id)
        else:
            print("No properties leased by tenant ID", tenant_id)

               
    def calculate_rent_payment_landowner(self):
        landowner_id = input("Enter landowner ID: ")
        
        # Retrieve properties owned by the specified landowner
        self.cur.execute('''SELECT property_id FROM Property WHERE landowner_id = ?;''', (landowner_id,))
        owned_properties = self.cur.fetchall()

        if owned_properties:
            total_payment_landowner = 0
            for property_id in owned_properties:
                property_id = property_id[0]
                
                # Retrieve lease information for the property
                self.cur.execute('''SELECT lease_id, start_date, end_date, rent_amount, payment_schedule FROM Lease WHERE property_id = ?;''', (property_id,))
                lease_info = self.cur.fetchone()

                if lease_info:
                    lease_id, start_date, end_date, rent_amount, payment_schedule = lease_info
                    # Calculate the duration of the lease in months
                    start_year, start_month, start_day = map(int, start_date.split('-'))
                    end_year, end_month, end_day = map(int, end_date.split('-'))
                    total_months = (end_year - start_year) * 12 + (end_month - start_month) + 1

                    # Calculate total payment based on payment schedule
                    if payment_schedule == 'Monthly':
                        total_payment_landowner += total_months * rent_amount
                    elif payment_schedule == 'Quarterly':
                        total_payment_landowner += (total_months // 3) * rent_amount
                    elif payment_schedule == 'Annually':
                        total_payment_landowner += (total_months // 12) * rent_amount

            print(f"Total rent payment for properties owned by landowner ID {landowner_id}: ${total_payment_landowner}")
        else:
            print(f"No properties found for landowner ID {landowner_id}")

    def search_property(self):
        property_type = input("Enter property type (leave blank for any): ")
        city = input("Enter city (leave blank for any): ")
        state = input("Enter state (leave blank for any): ")

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
        
        if properties:
            print("Properties matching the search criteria:")
            for prop in properties:
                print(prop)
        else:
            print("No properties found matching the search criteria.")



    def delete_existing_property(self):
        property_id = input("Enter property ID to delete: ")
        try:
            self.cur.execute("DELETE FROM Property WHERE property_id = ?", (property_id,))
            self.conn.commit()
            print("Property deleted successfully.")
        except sqlite3.Error as e:
            print("Error deleting property:", e)
            
    def landowner_login(self):
        console.print(Panel("=== Landowner Login ===", style="bold magenta"))
        print("1. Existing User")
        print("2. New User")
        print()
        title = Text("Enter your choice: ", style="italic")
        console.print(title, style="white")
        choice=input("")

        if choice == '1':
            existing_username = input("Enter your username: ")
            existing_password = input("Enter your password: ")
            # Check if the username and password exist in the database
            # Implement your authentication logic here

            # For demonstration purposes, let's assume a simple hardcoded check
            if existing_username == "existing_user" and existing_password == "password":
                print("Login successful!")
                self.logged_in = True
            else:
                print("Invalid username or password. Please try again.")
        elif choice == '2':
            self.insert_into_landowner()
            new_username = input("Enter a new username: ")
            new_password = input("Enter a new password: ")
            # Store the new username and password in the database
            # Implement your user creation logic here

            # For demonstration purposes, let's assume we successfully create a new user
            print("New user created successfully!")
            self.logged_in = True
        else:
            print("Invalid choice. Please try again.")
        console.print("\n[bold blue]=========================================================[/bold blue]\n")

    def mainmenu(self):
            console.print(Panel("=== Property Management System ===", style="bold magenta"))
            print("1. Landowner")
            print("2. Tenant")
            print("3. Admin")
            choice = int(input("Enter choice: "))
            if choice == 1:
                self.landowner_menu()
            elif choice == 2:
                self.tenant_menu()
            elif choice == 3:
                self.admin_menu()
            console.print("\n[bold blue]=========================================================[/bold blue]\n")
                    
    def landowner_menu(self):
        self.console.print("Welcome Landowner",style="bold magenta")
        if not self.logged_in:
                print("Please login first.")
                self.landowner_login()
                if not self.logged_in:
                    return
        while True:
            self.console.print(Panel("=== Landowner Menu ===", style="bold magenta"))
            print("1. Register New Property")
            print("2. View Existing Property")
            print("3. View Tenant Details")
            print("4. View Documents")
            print("5. Calculate Rent for property")
            print("6. Handle maintenance request")
            print("7. Delete Existing Property")
            print("8. Exit")
            choice = int(input("Enter choice: "))
            print()
            print()
        

            if choice == 1:
                self.create_property()
                self.insert_into_property()
            elif choice == 2:
                self.view_existing_property()
            elif choice == 3:
                self.view_tenant_details()
            elif choice == 4:
                self.view_documents()
            elif choice == 5:
                self.calculate_rent_payment_landowner()
            elif choice == 7:
                self.delete_existing_property()
            elif choice == 8:
                print("Exiting...")
                
                return
            else:
                print("Invalid choice")
        
            console.print("\n[bold blue]=========================================================[/bold blue]\n")

    def view_lease_details(self):
        if not self.logged_in:
            print("Please login first.")
            self.tenant_login()
            if not self.logged_in:
                return

        tenant_id = input("Enter tenant ID: ")
        # Retrieve leases associated with the specified tenant
        self.cur.execute('''SELECT lease_id FROM Tenant WHERE tenant_id = ?;''', (tenant_id,))
        leases = self.cur.fetchall()

        if leases:
            # Extract lease IDs from the fetched leases
            lease_ids = [lease[0] for lease in leases]
            # Query lease details for the tenant's leases
            self.cur.execute('''SELECT * FROM Lease WHERE lease_id IN ({seq})'''.format(seq=','.join(['?']*len(lease_ids))), lease_ids)
            lease_details = self.cur.fetchall()

            if lease_details:
                print("Lease details for tenant ID", tenant_id, ":")
                for lease in lease_details:
                    print(lease)
            else:
                print("No lease details found for tenant ID", tenant_id)
        else:
            print("No leases found for tenant ID", tenant_id)        
        def tenant_login(self):
            print("=== Tenant Authentication ===")
            print("1. Existing User")
            print("2. New User")
            choice = input("Enter your choice: ")

            if choice == '1':
                existing_username = input("Enter your username: ")
                existing_password = input("Enter your password: ")
                # Check if the username and password exist in the database
                # Implement your authentication logic here

                # For demonstration purposes, let's assume a simple hardcoded check
                if existing_username == "existing_user" and existing_password == "password":
                    print("Login successful!")
                    self.logged_in = True
                else:
                    print("Invalid username or password. Please try again.")
            elif choice == '2':
                new_username = input("Enter a new username: ")
                new_password = input("Enter a new password: ")
                # Store the new username and password in the database
                # Implement your user creation logic here

                # For demonstration purposes, let's assume we successfully create a new user
                print("New user created successfully!")
                self.logged_in = True
            else:
                print("Invalid choice. Please try again.")
            
    def view_maintenance_requests(self):
        if not self.logged_in:
            print("Please login first.")
            self.tenant_login()
            if not self.logged_in:
                return

        tenant_id = input("Enter tenant ID: ")
        # Retrieve maintenance requests associated with the specified tenant
        self.cur.execute('''SELECT * FROM MaintenanceRequest WHERE tenant_id = ?;''', (tenant_id,))
        maintenance_requests = self.cur.fetchall()

        if maintenance_requests:
            print("Maintenance requests for tenant ID", tenant_id, ":")
            for request in maintenance_requests:
                print(request)
        else:
            print("No maintenance requests found for tenant ID", tenant_id)
         
    def tenant_login(self):
        console.print(Panel("=== Tenant Login ===", style="bold magenta"))
        print("1. Existing User")
        print("2. New User")
        title = Text("Enter your choice: ", style="italic")
        console.print(title, style="white")
        choice=input("")

        if choice == '1':
            existing_username = input("Enter your username: ")
            existing_password = input("Enter your password: ")
            # Check if the username and password exist in the database
            # Implement your authentication logic here

            # For demonstration purposes, let's assume a simple hardcoded check
            if existing_username == "existing_user" and existing_password == "password":
                print("Login successful!")
                self.logged_in = True
            else:
                print("Invalid username or password. Please try again.")
        elif choice == '2':
            self.create_tenant()
            self.insert_into_tenant()
            new_username = input("Enter a new username: ")
            new_password = input("Enter a new password: ")
            # Store the new username and password in the database
            # Implement your user creation logic here

            # For demonstration purposes, let's assume we successfully create a new user
            print("New user created successfully!")
            self.logged_in = True
        else:
            print("Invalid choice. Please try again.")
            
    def tenant_menu(self):
        if not self.logged_in:
            print("Please login first.")
            self.tenant_login()
            if not self.logged_in:
                return

        print("Welcome Tenant")
        while True:
            self.console.print(Panel("=== Landowner Menu ===", style="bold magenta"))
            print("1. View Lease Details")
            print("2. View Maintenance Requests")
            print("3. View rent details")
            print("4. View Documents")
            print("5. Search Property")
            print("6. Exit")
            choice = input("Enter choice: ")
            print()
            print()

            if choice == '1':
                self.view_lease_details()
            elif choice == '2':
                self.view_maintenance_requests()
            elif choice == '3':
                self.calculate_rent_payment()
            elif choice == '4':
                self.view_documents_tenant()
            elif choice == '5':
                self.search_property()
            elif choice == '6':
                print("Exiting...")
                break
            else:
                print("Invalid choice")       
            
    def admin_menu(self):
        if not self.logged_in:
            self.login()
            if not self.logged_in:
                return
        while True:
            self.console.print(Panel("=== Admin Menu ===", style="bold magenta"))
            print("1. Creation")
            print("2. Testing")
            print("3. Display")
            choice = int(input("Enter choice: "))

            if choice == 1:
                print("\n=== MENU ===")
                print("1. Insert Landowner")
                print("2. Insert Property")
                print("3. Insert Lease")
                print("4. Insert Tenant")
                print("5. Insert Rent Payment")
                print("6. Insert Maintenance Request")
                print("7. Insert Document")
                print("8. Exit")
                choice2 = int(input("Enter choice: "))

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
                    print("Exiting...")
                    break
                else:
                    print("Invalid choice")

            elif choice == 2:
                print("\n=== MENU-TESTING ===")
                print("1. Calculate rent payment")
                print("2. Search property")
                print("3. Transfer ownership")
                print("4. Exit")
                choice3 = int(input("Enter choice: "))

                if choice3 == 1:
                    total_payment = self.calculate_rent_payment()
                    if total_payment is not None:
                        print(f"Total rent payment: ${total_payment}")
                elif choice3 == 2:
                    properties = self.search_property()
                    if properties:
                        print("Properties found:")
                        for prop in properties:
                            print(prop)
                    else:
                        print("No properties found.")
                elif choice3 == 3:
                    self.transfer_property_ownership()
                elif choice3 == 4:
                    print("Exiting...")
                    break
                else:
                    print("Invalid choice")
            
            elif(choice==3):
                self.display_data()
            else:
                print("Invalid choice")

     
def main():
    a=Database("PMS")
    a.input_sample_data()
    a.mainmenu()
if __name__=='__main__':
    main()    