class City:
    def __init__(self, name):
        self.name = name

    def handle_message(self):
        return self.name

class Strasbourg(City):
    def __init__(self):
        super().__init__("Страсбург")

class Toulouse(City):
    def __init__(self):
        super().__init__("Тулуза")

class Marseille(City):
    def __init__(self):
        super().__init__("Марсель")

class Birmingham(City):
    def __init__(self):
        super().__init__("Бірмінгем")

class Manchester(City):
    def __init__(self):
        super().__init__("Манчестер")

class Canberra(City):
    def __init__(self):
        super().__init__("Канберра")

class Sydney(City):
    def __init__(self):
        super().__init__("Сідней")

class Melbourne(City):
    def __init__(self):
        super().__init__("Мельбурн")

class Europe:
    def __init__(self):
        self.cities = [Strasbourg(), Toulouse(), Marseille(), Birmingham(), Manchester()]

    def handle_messages(self):
        return [city.handle_message() for city in self.cities]

class Australia:
    def __init__(self):
        self.cities = [Canberra(), Sydney(), Melbourne()]

    def handle_messages(self):
        return [city.handle_message() for city in self.cities]

# Виклик обробників для міст
strasbourg = Strasbourg()
toulouse = Toulouse()
marseille = Marseille()
birmingham = Birmingham()
manchester = Manchester()
canberra = Canberra()
sydney = Sydney()
melbourne = Melbourne()

print(strasbourg.handle_message())
print(toulouse.handle_message())
print(marseille.handle_message())
print(birmingham.handle_message())
print(manchester.handle_message())
print(canberra.handle_message())
print(sydney.handle_message())
print(melbourne.handle_message())

# Виклик обробників для Європи та Австралії
europe = Europe()
australia = Australia()

print(europe.handle_messages())
print(australia.handle_messages())
