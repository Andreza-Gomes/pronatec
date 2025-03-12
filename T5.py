def calcular_media(notal,nota2,nota3):
    media = (notal + nota2 + nota3) / 3 
    if media >= 7: 
        situação = "aprovado" 
    else:
        situação = "reprovado" 
        return media, situação 
    # Exemplo de uso: 
    nota1 = 8 
    nota2 = 7 
    nota3 = 9 
    media, situação =    calcular_media(nota1, nota2, nota3) 
    print(f"media: {media: .2f}")
    print(f"situação: {situação}") 
