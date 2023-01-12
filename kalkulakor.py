prviBroj = int(input("unesi prvi broj: "))
drugBroj = int(input("unesi drugi broj: "))
znak = input("unesi znak: ")

def calc(prviBroj, drugBroj, znak):
    if znak == "+":
        return prviBroj + drugBroj
    elif znak == "-":
        return prviBroj - drugBroj
    elif znak == "*":
        return prviBroj * drugBroj
    elif znak == "/":
        return prviBroj / drugBroj

rez = calc(prviBroj, drugBroj, znak)
print(rez)
