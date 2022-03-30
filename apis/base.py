from sys import prefix
from fastapi import APIRouter
from apis.version1 import route_homepage
from apis.version1 import route_users

api_router = APIRouter()
api_router.include_router(route_homepage.general_pages_router, prefix="", tags=["general_pages"])
api_router.include_router(route_users.router,prefix="/users", tags=["users"])