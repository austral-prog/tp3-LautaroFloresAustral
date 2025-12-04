def check_vowels():
    name = input("Ingrese un nombre: ")
    name_lower = name.lower()

    print("Contiene a:", "a" in name_lower)
    print("Contiene e:", "e" in name_lower)
    print("Contiene i:", "i" in name_lower)
    print("Contiene o:", "o" in name_lower)
    print("Contiene u:", "u" in name_lower)