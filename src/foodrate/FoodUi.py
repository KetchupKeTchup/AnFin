

class FoodUi:
    def display_menu(self):
        #Початковий інтерфейс
        print("*" * 50)
        print("1. Записати продукт\n"
              "2. Перегляд всіх записів\n"
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