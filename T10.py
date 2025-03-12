def calcular_litros(preço_litro,
     valor_abastecer):
    return valor_abastecer/preço_litro

preço_litro = float(input("digite o preço do litro do combustivel: R$")) 
valor_abastecer = float(input("digite o valor em dinheiro que sedeseja abastecer: R%")) 

print(f"serão comprados{calcular_litros(preço_litro,valor_abastecer):.2f} litros de combustivel.") 
