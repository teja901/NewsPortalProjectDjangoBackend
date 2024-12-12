from django.db import IntegrityError
from django.shortcuts import get_object_or_404
from ninja import NinjaAPI ,File ,UploadedFile,Form
from pydantic import ValidationError
from .models import *
from .Schemas import AdminEmployeeGetSchema, CategorySchema, SubCategorySchema
from django.http import Http404, JsonResponse
from typing import List
import json

api = NinjaAPI()


def redis():
        redis_client = redis.StrictRedis(
        host=settings.CHANNEL_LAYERS['default']['CONFIG']['hosts'][0][0],
        port=settings.CHANNEL_LAYERS['default']['CONFIG']['hosts'][0][1],
        db=0
    )

    # Fetch all keys that represent channel groups
        group_keys = redis_client.keys("asgi:group:*")
        group_names = [key.decode("utf-8").replace("asgi:group:", "") for key in group_keys]
        print(group_names)
        print(group_keys)


@api.get('validateAdminEmployee/{username}/{password}',response=AdminEmployeeGetSchema)
def getAdminEmployeeCredentials(request,username :str,password :str):
    try:
        employee = get_object_or_404(AdminEmployeeCredentials, name=username, password=password)
        if not employee.status:
            return JsonResponse({"detail": "UnAuthorised"}, status=403)
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
@api.post('createcategory',response={201:List[CategorySchema]})
def createCategory(request):
    data=request.POST.dict()
    try:
     category=Categories.objects.create(**data)
    except:
        return JsonResponse({'data':"Category Already Exists"},status=400)
    return Categories.objects.all()

@api.get('getAllCategoriesSubCategories',response={200:List[CategorySchema]})
def getAllCategoriesSubCategories(request):
    return Categories.objects.all()
   
   
# Delete Category By NAme {Associated Sub Categories Will deleted automatically}................
@api.delete("deleteCategoryByName/{name}",response={200:List[CategorySchema]})
def deleteCategoryByName(request,name:str):
    try:
     category=Categories.objects.get(categoryName=name)
     category.delete()
    except: return JsonResponse({"data":"No Records Found"},status=404)
    return Categories.objects.all()

#Create a SubCAtegory......................................
@api.post('createSubCategory',response={201:List[CategorySchema]})
def createSubcategory(request):
    data=request.POST.dict()
    category_id=data.get('category')
    try:
     cresult=Categories.objects.get(id=category_id)
     subcategory=SubCategories.objects.create(subcategoryName=data.get('subcategoryName'),category=cresult)
    except IntegrityError as e:return JsonResponse({'data':"SubCategory Already Exists"},status=400)
    except :return JsonResponse({"data":"No Category Records Found"},status=404)
    return Categories.objects.all()

# Get CAtegory and their associated SubCategories By Name........
@api.get('/getCategorySubCategoriesByName/{name}',response=CategorySchema)
def getCategorySubCategoriesByName(request,name:str):
    try:return Categories.objects.get(categoryName=name)
    except:return JsonResponse({"data":"No Records Found"},status=404)
     
# Get Only SubCategory BY NAMe.............................
@api.get('getSubCategoryByName/{name}',response=SubCategorySchema)
def getSubCategoriesByName(request,name:str):
  try:subcategory=get_object_or_404(SubCategories, subcategoryName=name)
  except:return JsonResponse({"data":"No Records Found"},status=404)
  return subcategory

@api.delete('deleteSubCategoryByName/{subcategoryname}',response={200:List[CategorySchema]})
def deleteSubCategoryByName(request,subcategoryname : str):
    try:
     subcategory=SubCategories.objects.get(subcategoryName=subcategoryname)
     subcategory.delete()
    except: return JsonResponse({"data":"No Records Found"},status=404)
    return Categories.objects.all()
    

from asgiref.sync import sync_to_async
from channels.layers import get_channel_layer
from django.conf import settings
import redis


@sync_to_async
def toggle_employee_status_in_db(emp_id):
    emp_obj = AdminEmployeeCredentials.objects.get(id=emp_id)
    emp_obj.status = not emp_obj.status
    emp_obj.save()
    return emp_obj.status

@api.get("toggeleEmployeeStatus/{empId}")
async def toggle_employee_status(request, empId):
   
    try:
        updated_status = await toggle_employee_status_in_db(empId)
        channel_layer = get_channel_layer()
        group_name = f"Editor_{empId}"
     
       
        if channel_layer:
            await channel_layer.group_send(
                group_name,
                {
                    'type': 'chat_message',
                    'status': updated_status
                }
            )

        return JsonResponse({'data': "Success", 'status': updated_status}, status=200)

    except AdminEmployeeCredentials.DoesNotExist:
        return JsonResponse({'error': 'Employee not found'}, status=404)
    
async def employee_status_update(self, updated_status):
       
        print(f"Received status update: {updated_status}")

        # Send response to WebSocket
        await self.send(text_data=json.dumps({
            'status': updated_status,
        }))

     
    
         
   