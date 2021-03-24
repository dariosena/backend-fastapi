from typing import List
from ..useCases.createCategory.CreateCategoryDto import CreateCategoryDto
from ..model.Category import Category


class CategoriesRepository:
    def __init__(self) -> None:
        self.categories: List[Category] = []

    def findByName(self, name: str) -> Category:
        for category in self.categories:
            if category.name == name:
                return category

    def create(self, createCategoryDto: CreateCategoryDto):
        category: Category = Category(
            createCategoryDto.name, createCategoryDto.description)

        self.categories.append(category)

    def getAllCategories(self) -> List[Category]:
        return self.categories
