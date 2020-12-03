def MaximumDiscount(N:int, price:int):
    price_sort = sorted(price, reverse=True)
    sale = 0
    for i in range(2, N, 3):
        sale += price_sort[i]
    return sale