from datetime import datetime

class SalesManager:
    def __init__(self, storage, product_manager):
        self.storage = storage
        self.product_manager = product_manager
    
    def record_sale(self, product_id, quantity):
        product = self.product_manager.get_product(product_id)
        if not product or product['quantity'] < quantity:
            return False
            
        total_price = product['price'] * quantity
        sale = {
            'id': self.storage.get_next_id(),
            'product_id': product_id,
            'product_name': product['name'],
            'quantity': quantity,
            'total_price': total_price,
            'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
        # Update product quantity
        product['quantity'] -= quantity
        self.storage.data['sales'].append(sale)
        self.storage.save_data()
        return True
    
    def get_sales_report(self):
        return self.storage.data['sales']