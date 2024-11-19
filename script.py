# import pdb; pdb.set_trace() 

def divide_numbers(a, b):
    """
    Divise deux nombres, avec une gestion d'erreur pour éviter la division par zéro.
    """
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        print("Erreur : Division par zéro détectée.")
    return result

def main():
    print("Bienvenue dans le test de débogage !")
    
   
    numbers = [10, 5, 0, 3]
    
    total = 0

    for i in range(len(numbers)):
        print(f"Étape {i + 1} :")
  
        a = numbers[i]
        b = numbers[i - 1] if i > 0 else 1 
        print(f"Diviser {a} par {b}")

       
        result = divide_numbers(a, b)
        if result is not None:
            total += result

    print(f"Somme totale des résultats : {total}")

if __name__ == "__main__":
    main()
