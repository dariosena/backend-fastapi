from ...repositories.CategoriesRepository import CategoriesRepository


class ListCategoriesUseCase:
    def __init__(self) -> None:
        self.categoriesRepository = CategoriesRepository()

    def execute(self):
        return self.categoriesRepository.getAllCategories()
