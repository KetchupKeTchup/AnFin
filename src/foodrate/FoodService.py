from src.database.FoodKkal import FoodKkalManager

class FoodService:
    def __init__(self):
        self.food_manager = FoodKkalManager()


    def add_product(self,product,mass,kkal,protein,sacharidy,fat):
        total_kkal = (kkal * mass) / 100
        total_protein = (protein * mass) / 100
        total_sacharidy = (sacharidy * mass) / 100
        total_fat = (fat * mass) / 100

        self.food_manager.add_product(product, mass, total_kkal, total_protein, total_sacharidy, total_fat)

    def get_all_products(self):
        # Повертає список продуктів з бази даних
        return self.food_manager.get_all_products()

    def get_total_calories(self):
        # Повертає загальну кількість калорій, білків, вуглеводів та жирів за сьогоднішній день
        return self.food_manager.get_total_calories()