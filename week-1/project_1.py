user = input('What is your Name Sir?:')
print('Welcome to the Finance Calculator Sir',user )

def simple_interest(principal, rate, time):
    si = principal * (1 + ((rate / 100) * time))
    return si

def compound_interest(principal, rate, time, n):
    ci = principal * ((1 + ((rate / 100) / n ))**(n * time))
    return ci

def annuity_plan(payment, rate, time, n):
    r = rate / 100 
    fv = payment * (((1 + r/n)**(n * time) - 1) / (r/n))
    return fv

P = float(input("Enter Principal: "))
R = float(input("Enter Rate of Interest: "))
T = float(input("Enter Time in years: "))
n = int(input("Enter number of times interest is compounded per year: "))
PMT = float(input("Enter Annuity Payment: "))

print(f"Simple Interest: {simple_interest(P, R, T):.2f}")
print(f"Compound Interest: {compound_interest(P, R, T, n):.2f}")
print(f"Annuity Future Value: {annuity_plan(PMT, R, T, n):.2f}") 