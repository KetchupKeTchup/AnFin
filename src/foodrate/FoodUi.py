

class FoodUi:
    
    def display_menu_food(self):
        #Початковий інтерфейс
        print("*" * 50)
        print("1. Записати продукт\n"
              "2. Перегляд всіх записів\n"
              "3. Загальна кількість калорій\n"
              "0. Вийти")
        print("*" * 50)
        return input("Введіть дію: ")

    def get_product_data(self):
        # Збираємо данні про продукт
        try:
            product = input("Продукт: ")
            mass = float(input("Вага: "))
            kkal = float(input("Кількість ккалорій на 100г: "))
            protein = float(input("Кількість білків на 100г: "))
            sacharidy = float(input("Кількість вугливодів на 100г: "))
            fat = float(input("Кількість жирів на 100г: "))
            return product, mass, kkal, protein, sacharidy, fat
        
        except ValueError:
            print("Помилка: введено некоректне значення. Будь ласка, введіть числові значення для ваги та харчових показників.")
            return None

    def show_message(self, message):
        print(message)

    def show_products(self, products):
        if products:
            print("Список продуктів:")
            for product in products:
                print(f"ID: {product[0]}, Продукт: {product[1]}, Вага: {product[2]}г, Ккал: {product[3]}, "
                      f"Білки: {product[4]}г, Вуглеводи: {product[5]}г, Жири: {product[6]}г, Дата: {product[7]}")
        else:
            print("Немає записів у базі даних.")

    def show_total_calories(self, total_calories):
        if total_calories:
            print("Загальна кількість калорій:")
            print(f"Калорії: {total_calories[0]:.2f}")
            print(f"Білки: {total_calories[1]:.2f}г")
            print(f"Вуглеводи: {total_calories[2]:.2f}г")
            print(f"Жири: {total_calories[3]:.2f}г")
        else:
            print("Немає записів у базі даних.")