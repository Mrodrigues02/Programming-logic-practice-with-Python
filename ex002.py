d = int(input('Qantos dias?'))
h = int(input('Quantas horas?'))
m = int(input('Qantos minutos?'))
s = int(input('Qantos segundos?'))
t = s+(m * 60)+(h * 60 * 60)+(d * 24 * 60 * 60)
print('O total de segundos calculado é de {}.'.format(t))