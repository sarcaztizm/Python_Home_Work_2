# Иван Васильевич пришел на рынок и решил купить два арбуза:
# один для себя, а другой для тещи. Понятно, что для себя нужно выбрать арбуз потяжелей,
# а для тещи полегче. Но вот незадача: арбузов слишком много и он не знает
# как же выбрать самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество арбузов.
# Вторая строка содержит N чисел, записанных на новой строчке каждое.
# Здесь каждое число – это масса соответствующего арбуза
# Input: 5 -> 5 1 6 5 9
# Output: 1 9

N = int(input('Количество выбранных арбузов: '))
print('Введите вес каждого арбуза')
weight = []

for i in range(N):
    weight.append(int(input()))

min = min(weight)
print('Арбуз для тещи: ',min)
max = max(weight)
print('Арбуз для себя',max)

