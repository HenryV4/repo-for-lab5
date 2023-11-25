class Flower:
    def __init__(self, name, height, size, color, price, quantity, delivery_rate):
        self.name = name
        self.height = height
        self.size = size
        self.color = color
        self.price = price
        self.quantity = quantity
        self.delivery_rate = delivery_rate


class FlowerShop:
    def __init__(self):
        self.stock = []

    def add_flower(self, flower, quantity):
        self.stock.extend([flower] * quantity)

    def remove_flower(self, flower):
        if flower in self.stock:
            self.stock.remove(flower)

    def get_the_most_expensive_flowers(self, n=1):
        sorted_flowers = sorted(
            self.stock, key=lambda flower: flower.price, reverse=True
        )
        return sorted_flowers[:n]


class Bouquet:
    def __init__(self):
        self.flowers = []

    def add_flower(self, flower, quantity=1):
        self.flowers.extend([flower] * quantity)

    def get_the_most_expensive_flower(self, n=1):
        sorted_flowers = sorted(
            self.flowers, key=lambda flower: flower.price, reverse=True
        )
        return sorted_flowers[:n]

    def get_bouquet_description(self):
        flower_list = "\n".join(
            [
                f"{flower.color} {flower.name} for {flower.price}$"
                for flower in self.flowers
            ]
        )
        return f"Bouquet contents:\n{flower_list}"

    def calculate_total_price(self):
        total_price = sum(flower.price for flower in self.flowers)
        return total_price


def main():
    flower_shop = FlowerShop()
    rose = Flower("rose", 7, "medium", "red", 1, 3, 2)
    tulip1 = Flower("tulip", 9, "small", "yellow", 2, 4, 1)
    tulip2 = Flower("tulip", 6, "small", "purple", 3, 5, 1)
    flower_shop.add_flower(rose, 10)
    flower_shop.add_flower(tulip1, 20)
    flower_shop.add_flower(tulip2, 10)

    bouquet = Bouquet()
    bouquet.add_flower(rose, quantity=1)
    bouquet.add_flower(tulip1, quantity=1)
    bouquet.add_flower(tulip2, quantity=1)

    expensive_flowers = flower_shop.get_the_most_expensive_flowers(n=3)
    print("Top 3 expensive flowers in the flower shop:")
    for flower in expensive_flowers:
        print(f"{flower.color} {flower.name} - {flower.price} $")

    most_expensive_bouquet_flower = bouquet.get_the_most_expensive_flower(n=3)
    print("Top 3 expensive flowers in the bouquet:")
    for flower in most_expensive_bouquet_flower:
        print(f"{flower.color} {flower.name} - {flower.price} $")

    print(bouquet.get_bouquet_description())

    print(f"Total sum of your bouquet is {bouquet.calculate_total_price()} $")


if __name__ == "__main__":
    main()
