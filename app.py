def shippingCharge(pp, dr, sc):
        total = pp*((100-dr)/100)+sc
        print(total)

shippingCharge(1000, 5, 50)