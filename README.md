# Property-Management-System:

## Property:
    property_id (Primary Key)
    property_type
    address
    city
    state
    postal_code
    country
    description
    amenities
    rental_status
    ownership_status
    landowner_id (Foreign Key)

## Landowner
    landowner_id (Primary Key)
    first_name
    last_name
    email
    phone_number

 ## Tenant
    tenant_id (Primary Key)
    first_name
    last_name
    email
    phone_number
    date_of_birth
    move_in_date
    move_out_date
    lease_id (Foreign Key)

## Lease
    lease_id (Primary Key)
    property_id (Foreign Key)
    tenant_id (Foreign Key)
    start_date
    end_date
    rent_amount
    payment_schedule
    lease_terms

   ## RentPayment
    payment_id (Primary Key)
    lease_id (Foreign Key)
    payment_date
    amount
    payment_method
    transaction_id

   ## MaintenanceRequest
    request_id (Primary Key)
    property_id (Foreign Key)
    tenant_id (Foreign Key)
    request_date
    description
    status
    assigned_to

   ## Expense
    expense_id (Primary Key)
    property_id (Foreign Key)
    expense_date
    category
    amount
    description
    
   ## Document
    document_id (Primary Key)
    property_id (Foreign Key)
    document_type
    document_name
    upload_date
    file_path

