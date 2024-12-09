from ninja import Schema, ModelSchema
from ninja.files import UploadedFile
from pydantic import BaseModel,ConfigDict
from .models import *
from typing import Any, Dict, List,Optional



# class CategoryGet(Schema):
#     categoryName: str

class SubCategorySchema(ModelSchema):
    class Config:
        model = SubCategories  
        model_fields = "__all__"
    
class CategorySchema(ModelSchema):
    subcategories:list[SubCategorySchema] = []
    class Config:
        model = Categories
        model_fields = "__all__"
        
    


class AdminEmployeeGetSchema(ModelSchema):
    categories: list[CategorySchema] = []
    class Config:
        model = AdminEmployeeCredentials
        model_fields = "__all__"
        
     
class AdminEmployeeCreate(Schema):
    pass

