from sqlalchemy import Column, Integer, String, ForeignKey, Text, DECIMAL, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

dish_svg_association = Table(
    'dish_svg_association', 
    Base.metadata,
    Column('dish_id', Integer, ForeignKey('dishes.id')),
    Column('svg_id', Integer, ForeignKey('svgs.id'))
)

class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    title_ru = Column(String(120))
    title_kg = Column(String(120))
    title_tu = Column(String(120))
    title_en = Column(String(120))
    image = Column(String(255))
    link = Column(String(100))
    number = Column(Integer, default=0, nullable=True)

    subcategories = relationship("SubCategory", back_populates="category")
    
class SubCategory(Base):
    __tablename__ = 'subcategories'

    id = Column(Integer, primary_key=True)
    title_ru = Column(String(120))
    title_kg = Column(String(120))
    title_tu = Column(String(120))
    title_en = Column(String(120))
    category_id = Column(Integer, ForeignKey('categories.id'))
    image = Column(String(255))
    link = Column(String(100))
    number = Column(Integer, default=0, nullable=True)

    category = relationship("Category", back_populates="subcategories")

class SVG(Base):
    __tablename__ = 'svgs'

    id = Column(Integer, primary_key=True)
    svg = Column(String(255))

class Dish(Base):
    __tablename__ = 'dishes'

    id = Column(Integer, primary_key=True)
    title_ru = Column(String(120))
    title_kg = Column(String(120))
    title_tu = Column(String(120))
    title_en = Column(String(120))
    image = Column(String(255))
    subcategory_id = Column(Integer, ForeignKey('subcategories.id'))
    text_ru = Column(Text)
    text_kg = Column(Text)
    text_tu = Column(Text)
    text_en = Column(Text)
    price = Column(DECIMAL(10, 2), default=0)
    number = Column(Integer, default=0, nullable=True)

    subcategory = relationship("SubCategory", back_populates="dishes")
    svgs = relationship("SVG", secondary=dish_svg_association, backref="dishes")

SubCategory.dishes = relationship("Dish", back_populates="subcategory")
Category.subcategories = relationship("SubCategory", back_populates="category")
