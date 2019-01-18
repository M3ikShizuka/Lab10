#####################################################################################################################
################################################## Test data: #######################################################
#####################################################################################################################
### Count: 6
###  Result: 1 2 1
#Перекресток Короленко 15 2000
#Перекресток Короленко 20 2500
#Перекресток Короленко 25 3000
#Пятёрочка Короленко 15 2100
#Пятёрочка Короленко 20 2500
#Пятёрочка Короленко 25 3100
###  Count: 4
###  Result: 1 2 0
#Перекресток Короленко 15 2000
#Перекресток Короленко 20 2500
#Пятёрочка Короленко 15 2100
#Пятёрочка Короленко 20 2500
#####################################################################################################################
##################################################### Data: #########################################################
#####################################################################################################################
class CStores:
    firm = None
    street = None
    fat = None
    price = None

    def __init__(self, firm, street, fat, price):
        self.firm = firm
        self.street = street
        self.fat = fat
        self.price = price
#####################################################################################################################
##################################################### Funcs: ########################################################
#####################################################################################################################
def main():
    stores_count = int(input("Количество магазинов: "))
    store_list = list()
    top_price_dict = {15:5000, 20:5000, 25:5000}
    top_stores = {15:0, 20:0, 25:0}

    store_index = 0
    while store_index < stores_count:
        store_index += 1

        input_string = input()
        price = None

        # Обработка данных участника.
        firm, street, fat, price = input_string.split(" ")
        fat = int(fat)
        price = int(price)

        if len(firm) > 20:
            print("Название фирмы слишком длинная!")
            print("Повторите попытку ввода.")
            continue

        if len(street) > 20:
            print("Название улицы слишком длинная!")
            print("Повторите попытку ввода.")
            continue

        if fat != 15 and fat != 20 and fat != 25:
            print("Не верная жирность!")
            print("Повторите попытку ввода.")
            continue

        if price < 2000 or price > 5000:
            print("Не верная цена!")
            print("Повторите попытку ввода.")
            continue
        
        # Инициализация объектов класса учаник.
        store = CStores(firm, street, fat, price)
        store_list.append(store)
        # Находим минимальную цену
        if top_price_dict[fat] > price:
            top_price_dict[fat] = price

    for store in store_list:
        if top_price_dict[store.fat] == store.price:
            top_stores[store.fat] += 1

    print(top_stores[15], top_stores[20], top_stores[25])
#####################################################################################################################
##################################################### Exec: #########################################################
#####################################################################################################################
main()