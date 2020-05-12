
def bonAppetit(bill, k, b):
    bill.pop(k)
    subTotal = sum(bill)
    annaTotal = int(subTotal / 2)
    if annaTotal == b:
        print("Bon Appetit")
    else:
        print(str(b-annaTotal))

