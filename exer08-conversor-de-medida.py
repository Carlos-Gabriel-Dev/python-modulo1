try : 

    metros = float(input("Quantos metros :"))

    centimetros = metros * 100

    milimetro = metros * 1000
    
except : 
    
    print('Apenas numeros')
    
else : 

    print(f"A sua parede tem {metros} metros isso em centimetros é {centimetros} que por sua vez em milimetros é {milimetro}")