def totalcalc(bill_amount,tip_perc):
     #define function to caculate tip on bill
       total = bill_amount*(1 +  0.01*tip_perc)
       total = round (total,2)
       print(f"Please pay ${total}")

totalcalc(150,20)