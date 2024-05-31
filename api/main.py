from fastapi import FastAPI, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from models import Category, SubCategory, SVG, Dish
from decouple import config

BASE_URL = config('BASE_URL')

SQLALCHEMY_DATABASE_URL = f"postgresql://sanjik:1@db:5432/michelle_db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/categories/")
def get_categories(request: Request, db: Session = Depends(get_db)):
    categories = db.query(Category).all()
    for category in categories:
        if category.image:
            category.image = BASE_URL + "media/" + category.image
    return categories

@app.get("/subcategories/")
def get_subcategories(request: Request, db: Session = Depends(get_db)):
    subcategories = db.query(SubCategory).all()
    for subcategory in subcategories:
        if subcategory.image:
            subcategory.image = BASE_URL + "media/" + subcategory.image
    return subcategories

@app.get("/dishes/")
def get_dishes(request: Request, db: Session = Depends(get_db)):
    dishes = db.query(Dish).all()
    for dish in dishes:
        if dish.image:
            dish.image = BASE_URL + "media/" + dish.image
    return dishes

@app.get("/svgs/")
def get_svgs(request: Request, db: Session = Depends(get_db)):
    svgs = db.query(SVG).all()
    for svg in svgs:
        if svg.svg:
            svg.svg = BASE_URL + "media/" + svg.svg
    return svgs
