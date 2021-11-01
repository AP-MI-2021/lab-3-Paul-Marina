def verif_prim(n):
    """
    Verifica daca un numar introdus este prim sau nu
    :param n: numar natural
    :return: True daca numarul introdus e prim, iar False in caz contrar
    """
    if n == 1 :
        return False
    elif n == 2 :
        return True
    elif n % 2 == 0 :
        return False
    for i in range(3, n//2):
        if n % i == 0 :
            return False
    return True

def  get_longest_sum_is_prime(list):
    """
    Determinare cea mai lungă subsecvență de numere ce au suma un nr prim
    :param list: lista cu numere intregi
    :return: Cea mai lungă subsecvență de numere ce au suma un nr prim
    """
    rezultat=[]
    s=0
    l = 0
    maxim = 0
    for i in range(len(list)):
        s = 0
        for j in range(i, len(list)):
                s = s + list[j]
                if verif_prim(s):
                    if j-i+1 > maxim:
                        maxim = j - i + 1
                        l = i
        for i in range(l,l+maxim):
            rezultat.append(list[i])
        return rezultat

def test_get_longest_sum_is_prime():
    assert get_longest_sum_is_prime([2, 3, 7]) == [2, 3]
    assert get_longest_sum_is_prime([1, 2, 3]) == [1, 2]

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
    determinare cea mai lungă subsecvență de numere ce numarul de cifre in ordine descrescatoare
    :param list: numere naturale
    :return: Cea mai lungă subsecvență de numere ce numarul de cifre in ordine descrescatoare
    """
    l=0
    rezul=[]
    maxim = 0
    for i in range(len(list)):
        for j in range(i+1, len(list)):
             if nrcifre(list[j-1]) > nrcifre(list[j]):
                 if j - i + 1 > maxim:
                     maxim = j - i + 1
                     l = i
             else:
                 break
    for i in range(l, l + maxim):
        rezul.append(list[i])
    return rezul


def test_get_longest_digit_count_desc():
    assert get_longest_digit_count_desc([123, 12, 1]) == [123, 12, 1]
    assert get_longest_digit_count_desc([123, 12, 123]) == [123, 12]

def get_longest_sorted_asc(list):
    """
    Determina cea mai lungă subsecvență de numere care sunt in ordine crescatoare
    :param list: numere naturale
    :return: Cea mai lungă subsecvență de numere care sunt in ordine crescatoare
    """
    rezu=[]
    l=0
    maxim = 0
    for i in range(len(list)):
        for j in range(i + 1, len(list)):
            if list[j - 1] < list[j]:
                if j - i + 1 > maxim:
                    maxim = j - i + 1
                    l = i
            else:
                break
    for i in range(l, l + maxim):
        rezu.append(list[i])
        return rezu

def test_get_longest_sorted_asc():
    assert get_longest_sorted_asc([1, 2, 3]) == [1, 2, 3]
    assert get_longest_sorted_asc([1, 3, 2]) == [1, 3]

def main():
    while True:
        list = []
        n = int(input("Dati numar de elemente : "))
        for i in range(n):
            list.append(int(input("Dati elemente : ")))
        print(test_get_longest_sum_is_prime())
        print(test_get_longest_digit_count_desc())
        print(test_get_longest_sorted_asc())
        print("1.Afiseaza cea mai lungă subsecvență de numere ce au suma un nr prim.")
        print("2.Afiseaza cea mai lungă subsecvență de numere ce au numarul de cifre in ordine descrescatoare.")
        print("3.Afiseaza cea mai lungă subsecvență de numere care sunt in ordine crescatoare.")
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


main()
