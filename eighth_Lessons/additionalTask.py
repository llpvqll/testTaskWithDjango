

class Car:
    color = input('Select color for your car: ')
    max_speed = input('Which speed you need in your car: ')
    horse_power = input('How much horse power you want: ')
    doors_count = input('How much doors you need: ')


class Car_Showroom:
    lst_of_car = ['Audi', 'Mercedes', 'BMW', 'Citroen', 'Reno', 'Ford', 'Maserati']

    def car_for_sale(self):
        select_car = input(f'{Car_Showroom.lst_of_car}\n Select mark of car: ')
        for item in Car_Showroom.lst_of_car:
            if select_car == item:
                return item

car_color = Car.color
sale_car = Car_Showroom().car_for_sale()
doors_in_car = Car.doors_count
maximal_speed = Car.max_speed
car_horse_power = Car.horse_power
print(f'You chose {car_color} {sale_car}. \nWith {doors_in_car} doors. \n{maximal_speed} maximal speed. \nAnd {car_horse_power} horse power!')