segundos = int(input("Por favor, entre com o numero de segundos que deseja converter: "))

dias, segundos = divmod(segundos, 86400)
horas, segundos = divmod(segundos, 3600)
minutos, segundos = divmod(segundos, 60)

print(f'{dias} dias, {horas} horas, {minutos} minutos e {segundos} segundos')