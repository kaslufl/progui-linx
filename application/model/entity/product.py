class Product:
    def __init__(self, id, name, image, old_price, price, description, installments, value):
        self._id = id
        self.name = name
        self.image = image
        self.old_price = old_price
        self.price = price
        self.description = description
        self.installments = installments
        self.value = value
    
    def get_id(self):
        return self._id

    def get_name(self):
        return self.name
    
    def get_image(self):
        return self.image
    
    def get_old_price(self):
        return self.old_price
    
    def get_price(self):
        return self.price
    
    def get_description(self):
        return self.description
    
    def get_installments(self):
        return self.installments
    
    def get_value(self):
        return self.value