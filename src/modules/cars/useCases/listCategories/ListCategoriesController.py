from typing import List
from fastapi_utils.cbv import cbv

from modules.cars.model.Category import Category

from .ListCategoriesUseCase import ListCategoriesUseCase
from .. import categoriesRouter


@cbv(categoriesRouter)
class ListCategoriesController:
    def __init__(self) -> None:
        self.listCategoriesUseCase = ListCategoriesUseCase()

    @categoriesRouter.get("/categories")
    def handle(self) -> List[Category]:
        return self.listCategoriesUseCase.execute()
