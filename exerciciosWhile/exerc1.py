n = int(input("Fatorial de: ") )

fatorial=1
count=1

while (count <= n):
    fatorial *= count #fatorial = fatorial * count
    count = count + 1

print(fatorial)