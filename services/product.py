from models.product import Product as ProductModel
from schemas.product import Product, EditProduct

class ProductService():
    def __init__(self, db) -> None:
        self.db = db
    
    def get_products(self):
        result = self.db.query(ProductModel).all()
        return result
    
    def get_product(self, id: int):
        result = self.db.query(ProductModel).filter(ProductModel.id == id).first()
        print(333,result)
        return result
    
    def create_product(self, product: Product):
        new_product = ProductModel(**product.model_dump())
        self.db.add(new_product)
        self.db.commit()

    def get_products_by_category(self, category:str):
        result = self.db.query(ProductModel).filter(ProductModel.category == category).all()
        return result
    
    def get_products_by_provider(self, id_provider:int):
        result = self.db.query(ProductModel).filter(ProductModel.id_provider == id_provider).all()
        return result
    
    def update_product(self, id:int, data:Product):
        print(111,data)
        product = self.get_product(id)
        print(222,product)
        product.stock = data.stock
        product.price = data.price
        self.db.commit()

    def delete_product(self, id:int):
        product = self.get_product(id)
        self.db.delete(product)
        self.db.commit()



    
    
    
