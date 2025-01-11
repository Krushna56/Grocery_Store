import psycopg2
import os
from storage import JsonStorage
from product_manager import ProductManager
from sales_manager import SalesManager
from ui_manager import UIManager
from dotenv import load_dotenv
    
# Load environment variables from .env
load_dotenv()
 
# Fetch variables
USER = os.getenv("POSTGRES_USER")
PASSWORD = os.getenv("POSTGRES_PASSWORD")
HOST = os.getenv("POSTGRES_HOST")
PORT = os.getenv("POSTGRES_PORT")
DBNAME = os.getenv("POSTGRES_DB")

# Connect to the database
try:
    connection = psycopg2.connect(
        user=USER,
        password=PASSWORD,
        host=HOST,
        port=PORT,
        dbname=DBNAME
    )
    print("Connection successful!")
    
    # Create a cursor to execute SQL queries
    cursor = connection.cursor()
    
    # Example query
    cursor.execute("SELECT NOW();")
    result = cursor.fetchone()
    print("Current Time:", result)

    # Close the cursor and connection
    cursor.close()
    connection.close()
    print("Connection closed.")

except Exception as e:
    print(f"Failed to connect: {e}")

def main():
    # Initialize storage and managers
    storage = JsonStorage('store_data.json')
    product_manager = ProductManager(storage)
    sales_manager = SalesManager(storage, product_manager)
    ui_manager = UIManager(product_manager, sales_manager)
    
    # Run the application
    ui_manager.run()

if __name__ == "__main__":
    main()


    