from src.foodrate.FoodService import FoodService
from src.foodrate.FoodUi import FoodUi


class FoodController:
    def __init__(self):
        self.service = FoodService()
        self.ui = FoodUi()

    def handle_add_product(self, product, mass, kkal, protein, sacharidy, fat):
        # 1. Передає дані в сервіс для обрахунку та збереження
        self.service.add_product(product, mass, kkal, protein, sacharidy, fat)
        print("Продукт успішно додано!")

    def handle_view_products(self):
        # 1. Просить сервіс дістати дані з БД
        products = self.service.get_all_products()
        # 2. Передає ці дані в UI, щоб він їх намалював
        self.ui.show_products(products)