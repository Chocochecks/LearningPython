def get_total_page(ntotal,npage):
    numberpage = ntotal//npage
    if ntotal % npage > 0:
        numberpage += 1
    return numberpage


print(get_total_page(5,10))
print(get_total_page(15,10))
print(get_total_page(25,10))
print(get_total_page(30,10))