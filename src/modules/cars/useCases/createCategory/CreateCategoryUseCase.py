from fastapi import HTTPException

from .CreateCategoryDto import CreateCategoryDto
from ...repositories.CategoriesRepository import CategoriesRepository


class CreateCategoryUseCase:
    def __init__(self) -> None:
        self.categoriesRepository = CategoriesRepository()

    def execute(self, createCategoryDto: CreateCategoryDto):
        categoryAlreadyExists = self.categoriesRepository.findByName(
            createCategoryDto.name)

        if (categoryAlreadyExists):
            raise HTTPException(
                status_code=404, detail='Category already exists.')

        self.categoriesRepository.create(createCategoryDto)
