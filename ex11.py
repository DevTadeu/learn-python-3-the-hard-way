# Colocamos end=' ' no final de cada linha print. Isso informa ao print
# para não terminar a linha com um caractere de nova linha e ir para a próxima.
print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
height = input()
print("How much do you weigh?", end=' ')
weight = input()
print(f"So, you're {age} old, {height} tall and {weight} heavy.")
