#####Start
 
 
 
 
amountValid = False
x = 0
 
#This states that while the amount hasn't yet been entered/validated, do not continue
while amountValid == False:
 try:
   amount = float(input("Please input the amount you'd like to exchange (GBP): £"))
 except:
   print("Sorry, that input was invalid")
 
 if (float(amount) > 0 and float(amount) < 2500) or (float(amount) == 2500):
   if float(amount) <= 300:
     fee = 1.035
   elif float(amount) > 300 and float(amount) <=750:
     fee = 1.03
   elif float(amount) > 750 and float(amount) <= 1000:
     fee = 1.025
   elif float(amount) > 1000 and float(amount) <= 2000:
     fee = 1.02
   else:
     fee = 1.015
   amountValid = True
  else:
   print("please enter a valid amount")
   amountValid = False
 
 
 
 
          
#this calculates the transaction fee, it then creates a separate variable for the transaction fee rounded to 2 decimal places, as we are using money.
 
feeGBP = (float(amount)*fee) - float(amount)
feeRounded = round(feeGBP,2)
 
 
 
 
#After the user inputs an amount, and the transaction fee is calcuated based on that amount, the fee is outputted to the user.
 
print("Transaction Fee:   £",feeRounded)
 
 
#this asks the user what currency they'd like to convert the amount to.
 
currency = input("please type in the currency you would like, USD, EUR, BRL, JPY, TRY")
 
 
#As each currency has an exchange rate, the multiplier is different and selected based on the input.
 
if currency.upper() == 'USD':
   multiplier = 1.40
elif currency.upper() == 'EUR':
   multiplier = 1.14
elif currency.upper() == 'BRL':
   multiplier = 4.77
elif currency.upper() == 'JPY':
   multiplier = 151.05
elif currency.upper() == 'TRY':
   multiplier = 5.68
 
 
#if the user does not enter a string relating to one of the currencies they are asked to re-input.
 
else:
   print("Please enter a valid currency")
 
 
#the converted amount is then calculated and outputted to 2 decimal places.
 
convertedAmount = float(amount)*multiplier
convertedAmountRounded = round(convertedAmount,2)
print("This will be the amount after conversion: ",convertedAmountRounded)
 
 
#the final amount is calculated using the transcation fee and the amount inputted by the user, this is outputted as GBP.
 
totalAmountGBP = (convertedAmount/multiplier)*fee
totalAmountGBPRounded = round(totalAmountGBP,2)
 
 
 
#This small cut-off adds a 5% discount if the user is a member of staff through using a 0.95 multiplier to the final amount.
y = 1
while y == 1:
   try:
       staffCheck = input("Are you a memeber of staff? Y/N")
   except:
       print("please enter 'Y' or 'N'")
      
   if staffCheck.upper() == 'Y':
       discount = 0.95
       discountedTotal = totalAmountGBP*discount
       discountedTotalRounded = round(discountedTotal,2)
       print("Please pay a total of: £",discountedTotalRounded)
       y = 0
 
   elif staffCheck.upper() == 'N':
       print("Please pay a total of: £",totalAmountGBPRounded)
       y= 0
 
  
######End
