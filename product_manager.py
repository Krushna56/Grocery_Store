from storage import JsonStorage

class ProductManager:
    def __init__(self, storage):
        self.storage = storage
    
    def add_product(self, name, price, quantity, category):
        product = {
            'id': self.storage.get_next_id(),
            'name': name,
            'price': price,
            'quantity': quantity,
            'category': category
        }
        self.storage.data['products'].append(product)
        self.storage.save_data()
        return product
    
    def update_product(self, id, name, price, quantity, category):
        for product in self.storage.data['products']:
            if product['id'] == id:
                product.update({
                    'name': name,
                    'price': price,
                    'quantity': quantity,
                    'category': category
                })
                self.storage.save_data()
                return True
        return False
    
    def delete_product(self, id):
        products = self.storage.data['products']
        self.storage.data['products'] = [p for p in products if p['id'] != id]
        self.storage.save_data()
    
    def get_all_products(self):
        return self.storage.data['products']
    
    def get_product(self, id):
        for product in self.storage.data['products']:
            if product['id'] == id:
                return product
        return None