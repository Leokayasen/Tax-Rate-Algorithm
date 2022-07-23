taxRate = 0.2
# ∆ This is the standard tax rate
overTimeRate = 1.5
# ∆ This is used to calculate extra given/lost during overtime

pay = int(input("Input hourly pay rate: "))
# ∆ This is the input for hourly rate of pay
hours = int(input("Input hours worked: "))
# ∆ This is the input for hours worked

if hours > 40:
  # ∆ Opening of 'if' statement to calculate overtime
	overTime = (hours - 40) * (pay * overTimeRate)
  # ∆ Overtime payment calculation
	total = (pay * 40) + overTime
  # ∆ Total pay, including overtime calculation
else:
	total = pay * hours
  # ∆ If the overtime is below '40', standard total is calculated

tax = total * taxRate
# ∆ Tax amount calculated with total and taxrate
total = total - tax
# ∆ Final total pay, minus the tax calculated

print("Your total pay is "+str(total))
# ∆ Output message of total pay, without tax amount
