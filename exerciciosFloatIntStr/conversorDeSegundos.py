segundos= input("Por favor, entre com o numero de segundos que deseja converter: ") 
total_segs = int(segundos)

dias = total_segs // 86400
dias_restantes = total_segs% 86400
horas = total_segs // 3600
segs_restantes = total_segs% 3600
minutos = segs_restantes // 60
seg_restantes_final = segs_restantes % 60

print(dias, "dias,", horas, "horas,", minutos, "minutos e ", seg_restantes_final, "segundos.")