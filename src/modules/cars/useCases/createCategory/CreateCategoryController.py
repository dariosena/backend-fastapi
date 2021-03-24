from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter

from .CreateCategoryDto import CreateCategoryDto
from .CreateCategoryUseCase import CreateCategoryUseCase
from .. import categoriesRouter


@cbv(categoriesRouter)
class CreateCategoryController:
    def __init__(self) -> None:
        self.createCategoryUseCase = CreateCategoryUseCase()

    @categoriesRouter.post("/categories")
    def handle(self, createCategoryDto: CreateCategoryDto):
        self.createCategoryUseCase.execute(createCategoryDto)
