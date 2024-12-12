# your_app_name/routing.py
from django.urls import path
from .Consumers import MyAsyncConsumer

websocket_urlpatterns = [
    path('ws/ToggleEditorStatus/<int:editor_id>/', MyAsyncConsumer.as_asgi()),
]
