from fastapi import FastAPI

from .modules.cars.useCases.createCategory.CreateCategoryController import categoriesRouter

app = FastAPI()

app.include_router(categoriesRouter)
