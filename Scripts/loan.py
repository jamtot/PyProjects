def loan(amount,interest_per_annum,years,frequency_per_year):
    interest = interest_per_annum * 0.01
    total = amount * ((1+(interest/frequency_per_year))**(frequency_per_year*years))
    print("The total loan repayment amounts to €"+str(round(total,2)))

if __name__ == "__main__":
    print("Please input the following to get your total loan repayments")

    amount=float(input("Insert loan amount: "))
    interest=float(input("Insert amount of interest per annum: "))
    years=float(input("How long the loan is for: "))
    tpy = float(input("How many times a year it compound: "))
    loan(amount,interest,years,tpy)