
record = {2201 : {"Name": "Perk" , "Type": "chocolate" , "Quantity" : "30" , "Expiry date" : "20 aug,23" , "Price" : "10", },          
             
          2202 : {"Name": "Bourneville" , "Type": "chocolate" , "Quantity" : "50" , "Expiry date" : "16 aug,24" , "Price" : "10",},

          2203 : {"Name": "Dairy Milk" , "Type": "chocolate" , "Quantity" : "40" , "Expiry date" : "11 aug,24" , "Price" : "10",},

          2204 : {"Name": "Nutties" , "Type": "chocolate" , "Quantity" : "100" , "Expiry date" : "12 aug,25" , "Price" : "10",},
          2205 : {"Name": "Kit-Kat" , "Type": "chocolate" , "Quantity" : "60" , "Expiry date" : "26 aug,24" , "Price" : "10",},
          2206 : {"Name": "Perk" , "Type": "chocolate" , "Quantity" : "200" , "Expiry date" : "04 aug,26" , "Price" : "20",},
          2207 : {"Name": "Bourneville" , "Type": "chocolate" , "Quantity" : "40" , "Expiry date" : "01 aug,22" , "Price" : "50",},
          2208 : {"Name": "Milky Bar" , "Type": "chocolate" , "Quantity" : "70" , "Expiry date" : "22 aug,23" , "Price" : "10",},
          2209 : {"Name": "Dairy Milk" , "Type": "chocolate" , "Quantity" : "80" , "Expiry date" : "21 aug,24" , "Price" : "40",},
          2210 : {"Name": "Dairy Milk Silk" , "Type": "chocolate" , "Quantity" : "50" , "Expiry date" : "25 aug,25" , "Price" : "20",},
          2211 : {"Name": "Dairy Milk Silk" , "Type": "chocolate" , "Quantity" : "80" , "Expiry date" : "07 aug,26" , "Price" : "80",},
          2212 : {"Name": "Munch" , "Type": "chocolate" , "Quantity" : "90" , "Expiry date" : "09 aug,24" , "Price" : "5",},
          2213 : {"Name": "Munch" , "Type": "chocolate" , "Quantity" : "150" , "Expiry date" : "29 aug,26" , "Price" : "10",},
          2214 : {"Name": "Munch" , "Type": "chocolate" , "Quantity" : "170" , "Expiry date" : "24 aug,25" , "Price" : "20",},
          2215 : {"Name": "Bar-one" , "Type": "chocolate" , "Quantity" : "60" , "Expiry date" : "05 aug,24" , "Price" : "10",},
          2216 : {"Name": "Lays wavy" , "Type": "Lays" , "Quantity" : "70" , "Expiry date" : "04 aug,25" , "Price" : "10",},
          2217 : {"Name": "kurkure masala munch" , "Type": "kurkure" , "Quantity" : "80" , "Expiry date" : "06 aug,22" , "Price" : "10",},
          2218 : {"Name": "Lays classic" , "Type": "Lays" , "Quantity" : "100" , "Expiry date" : "04 aug,24" , "Price" : "5",},
          2219 : {"Name": "Lays MAXX" , "Type": "Lays" , "Quantity" : "110" , "Expiry date" : "20 aug,23" , "Price" : "20",},
          2220 : {"Name": "kurkure Solid Masti" , "Type": "kurkure" , "Quantity" : "120" , "Expiry date" : "08 aug,23" , "Price" : "10",},
          2221 : {"Name": "kurkure NIMKO" , "Type": "kurkure" , "Quantity" : "190" , "Expiry date" : "13 aug,23" , "Price" : "15",},
          2222 : {"Name": "Mother Dairy" , "Type": "Milk" , "Quantity" : "200" , "Expiry date" : "08 jan,22" , "Price" : "20",},
          2223 : {"Name": "Mother Dairy" , "Type": "Milk" , "Quantity" : "80" , "Expiry date" : "08 jan,22" , "Price" : "10",},
          2224 : {"Name": "Dynamix Dairy" , "Type": "Milk" , "Quantity" : "50" , "Expiry date" : "08 jan,22" , "Price" : "20",},
          2225 : {"Name": "AAVIN" , "Type": "Milk" , "Quantity" : "60" , "Expiry date" : "08 jan,22" , "Price" : "20",},
          2226 : {"Name": "Dudhsagar Dairy" , "Type": "Milk" , "Quantity" : "130" , "Expiry date" : "08 jan,22" , "Price" : "15",},
          2227 : {"Name": "MILMA" , "Type": "Milk" , "Quantity" : "70" , "Expiry date" : "08 jan,22" , "Price" : "20",},
          2228 : {"Name": "Candyman" , "Type": "Candy" , "Quantity" : "80" , "Expiry date" : "23 aug,23" , "Price" : "1",},
          2229 : {"Name": "Mango Bite" , "Type": "Candy" , "Quantity" : "60" , "Expiry date" : "03 aug,24" , "Price" : "2",},
          2230 : {"Name": "Coffy Bite" , "Type": "Candy" , "Quantity" : "60" , "Expiry date" : "13 aug,24" , "Price" : "1",},
          2231 : {"Name": "Happy Happy" , "Type": "Biscuits" , "Quantity" : "80" , "Expiry date" : "15 aug,23" , "Price" : "10",},
          2232 : {"Name": "Milk Shakti" , "Type": "Biscuits" , "Quantity" : "80" , "Expiry date" : "11 aug,24" , "Price" : "5",},
          2233 : {"Name": "Coconut Cookies" , "Type": "Biscuits" , "Quantity" : "90" , "Expiry date" : "11 aug,23" , "Price" : "10",},
          2234 : {"Name": "Top" , "Type": "Biscuits" , "Quantity" : "70" , "Expiry date" : "18 aug,22" , "Price" : "30",},
          2235 : {"Name": "Festo" , "Type": "Biscuits" , "Quantity" : "100" , "Expiry date" : "12 aug,5" , "Price" : "40",}}

import json
js = json.dumps(record)

fd = open("record.json",'w')
fd.write(js)
fd.close()

print(record)



for a in record:
  a=input('Enter the Item key you want::')
  A=int(a)
  print(record[A])
  if(int(record[A]['Quantity'])>0):
    b=input('How much you want::')
    B=int(b)
    d=record[A]['Price']
    if(B>int(record[A]['Quantity'])):
      print(' ***** Sorry no enough product, try for other Items *****')
    else:
      if(B==0):
        print('You asked for nothing')
        print('Enter the key of Item again')
        
      else:
        x=record[A]['Quantity']
        record[A]['Quantity']=int(x)-B
        print(record[A])
      
        y=int(d)*B
      

        record[A]['Quantity']=int(x)-B
        print("You have to pay  " +str(y)  +"  Rupees" )
       

        print('***************************')
        print('     ----   BILL ----      ')
        print("Your bill is " +str(y)  +"  rupees")
        print('----------------------------------')
        print('You orderd for  ' )

        print(str(B)+ "   " +  record[A]['Name'])

        print('***************************')
        c=str(input('If want to buy some more items enter .Y. ,If not enter .N. :: '))
        if(c==str('Y')):
          pass
        else:
          print('Have a nice day')
          break

  else:
    print('ITEM OUT OF STOCK !!!')
    print('##### Please try other products #####')

