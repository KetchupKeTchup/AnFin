from src.foodrate.FoodService import FoodService
from src.foodrate.FoodUi import FoodUi
from src.UI.main_window import MainWindow

def main():
    ui_Food = FoodUi()
    ui = MainWindow()
    service = FoodService()

    while True:
        action = ui.display_menu()

        if action == "1":
            
            while True:
                action = ui_Food.display_menu_food()
                
                if action == "1":
                            # 1. Просимо UI зібрати дані
                            product_data = ui_Food.get_product_data()
                
                            if product_data is not None:
                                service.add_product(*product_data)
                                ui_Food.show_message("Продукт успішно додано!")
                            else:
                                ui_Food.show_message("Помилка при додаванні продукту.")
                elif action == "2":
                    # 1. Просимо Service дістати дані з бази
                    products = service.get_all_products()
                    # 2. Просимо UI показати ці дані
                    ui_Food.show_products(products)
                elif action == "3":
                    # 1. Просимо Service дістати дані з бази
                    total_calories = service.get_total_calories()
                    # 2. Просимо UI показати ці дані
                    ui_Food.show_total_calories(total_calories)

                elif action == "0":
                            print("Вихід з програми.")
                            break


        elif action == "2":
            print("В розробці.")
            return 
                    
        
        elif action == "0":
            print("Вихід з програми.")
            break

        else:
            print("Некоректна дія. Спробуйте ще раз.")




if __name__ == "__main__":
    main()