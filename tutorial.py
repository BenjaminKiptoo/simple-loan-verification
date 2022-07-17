high_income = True
good_credit = True
has_defaulted_before = False

if high_income and good_credit:
    print("Eligible for loan")
elif good_credit and not has_defaulted_before:
    print("Eligible for loan")
else:
    print("Not eligible for loan")