def vyhra(list, x, y, hrac):
    """
    vysvětlím princip
    v podstatě kontroluji poslední místo, kam hráči zahráli, vždy o čtyři místa do všech různých světových stran = (S,J,V,Z,SV atd.)
    pokud jsme zjistili, že v některých ze směrů, je čtyři a více stejných křížků nebo koleček (záleží na hráči), pak víme,
    že hráč vyhrál
    """
    if (hrac==1):
        hrac = 2
    else:
        hrac = 1
    d1 = diagonala1(list, x, y, hrac) # zde kontroluji směr od SZ do JV
    d2 = diagonala2(list, x, y, hrac) # zde kontroluji směr od SV do JZ
    r = radek(list, x, y, hrac) # kontrola horizontální
    s = sloupec(list, x, y, hrac) # kontrola vertikální

    # pokud některá z funkcí najde pět za sebou jdoucích X nebo O tak vrátí True, jakože někdo vyhrál
    if (d1):
        return True
    elif (d2):
        return True
    elif (r):
        return True
    elif (s):
        return True
    else:
        return False

# všechny funkce fungují v podstatě stejně, akorát for loop kouká na jiné strany
# princip je ovšem stejný
# podrobné vysvětlení u funkce radek
def diagonala1(list, x, y, hrac): # stejný princip hledání, ale kouká se ze směru SZ-JV
    count = 0
    for i in range(1,5):
        if (x+i <= 14 and y+i <= 14):
            if (hrac==list[y+i][x+i]):
                count += 1
            else:
                break
    for i in range(1,5):
        if (x-i >= 0 and y-i >= 0):
            if (hrac==list[y-i][x-i]):
                count += 1
            else:
                break
    if (count >= 4):
        return True
    return False    

def diagonala2(list, x, y, hrac): # stejný princip hledání, ale kouká se ze směru SV-JZ
    count = 0 
    for i in range(1,5):
        if (x-i >= 0 and y+i <= 14):
            if (hrac==list[y+i][x-i]):
                count += 1
            else:
                break
    for i in range(1,5):
        if (x+i <= 14  and y-i >= 0):
            if (hrac==list[y-i][x+i]):
                count += 1
            else:
                break
    if (count >= 4):
        return True
    return False

def radek(list, x, y, hrac):
    count = 0 # počítadlo X nebo O záleží na hráči
    for i in range(1,5): # for loop, který bude koukat na ose x doprava
        if (x+i <= 14): # tahle podmínka je zde, abychom se neocitli mimo hrací plochu
            if (hrac==list[y][x+i]): # kouká do mého seznamu, kde se ukládají data o hře
                # hráč 1 má čislo 1 a hráč 2 číslo 2 a podle toho se mi ukládají i v seznamu
                # pokud daný hráč bude mít vedle posledního zahraného místa (jeho posledního tahu) jiný X (nebo O)
                count += 1 # počítadlo započte, že se vedle nachází jeho symbol
            else:
                break # kdyby vedle posledního zahraného místa nebyl jeho symbol, přeruší hledání loopu
    for i in range(1,5): # to samé, jako nahoře, ale pro druhý směr 
        # nahoře koukal doprava, zde kouká doleva
        if (x-i >= 0):
            if (hrac==list[y][x-i]):
                count += 1
            else:
                break
    if (count >= 4): # pokud našel více jak (nebo přesně) 4 symboly vedle sebe víme, že vyhrál
        return True
    return False

def sloupec(list, x, y, hrac): # zde se opakuje přesně to samé, ale pro sloupec, takže kouká na osu y
    count = 0 
    for i in range(1,5):
        if (y+i <= 14):
            if (hrac==list[y+i][x]):
                count += 1
            else:
                break
    for i in range(1,5):
        if (y-i >= 0):
            if (hrac==list[y-i][x]):
                count += 1
            else:
                break
    if (count >= 4):
        return True
    return False
        