def verificar_número(): 
    num = int(input("informe um número inteiro: ")) 
    if num > 0: 
        print("o número e positivo.")
    elif num < 0:
        print("0 número é negativo.") 
    else: 
        print("o número é zero.") 

        verificar_número() 