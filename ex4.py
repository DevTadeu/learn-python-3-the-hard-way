# quantidade de carros
cars = 100
# espaço no carro
space_in_a_car = 4.0
# motoristas
drivers = 30
# passageiros
passengers = 90
# carros não dirigidos é o resultado da quantidade de carros - motoristas
cars_not_driven = cars - drivers
# carros dirigidos = ao numero de motoristas
cars_driven = drivers
# quantidade de pessoas transportadas
carpool_capacity = cars_driven * space_in_a_car
# passageiros medios por carro
average_passengers_per_car = passengers / cars_driven

# quantidade de carros para usar
print("There are", cars, "cars available.")
# quantidade de motoristas disponiveis
print("There are only", drivers, "drivers available.")
# quantidade de carros vazios
print("There will be", cars_not_driven, "empty cars today.")
# quantidade de pessoas transportadas
print("We can transport", carpool_capacity, "people today.")
# quantidade de passageiros 
print("We have", passengers, "to carpool today.")
# quantidade de lugares livres no carros a ser usado (fora o motorista)
print("We need to put about", average_passengers_per_car, "in each car.")
