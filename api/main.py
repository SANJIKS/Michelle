from fastapi import FastAPI, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from models import Category, SubCategory, SVG, Dish

SQLALCHEMY_DATABASE_URL = "sqlite:///./db.sqlite3"

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
            category.image = str(request.base_url) + "media/" + category.image
    return categories

@app.get("/subcategories/")
def get_subcategories(request: Request, db: Session = Depends(get_db)):
    subcategories = db.query(SubCategory).all()
    for subcategory in subcategories:
        if subcategory.image:
            subcategory.image = str(request.base_url) + "media/" + subcategory.image
    return subcategories

@app.get("/dishes/")
def get_dishes(request: Request, db: Session = Depends(get_db)):
    dishes = db.query(Dish).all()
    for dish in dishes:
        if dish.image:
            dish.image = str(request.base_url) + "media/" + dish.image
    return dishes

@app.get("/svgs/")
def get_svgs(request: Request, db: Session = Depends(get_db)):
    svgs = db.query(SVG).all()
    for svg in svgs:
        if svg.svg:
            svg.svg = str(request.base_url) + "media/" + svg.svg
    return svgs
