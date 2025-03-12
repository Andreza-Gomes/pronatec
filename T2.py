def verificar_paridade(número): 
    if número % 2==0: 
        return "par"
    else: 
        return "impar" 
    
número = int(input("5:"))
print(verificar_paridade(número))