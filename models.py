from flask_sqlalchemy import SQLAlchemy
db=SQLAlchemy()

class Products(db.Model):
    __tablename__ = "product"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    url_image = db.Column(db.String(200))
    price = db.Column(db.Float)
    discount = db.Column(db.Integer)
    category = db.Column(db.Integer, db.ForeignKey("category.id"), nullable= False)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "url_image": self.url_image,
            "price": self.price,
            "discount": self.discount,
            "category": self.category
        }

class Category(db.Model):
    __tablename__ = "category"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    product_id = db.relationship("Products", backref="product")

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name            
        }
    
    def get_products(self):
        return list(map(lambda product: product.serialize(), self.product_id))

    
