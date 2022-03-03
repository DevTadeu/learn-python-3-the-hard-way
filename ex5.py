name = 'Márcio'
age = 41
height = 174
weight = 124
eyes = 'castanhos'
teeth = 'branco'
hair = 'castanhos claros'

total_hei_pol = height * 2.54 # total da altura em polegadas
total_wei_lib = weight * 2.20 # total do peso em libras
print(f"Let's talk about {name}.")
print(f"He's {height} centimetros e em polegadas {total_hei_pol} inches tall.")
print(f"He's {weight} kilos e {total_wei_lib} em libras pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")
