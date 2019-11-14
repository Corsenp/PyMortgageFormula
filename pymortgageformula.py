
def fixed_monthly_payments_formula(P, r, n):
    print("fixed_monthly_payments_formula def")
    top = (1 + r)**n
    bottom = ((1 + r)**n - 1)
    result = top / bottom
    return result

def get_principal():
    P = input("What is the principal ?\n")

    try:
        float(P)
        return P

    except ValueError:
        print("ERROR : not a correct Value\n")

def get_interest_rate():
    r = input("What is the monthly interest rate ?\n")

    try:
        float(r)
        return r
    
    except ValueError:
        print("ERROR : Not a correct Value\n")
        get_interest_rate()

def get_number_months():
    n = input("What is the number of months\n")

    try:
        float(n)
        return n

    except ValueError:
        print("ERROR : Not a correct Value\n")
        get_number_months()

def main():
    P = get_principal()
    r = get_interest_rate()
    n = get_number_months()

    print("P = %s"% P)
    print("r = %s"% r)
    print("n = %s"% n)

    

main()