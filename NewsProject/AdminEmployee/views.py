# import time
# from django.http import HttpResponse
# from django.shortcuts import render
# from asgiref.sync import sync_to_async
# import asyncio
# from datetime import datetime


# # Create your views here.



# def syncdemo(request):
#     start_time_seconds = time.time()
#     start_time_milliseconds = int(start_time_seconds * 1000)  # Convert seconds to milliseconds
#     start_time_str = datetime.fromtimestamp(start_time_seconds).strftime('%Y-%m-%d %H:%M:%S.%f')
#     print(f"Start time: {start_time_str} (milliseconds: {start_time_milliseconds})")
#     # print("Started")
#     time.sleep(3)
#     end_time_seconds = time.time()
#     end_time_milliseconds = int(end_time_seconds * 1000)  # Convert seconds to milliseconds
#     end_time_str = datetime.fromtimestamp(end_time_seconds).strftime('%Y-%m-%d %H:%M:%S.%f')

#     print(f"End time: {end_time_str} (milliseconds: {end_time_milliseconds})")
    
#     execution_time_ms = end_time_milliseconds - start_time_milliseconds
#     print(f"Execution time: {execution_time_ms} milliseconds")
#     # print("Finished")
#     return HttpResponse("Sucess")

# async def asyncdemo(request):
#     start_time_seconds = time.time()
#     start_time_milliseconds = int(start_time_seconds * 1000)  # Convert seconds to milliseconds
#     start_time_str = datetime.fromtimestamp(start_time_seconds).strftime('%Y-%m-%d %H:%M:%S.%f')
#     print(f"Start time: {start_time_str} (milliseconds: {start_time_milliseconds})")
#     # print("Started")
#     await asyncio.sleep(3)
#     end_time_seconds = time.time()
#     end_time_milliseconds = int(end_time_seconds * 1000)  # Convert seconds to milliseconds
#     end_time_str = datetime.fromtimestamp(end_time_seconds).strftime('%Y-%m-%d %H:%M:%S.%f')

#     print(f"End time: {end_time_str} (milliseconds: {end_time_milliseconds})")
    
#     execution_time_ms = end_time_milliseconds - start_time_milliseconds
#     print(f"Execution time: {execution_time_ms} milliseconds")
#     return HttpResponse("Sucess async")