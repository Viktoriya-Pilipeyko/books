# Бесполезные факты
#
# Узнает у пользователя его / ее личные данные и выдает несколько фактов #о нем / ней. Эти факты истинны. но совершенно бесполезны.

name = input( "Привет. Как тебя зовут? ")
age = input("Сколько тебе лет? ")
age = int(age)
weight = int(input("Xopoшo. и последний вопрос. Сколько в тебе килограммов?"))

print('\nЕсли бы поэт Камминг решил адресовать тебе письмо, он бы обратился к тебе так: ', name.lower())
print('А если бы это был рехнувшийся Каммингс. то так: ', name.upper())
print('\nЕсли бы маленький ребенок решил привлечь твое внимание')
print('он произнес бы твое имя так:')
print(name * 5)

seconds = age * 365 * 24 * 60 * 60

print('\nТвой нынешний возраст - свыше', seconds, 'секунд')

moon_weight = weight / 6
sun_weight = weight * 27.1

print('\nЗнаете ли Вы, что на Луне вы бы весили всего', moon_weight, 'кг?')
print('А вот находясь на Солнце, вы бы весили', sun_weight, 'кг. (Но, увы, это продолжалось бы недолго...)')

input( "\n\nНажмите Enter. чтобы выйти.")