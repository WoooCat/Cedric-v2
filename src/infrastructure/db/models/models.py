from sqlalchemy import Column, Integer, String, ForeignKey, Float, Boolean, DateTime
from sqlalchemy.orm import relationship, backref
from datetime import datetime
from src.infrastructure.db.database import Base


# from config import (
#     CATEGORY_RELATIONS_TABLE,
#     CATEGORY_TABLE,
#     DISCOUNT_TABLE,
#     PRODUCT_DISCOUNT_TABLE,
#     PRODUCT_TABLE,
#     RESERVATION_TABLE,
#     SALE_TABLE,
# )

class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    parent_id = Column(Integer, ForeignKey('categories.id'), nullable=True)

    subcategories = relationship(
        "Category",
        backref=backref("parent", remote_side=[id]),
        lazy="selectin",
        collection_class=list,
        cascade="all, delete-orphan",
    )
    products = relationship(
        "Product",
        back_populates="category",
        cascade="all, delete",
    )


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    description = Column(String)
    price = Column(Float, nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)
    category = relationship("Category", back_populates="products")
    stock = Column(Integer, default=0)
    reservations = relationship("Reservation", back_populates="product")
    sales = relationship("Sale", back_populates="product")
    discount_id = Column(Integer, ForeignKey('discounts.id'), nullable=True)
    discount = relationship("Discount", back_populates="products")

    @property
    def final_price(self):
        if self.discount:
            return self.price * (1 - self.discount.percentage / 100)
        return self.price

    @property
    def reserved_quantity(self):
        return sum(reservation.quantity for reservation in self.reservations if reservation.active)


class Reservation(Base):
    __tablename__ = 'reservations'

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    reserved_at = Column(DateTime, default=datetime.utcnow)
    quantity = Column(Integer, nullable=False)
    active = Column(Boolean, default=True)

    product = relationship("Product", back_populates="reservations")


class Sale(Base):
    __tablename__ = 'sales'

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    quantity = Column(Integer, nullable=False)
    discount = Column(Float, default=0.0)
    sold_at = Column(DateTime, default=datetime.utcnow)

    product = relationship("Product", back_populates="sales")


class Discount(Base):
    __tablename__ = 'discounts'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    percentage = Column(Float, nullable=False)
    description = Column(String, nullable=True)

    products = relationship("Product", back_populates="discount")
