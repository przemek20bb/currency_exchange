def parsowanie_listy_walut(waluta):
    if len(waluta) < 20:
        while len(waluta) < 20:
            waluta += " "
    return waluta



