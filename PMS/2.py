from rich import print
from rich.console import Console
from rich.panel import Panel

import sqlite3

console = Console()

def display_slide(title, content):
    """Display a slide with a title and content."""
    console.print(Panel.fit(content, title=title, border_style="pink on white"))

def main_menu():
    """Display the main menu."""
    display_slide("Main Menu", """
    [1] Landowner
    [2] Tenant
    [3] Admin
    [4] Exit
    """)

def landowner_menu():
    """Display the landowner menu."""
    display_slide("Landowner Menu", """
    [1] Register New Property
    [2] View Existing Property
    [3] View Tenant Details
    [4] View Documents
    [5] Calculate Rent for Property
    [6] Handle Maintenance Request
    [7] Delete Existing Property
    [8] Exit
    """)

def tenant_menu():
    """Display the tenant menu."""
    display_slide("Tenant Menu", """
    [1] View Lease Details
    [2] View Maintenance Requests
    [3] View Rent Details
    [4] View Documents
    [5] Exit
    """)

def admin_menu():
    """Display the admin menu."""
    display_slide("Admin Menu", """
    [1] Creation
    [2] Testing
    [3] Display
    [4] Exit
    """)

def main():
    while True:
        main_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            landowner_menu()
        elif choice == '2':
            tenant_menu()
        elif choice == '3':
            admin_menu()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
