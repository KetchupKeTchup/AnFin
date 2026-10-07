from src.foodrate.FoodService import FoodService
from src.foodrate.FoodUi import FoodUi

def main():
    ui = FoodUi()
    service = FoodService()

    while True:
        action = ui.display_menu()

        if action == "1":
            # 1. Просимо UI зібрати дані
            product_data = ui.get_product_data()

            if product_data is not None:
                service.add_product(*product_data)
                ui.show_message("Продукт успішно додано!")
            else:
                ui.show_message("Помилка при додаванні продукту.")

        elif action == "2":
            # 1. Просимо Service дістати дані з бази
            products = service.get_all_products()
            # 2. Просимо UI показати ці дані
            ui.show_products(products)

        elif action == "0":
            print("Вихід з програми.")
            break

        else:
            print("Некоректна дія. Спробуйте ще раз.")




if __name__ == "__main__":
    main()