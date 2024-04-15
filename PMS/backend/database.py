import sqlite3


class Database:
    def __init__(self,db_file):
        self.db_file=db_file
        self.conn=sqlite3.connect(self.db_file)
        self.cur=self.conn.cursor()
        self.logged_in = False
        
    
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
        start_date = input("Enter start date (YYYY-MM-DD): ")
        end_date = input("Enter end date (YYYY-MM-DD): ")

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
            print("Lease not found.")
            return None
        
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
        return properties
    
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
                    start_year, start_month = map(int, start_date.split('-'))
                    end_year, end_month = map(int, end_date.split('-'))
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
            
    def delete_existing_property(self):
        property_id = input("Enter property ID to delete: ")
        try:
            self.cur.execute("DELETE FROM Property WHERE property_id = ?", (property_id,))
            self.conn.commit()
            print("Property deleted successfully.")
        except sqlite3.Error as e:
            print("Error deleting property:", e)

    def mainmenu(self):
            print("\n=== Property Management System ===")
            print("1. Landowner")
            print("2. Tenant")
            print("3. Admin")
            choice = int(input("Enter choice: "))
            if choice == 1:
                self.landowner_menu()
            elif choice == 2:
                self.view_existing_property()
            elif choice == 3:
                self.admin_menu()
                
            
        
    def landowner_menu(self):
        print("Welcome Landowner")
        while True:
            print("\n=== Property Management System ===")
            print("1. Register New Property")
            print("2. View Existing Property")
            print("3. View Tenant Details")
            print("4. View Documents")
            print("5. Calculate Rent for property")
            print("6. Handle maintenance request")
            print("7. Delete Existing Property")
            print("8. Exit")
            choice = int(input("Enter choice: "))

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
            elif choice == 6:
                self.handle_maintenance_request()
            elif choice == 7:
                self.delete_existing_property()
            elif choice == 8:
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
            print("\n=== Property Management System ===")
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
    a.mainmenu()
if __name__=='__main__':
    main()    