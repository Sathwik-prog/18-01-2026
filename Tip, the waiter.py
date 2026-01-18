def total_calc(bill_amount,tip_perc):
#define function to calculate the tip on bill
  total = bill_amount*(1 + 0.01*tip_perc)
  total = round(total,2)
  print(f"Please pay ${total}")

# specify only bill_amount
# default value of tip percentage is used
# take user input for bill amount
bill_amount = int(input("Enter the bill amount: "))
tip_perc = int(input("Enter the tip percentage: "))
total_calc(bill_amount=bill_amount, tip_perc=tip_perc)
