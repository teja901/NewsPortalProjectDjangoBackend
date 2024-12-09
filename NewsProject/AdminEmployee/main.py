from django.shortcuts import get_object_or_404
from ninja import NinjaAPI ,File ,UploadedFile,Form
from pydantic import ValidationError
from .models import *
from .Schemas import AdminEmployeeGetSchema, CategorySchema, SubCategorySchema
from django.http import Http404, JsonResponse
from typing import List
import json

api = NinjaAPI()


@api.get('validateAdminEmployee/{username}/{password}',response=AdminEmployeeGetSchema)
def getAdminEmployeeCredentials(request,username :str,password :str):
    try:
        employee = get_object_or_404(AdminEmployeeCredentials, name=username, password=password)
    except:
        return JsonResponse({"detail": "Invalid Credentials"}, status=404)
    return employee



# Create Admin EMployee Function in DB.................................
@api.post("createAdminorEmployee")
def create_admin_employee(request,name:str=Form(...)):
    print(name)
    print(request.POST.dict())
    # for file in files:
    #     print(f"Filename: {file.name}, Size: {file.size} bytes")
    return {"message": "Files uploaded successfully!"}
   
   
# Create Category in DB.......................
@api.post('createcategory',response={201:CategorySchema})
def createCategory(request):
    data=request.POST.dict()
    category=Categories.objects.create(**data)
    return category

#Create a SubCAtegory......................................
@api.post('createSubCategory',response={201:SubCategorySchema})
def createSubcategory(request):
    data=request.POST.dict()
    category_id=data.get('category')
    # print(category_id)
    # print(data.get('subcategoryName'))
    try:
     cresult=Categories.objects.get(id=category_id)
     subcategory=SubCategories.objects.create(subcategoryName=data.get('subcategoryName'),category=cresult)
    except :
        return JsonResponse({"data":"No Records Found"},status=404)
    return subcategory


# Get CAtegory and their associated SubCategories By Name........
@api.get('/getCategorySubCategoriesByName/{name}')
def getCategorySubCategoriesByName(request,name:str):
    try:
     category=Categories.objects.get(categoryName=name)
     subcategories = category.subcategories.values("id", "subcategoryName")
     return {
            "categoryName": category.categoryName,
            "subcategories": list(subcategories)
        }
    except:
        return JsonResponse({"data":"No Records Found"},status=404)
     
# Get Only SubCategory BY NAMe.............................
@api.get('getSubCategoryByName/{name}',response=SubCategorySchema)
def getSubCategoriesByName(request,name:str):
  try:subcategory=get_object_or_404(SubCategories, subcategoryName=name)
  except:return JsonResponse({"data":"No Records Found"},status=404)
  return subcategory

# Delete Category By NAme {Associated Sub Categories Will deleted automatically}................
@api.delete("deleteCategoryByName/{name}")
def deleteCategoryByName(request,name:str):
    try:
     category=Categories.objects.get(categoryName=name)
     category.delete()
    except: return JsonResponse({"data":"No Records Found"},status=404)
    return {"data": "Category deleted successfully!"}
    
    
     
    
         
   