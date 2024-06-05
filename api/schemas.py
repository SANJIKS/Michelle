# schemas.py
from pydantic import BaseModel
from typing import List, Optional

class SVGBase(BaseModel):
    id: int
    svg: str

    class Config:
        orm_mode = True

class DishBase(BaseModel):
    id: int
    title_ru: str
    title_kg: str
    title_tu: str
    title_en: str
    image: Optional[str] = None
    subcategory_id: int
    text_ru: str
    text_kg: str
    text_tu: str
    text_en: str
    price: float
    number: Optional[int] = None
    svg_urls: List[SVGBase] = []

    class Config:
        orm_mode = True

class SubCategoryBase(BaseModel):
    id: int
    title_ru: str
    title_kg: str
    title_tu: str
    title_en: str
    category_id: int
    image: Optional[str] = None
    link: str
    number: Optional[int] = None

    class Config:
        orm_mode = True

class CategoryBase(BaseModel):
    id: int
    title_ru: str
    title_kg: str
    title_tu: str
    title_en: str
    image: Optional[str] = None
    link: str
    number: Optional[int] = None

    class Config:
        orm_mode = True


class CategoryWithSubCategories(BaseModel):
    category: CategoryBase
    subcategories: List[SubCategoryBase]