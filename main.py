
def verif_prim(n):
    """
    Verifica daca un numar introduc este prim sau nu
    :param n: numar natural
    :return: True daca numarul introdus e prim, iar False in caz contrar
    """
    if n == 1 :
        return False
    elif n == 2 :
        return True
    elif n % 2 == 0 :
        return False
    for i in range (3,n//2):
        if n % i == 0 :
            return False
    return True

def  get_longest_sum_is_prime(list):
    """
    Verifica daca suma numerelor este număr prim.
    :param list: numere naturale
    :return: True daca suma este un numar prim, iar False in caz contrar
    """
    sumaelem=0
    for i in range(len(list)):
        sumaelem=sumaelem+list[i]
    if verif_prim(sumaelem) == True:
        return True
    else :
        return False
def test_get_longest_sum_is_prime():
    assert get_longest_sum_is_prime([1, 3, 3]) is True
    assert get_longest_sum_is_prime([1, 2, 3]) is False
def nrcifre(n):
    """
    Calculez nr de cifre a numarului introdus
    :param n: numar natural
    :return: numarul de cifre al numarului n
    """
    k = n
    nr = 0
    while k != 0:
      k //= 10
      nr =nr + 1
    return nr
def get_longest_digit_count_desc(list):
    """
    Verifica daca numerele alaturate dintr o lista au numarul de cifre in ordine descrescatoare
    :param list: numere naturale
    :return: daca numerele alaturate dintr o lista au numarul de cifre in ordine descrescatoare afiseaza True, in caz contrar False
    """
    for i in range(len(list)-1):
        if nrcifre(list[i]) < nrcifre(list[i+1]):
            return False
    return True

def test_get_longest_digit_count_desc():
    assert get_longest_digit_count_desc([123, 12, 1]) is True
    assert get_longest_digit_count_desc([123, 12, 123]) is False

def get_longest_sorted_asc(list):
    """
    verifica daca numerele din lista sunt in ordine crescatoare
    :param list: numere naturale
    :return: True daca numerele sunt ordonate crescator, False in caz contrat
    """
    for i in range(len(list)-1):
        if list[i] > list[i+1]:
            return False
    return True

def test_get_longest_sorted_asc():
    assert get_longest_sorted_asc([1, 2, 3]) is True
    assert get_longest_sorted_asc([1, 3, 2]) is False
def main():
    while True:
        list = []
        n = int(input("Dati numar de elemente : "))
        for i in range(n):
            list.append(int(input("Dati elemente : ")))
        print(test_get_longest_sum_is_prime())
        print(test_get_longest_digit_count_desc())
        print(test_get_longest_sorted_asc())
        print("1.verifica daca suma numerelor este număr prim.")
        print("2.verifica daca numărul de cifre ale numerelor din lista este în ordine descrescătoare.")
        print("3.verifica daca numerele sunt ordonate crescator.")
        print("x.iesire")
        optiune = input("dati optiune : ")
        if optiune == "1":
           print(get_longest_sum_is_prime(list))
        elif optiune == "2":
           print(get_longest_digit_count_desc(list))
        elif optiune == "3":
           print(get_longest_sorted_asc(list))
        elif optiune == "x":
         break
        else :
         print("Optiune gresita, reincercati.")
if main():
    main()
