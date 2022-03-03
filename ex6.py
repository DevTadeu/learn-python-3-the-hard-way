# A variavel tipos de pessoas tem o valor de 10 (dez tipos de pessoas)
types_of_people = 10
# a variavel x esta formatada f e o que esta entre "" é a string
# e dentro dela esta o valor da variavel types_of_people
x = f"There are {types_of_people} types of people."
# a variavel binary é definido pela string "binary"
binary = "binary"
# a variavel do_not é definido pela string "dont't"
do_not = "don't"
# a variavel y esta formatada f e o que esta entre "" é a string
# e dentro dela esta o valor da variavel binary entre{string} e dont_t{string}
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)
# saira na tela a string do print e dentro a string de x
print(f"I said: {x}")
# saira na tela a string do print e dentro a string de y que na qual
# esta contido o string de binary e o string de dont_t
print(f"I also said: {y}")
# a variavel hilarious esta definido como false
hilarious = False
#
joke_evaluation = "Isn't that joke so funny?! {}"
#
print(joke_evaluation.format(hilarious))
#
w = "This is the left side of..."
#
e = "a string with a right side."
# o print é a soma das strings das variaveis w e e
print(w + e)
