# python_Billing_App
The goal of this project is to develop a GUI-based billing application for a retail store using Python and Tkinter. It helps shopkeepers easily manage customer orders, calculate item-wise and category-wise totals, apply taxes, and generate a final bill that can be saved and retrieved later.

🛠️ Core Functionalities
1. Customer Entry Section
Users enter the customer's name, phone number, and optionally search for an existing bill.

A random 4-digit bill number is generated for each transaction.

2. Product Categories
The application has three major product categories:

Cosmetics (e.g., soap, face wash, lotion)

Grocery (e.g., rice, sugar, tea)

Cold Drinks (e.g., Pepsi, Sprite, Red Bull)

Each product has:

A quantity input field

Fixed price per unit

Backend calculation to multiply quantity × price

3. Price and Tax Calculation
Totals are calculated automatically when the “Total” button is clicked.

A 5% GST is applied to each category separately.

All prices and taxes are displayed in the bottom panel.

4. Bill Area
The bill is dynamically generated in the text area.

It includes product name, quantity, price, and tax breakdown.

The total bill is shown at the end.

5. Save Bill Feature
The bill can be saved to a .txt file inside the Bills/ folder.

Each file is named using the unique bill number.

6. Search Bill
A user can retrieve an old bill by entering the bill number.

If the file exists, it is displayed in the bill area.

7. Clear & Exit Options
Clear resets all entries and variables.

Exit closes the application with a confirmation prompt.

📁 How It Works (Flow)
User enters customer details and product quantities.

Clicks 'Total' to compute price + taxes.

Clicks 'Generate Bill' to print bill in the text area.

Can save the bill to a .txt file.

Future searches can retrieve saved bills by number.

👨‍💻 Why This Project is Useful
Gives real-world experience with Tkinter GUI

Involves file handling, logic building, and error handling

Teaches how to break a problem into multiple small, manageable parts

Useful for retail shops, mini supermarkets, or counters where manual billing is still common

🔧 Optional Improvements (Future Scope)
Add login system for different staff users

Add PDF export of bills using reportlab

Connect to SQLite/MySQL database for long-term data storage

Use Modern UI toolkit like customtkinter

Add discounts, stock tracking, and analytics dashboard
