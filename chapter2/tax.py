my_income = 100  # 내소득
tax_rate = 0.2  # 세율


# 1
my_tax = my_income * tax_rate
print(f"내가 내야되는 세금 : {my_tax}")

# 2
after_tax_income = my_income - my_tax
print(f"세후 급여 {after_tax_income}")

# 3
my_income2 = float(input("수입 입력"))
tax_rate2 = float(input("세율 입력"))

my_tax2 = my_income2 * tax_rate2
after_tax_income2 = my_income2 - my_tax2

print(f"세후 급여: {after_tax_income2}")
