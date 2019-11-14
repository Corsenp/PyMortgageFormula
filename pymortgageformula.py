
# calculating the fixed monthly payments
def fixed_monthly_payments_formula(P, r, n):
    top = (1 + r)**n
    bottom = (((1 + r)**n) - 1)
    division = top / bottom
    result = P * r * division
    return result

def oustanding_loan_balance_formula(m, P, r, n):
    top = ((1 + r)**n - (1 + r)**m)
    bottom = (((1 + r)**n) - 1)
    division = top / bottom
    result = P * division
    return result

# get the principal of the loan
def get_principal():
    P = input("What is the principal ?\n")

    try:
        P = int(P)
        return P

    except ValueError:
        print("ERROR : not a correct Value\n")

# get the outstanding month
def get_outstanding_month():
    m = input("What month do you want to check the Oustanding ?\n")

    try:
        m = int(m)
        return m

    except ValueError:
        get_outstanding_month()

# get the monthly interest rate of the loan
def get_interest_rate():
    r = input("What is the monthly interest rate ?\n")

    try:
        r = float(r)
        return r
    
    except ValueError:
        print("ERROR : Not a correct Value\n")
        get_interest_rate()

# get the number of months
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
    m = get_outstanding_month()

    try:
        monthly_payments = fixed_monthly_payments_formula(P, r, n)
        oustanding = oustanding_loan_balance_formula(m, P, r, n)
        print("Fixed monthly payments = %s"% monthly_payments)
        print("Oustanding = %s"% oustanding)

    
    except:
        print("ERROR while calculating the fixed_monthly_payments_formula or the oustanding")
        return

    

main()