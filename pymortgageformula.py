
def fixed_monthly_payments_formula(P, r, n):
    top = (1 + r)**n
    bottom = (((1 + r)**n) - 1)
    division = top / bottom
    result = P * r * division
    return result

def get_principal():
    P = input("What is the principal ?\n")

    try:
        P = int(P)
        return P

    except ValueError:
        print("ERROR : not a correct Value\n")

def get_interest_rate():
    r = input("What is the monthly interest rate ?\n")

    try:
        r = float(r)
        return r
    
    except ValueError:
        print("ERROR : Not a correct Value\n")
        get_interest_rate()

def get_number_months():
    n = input("What is the number of months\n")

    try:
        n = int(n)
        return n

    except ValueError:
        print("ERROR : Not a correct Value\n")
        get_number_months()

def main():
    P = get_principal()
    r = get_interest_rate() / 100
    n = get_number_months()

    try:
        result = fixed_monthly_payments_formula(P, r, n)
        print("Fixed monthly payments = %s"% result)
    
    except:
        print("ERROR while calculating the fixed_monthly_payments_formula")
        return

    

main()