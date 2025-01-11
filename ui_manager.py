class UIManager:
    def __init__(self, product_manager, sales_manager):
        self.product_manager = product_manager
        self.sales_manager = sales_manager
    
    def print_menu(self):
        print("\n=== Grocery Store Management System ===")
        print("1. Add Product")
        print("2. Update Product")
        print("3. Delete Product")
        print("4. View All Products")
        print("5. Record Sale")
        print("6. View Sales Report")
        print("7. Exit")
    
    def handle_add_product(self):
        name = input("Enter product name: ")
        price = float(input("Enter price: "))
        quantity = int(input("Enter quantity: "))
        category = input("Enter category: ")
        self.product_manager.add_product(name, price, quantity, category)
        print("Product added successfully!")
    
    def handle_update_product(self):
        id = int(input("Enter product ID to update: "))
        product = self.product_manager.get_product(id)
        if product:
            name = input("Enter new name (press enter to keep current): ") or product['name']
            price = float(input("Enter new price (press enter to keep current): ") or product['price'])
            quantity = int(input("Enter new quantity (press enter to keep current): ") or product['quantity'])
            category = input("Enter new category (press enter to keep current): ") or product['category']
            self.product_manager.update_product(id, name, price, quantity, category)
            print("Product updated successfully!")
        else:
            print("Product not found!")
    
    def handle_delete_product(self):
        id = int(input("Enter product ID to delete: "))
        if self.product_manager.get_product(id):
            self.product_manager.delete_product(id)
            print("Product deleted successfully!")
        else:
            print("Product not found!")
    
    def handle_view_products(self):
        products = self.product_manager.get_all_products()
        print("\nAll Products:")
        print("ID | Name | Price | Quantity | Category")
        print("-" * 50)
        for product in products:
            print(f"{product['id']} | {product['name']} | ${product['price']:.2f} | {product['quantity']} | {product['category']}")
    
    def handle_record_sale(self):
        product_id = int(input("Enter product ID: "))
        quantity = int(input("Enter quantity sold: "))
        if self.sales_manager.record_sale(product_id, quantity):
            print("Sale recorded successfully!")
        else:
            print("Sale failed! Check product ID and quantity.")
    
    def handle_view_sales(self):
        sales = self.sales_manager.get_sales_report()
        print("\nSales Report:")
        print("Product | Quantity | Total Price | Date")
        print("-" * 60)
        for sale in sales:
            print(f"{sale['product_name']} | {sale['quantity']} | ${sale['total_price']:.2f} | {sale['date']}")
    
    def run(self):
        while True:
            self.print_menu()
            choice = input("\nEnter your choice (1-7): ")
            
            try:
                if choice == '1':
                    self.handle_add_product()
                elif choice == '2':
                    self.handle_update_product()
                elif choice == '3':
                    self.handle_delete_product()
                elif choice == '4':
                    self.handle_view_products()
                elif choice == '5':
                    self.handle_record_sale()
                elif choice == '6':
                    self.handle_view_sales()
                elif choice == '7':
                    print("Thank you for using the Grocery Store Management System!")
                    break
                else:
                    print("Invalid choice! Please try again.")
            except ValueError as e:
                print("Invalid input! Please enter correct values.")