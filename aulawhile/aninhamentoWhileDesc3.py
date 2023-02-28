
def tabuada():
    tab = 1
    while tab <= 10:
        print(tab,":","=", end= "\t") #são as quebras de linha/ descrições
        i = 1 
        while i <= 10:
            print (tab*i, end = "\t")
            i = i + 1
        
        print()
        tab = tab + 1   #tem que ficar de fora, se nao ele nao repete.
tabuada()
