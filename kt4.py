from datetime import date

# класс автомобиль
class Car:
    def __init__(self, license_plate, brand, model, car_type, price_per_day):
        self._license_plate = license_plate
        self._brand = brand
        self._model = model
        self._car_type = car_type
        self._price_per_day = price_per_day
        self._is_available = True
    
    # проверка доступности на период
    def is_available_for_period(self, start_date, end_date, rentals):
        if not self._is_available:
            return False
        
        for rental in rentals:
            if rental._car._license_plate == self._license_plate:
                # проверка пересечения дат
                if not (end_date < rental._start_date or start_date > rental._end_date):
                    return False
        return True
    
    def __str__(self):
        return f"{self._brand} {self._model} ({self._car_type}) - {self._license_plate}"


# класс клиент
class Client:
    def __init__(self, full_name, passport_id):
        self._full_name = full_name
        self._passport_id = passport_id
    
    def __str__(self):
        return f"{self._full_name} (паспорт: {self._passport_id})"


# класс аренда
class Rental:
    _next_id = 1
    
    def __init__(self, client, car, start_date, end_date):
        self._rental_id = Rental._next_id
        Rental._next_id += 1
        self._client = client
        self._car = car
        self._start_date = start_date
        self._end_date = end_date
    
    def __str__(self):
        return f"Аренда #{self._rental_id}: {self._client._full_name} - {self._car} с {self._start_date} по {self._end_date}"


# класс сервис проката
class CarRentalService:
    def __init__(self):
        self._cars = []  # список автомобилей
        self._rentals = []  # список аренд
    
    # добавить автомобиль
    def add_car(self, car):
        self._cars.append(car)
    
    # удалить автомобиль
    def remove_car(self, license_plate):
        for car in self._cars:
            if car._license_plate == license_plate:
                self._cars.remove(car)
                break
    
    # поиск свободных автомобилей
    def find_available_cars(self, start_date, end_date, car_type=None):
        available = []
        for car in self._cars:
            if car.is_available_for_period(start_date, end_date, self._rentals):
                if car_type is None or car._car_type == car_type:
                    available.append(car)
        return available
    
    # создать аренду
    def rent_car(self, client, license_plate, start_date, end_date):
        for car in self._cars:
            if car._license_plate == license_plate:
                if car.is_available_for_period(start_date, end_date, self._rentals):
                    rental = Rental(client, car, start_date, end_date)
                    self._rentals.append(rental)
                    car._is_available = False
                    print(f"автомобиль {car} арендован клиентом {client._full_name}")
                    return rental
                else:
                    print(f"автомобиль {license_plate} уже занят в указанный период")
                    return None
        print(f"автомобиль с номером {license_plate} не найден")
        return None
    
    # отменить аренду
    def cancel_rental(self, rental_id):
        for rental in self._rentals:
            if rental._rental_id == rental_id:
                self._rentals.remove(rental)
                rental._car._is_available = True
                print(f"аренда #{rental_id} отменена")
                return True
        print(f"аренда #{rental_id} не найдена")
        return False
    
    def show_all_cars(self):
        print("\nвсе автомобили в автопарке:")
        for car in self._cars:
            print(f"  {car}")
    
    def show_current_rentals(self):
        print("\nтекущие аренды:")
        if not self._rentals:
            print("  нет активных аренд")
        for rental in self._rentals:
            print(f"  {rental}")


# демонстрация работы
if __name__ == "__main__":
    
    # создание сервиса и автомобилей
    service = CarRentalService()
    
    car1 = Car("А001БВ", "Toyota", "Camry", "седан", 2500)
    car2 = Car("А002ГД", "Hyundai", "Creta", "кроссовер", 3000)
    car3 = Car("А003ЕЖ", "Kia", "Rio", "седан", 2000)
    
    # добавление авто в сервис
    service.add_car(car1)
    service.add_car(car2)
    service.add_car(car3)
    
    # создание клиентов
    client1 = Client("Иван Петров", "4510 123456")
    client2 = Client("Мария Сидорова", "4510 654321")
    
    # просмотр всех авто
    service.show_all_cars()
    
    # поиск доступных авто
    start = date(2026, 4, 20)
    end = date(2026, 4, 25)
    
    available = service.find_available_cars(start, end)
    print(f"\nдоступные авто с {start} по {end}:")
    for car in available:
        print(f"  {car}")
    
    # аренда автомобиля
    print("\nКЛИЕНТ АРЕНДУЕТ АВТОМОБИЛЬ")
    service.rent_car(client1, "А001БВ", start, end)
    
    # попытка арендовать уже занятый авто
    print("\nПОПЫТКА АРЕНДОВАТЬ УЖЕ ЗАНЯТЫЙ АВТОМОБИЛЬ")
    service.rent_car(client2, "А001БВ", start, end)
    
    # просмотр текущих аренд
    service.show_current_rentals()
    
    # проверка доступности после аренды
    available_after = service.find_available_cars(start, end)
    print(f"\nдоступные авто с {start} по {end} после аренды:")
    for car in available_after:
        print(f"  {car}")
    
    # отмена аренды
    print("\nОТМЕНА АРЕНДЫ")
    if service._rentals:
        rental_id = service._rentals[0]._rental_id
        service.cancel_rental(rental_id)
    
    # просмотр аренд после отмены
    service.show_current_rentals()
    
    # проверка доступности после отмены
    available_final = service.find_available_cars(start, end)
    print(f"\nдоступные авто с {start} по {end} после отмены:")
    for car in available_final:
        print(f"  {car}")
