
import csv


cuslist =[]
inventorylist=[]

x1 = input('')
x2= input('')

list1=[]
list2=[]


with open(x1) as csvfile:
    readCSV = csv.reader(csvfile)
    for row in readCSV:
        cuslist.append(row)
    #print(cuslist)  

with open(x2) as csvfile:
    readCSV = csv.reader(csvfile)
    for row in readCSV:
        inventorylist.append(row)
    #print(inventorylist)
    
x3 = input('')  
f = open(x3)  # create file object
contents_order = f.read()  # read file text into a string
orderlist = contents_order.split('\n')
    #print(orderlist)

nolist=[] 
datelist=[]
indicatorlist=[]
qtylist =[]
itemlist = []
datesecond=[]
itemline=[]
totalnum=[]


for i in range(len(orderlist)):
    no = orderlist[i][2:7]
    if (no.isdigit() == True):
        nolist.append(no)
        datelist.append(orderlist[i][11:])
        indicatorlist.append(orderlist[i][10])
        totalnum.append(int(orderlist[i][7:10]))
    else:
        #qtylist.append(orderlist[i][0:3])
        #itemlist.append(orderlist[i][4:9])
        #datesecond.append(orderlist[i][10:])
        itemline.append(orderlist[i])
itemline2=[]
for i in range(len(itemline)):
    newitemline = itemline[i].split('^')
    itemline2.append(newitemline)
    
    finalqty =[] 
noitem =[]
date2 = []
for i in range(len(itemline2)-1):
    finalqty.append(int(itemline2[i][0]))
    noitem.append(itemline2[i][1])
    date2.append(itemline2[i][2])
    
date3list=[]
for i in range(len(date2)):
    date3= date2[i][:2]+'/'+date2[i][2]+date2[i][3]+'/'+ date2[i][4:]
    date3list.append(date3)
newdate=[]
for i in range(len(datelist)):
    newdatt = datelist[i][:2]+'/'+datelist[i][2]+datelist[i][3]+'/'+ datelist[i][4:]
    newdate.append(newdatt)

itemname=[]  
pricelist=[]


invlist=[]
for j in range(len(inventorylist)):
    inv = inventorylist[j][0]
    invlist.append(inv)
    
for i in range(len(noitem)):
    for j in range(len(inventorylist)):
        if (noitem[i] == inventorylist[j][0]):
            itemname.append(inventorylist[j][1])
            pricelist.append(float(inventorylist[j][2]))
            
    if ((noitem[i] in invlist) == False):
        itemname.append('*** Item not found ***')
        pricelist.append(0.00)


numlist=[]
for i in range(len(cuslist)):
    numlist.append(cuslist[i][0])
    
    namelist=[] 
balancelist=[]
for i in range(len(nolist)):
    for j in range(len(numlist)):
        if(nolist[i] == numlist[j]):
            namelist.append(cuslist[j][1])
            balancelist.append(float(cuslist[j][2]))
    if( (nolist[i] in numlist) == False ):
        namelist.append('')
        balancelist.append(0.00)
        
        #print(namelist)
#['Costanza, George Louis', 'Costanza, George Louis', 'Petrie, Ritchie Rosebud', 'Norton, Edward Lilywhite', 'Burns, Frank Marion', '', 'Deveraux, Blanche E', 'Addams, Wednesday Friday', 'Petrie, Ritchie Rosebud', 'Petrie, Ritchie Rosebud']                               
#print(balancelist)
#[515.55, 515.55, 733.83, 1584.38, 19210.32, 0.0, 1607.33, 453.17, 733.83, 733.83]  
#print(itemname)
#['Pencils', 'Spiral notebooks', 'Pencils', 'Spiral notebooks', 'Graph paper', 'Markers', 'Spiral notebooks', 'Padded envelopes', 'Highlighters', 'Color coding labels', 'Calendar', 'Glue sticks', 'Spiral notebooks', 'Erasers', 'Bubble wrap', 'Tape', 'Time cards', 'Map pins', 'Staples', '3-ring binders', 'Manila file folders', 'Erasers', 'Thumbtacks', 'Index dividers', 'Fax paper', 'Pushpins', 'Paper clips', 'Post-it(R) notes', 'Hanging file folders', 'Markers', 'Pushpins', 'Tape', '3.5" high density disks', 'Calendar', 'Staples', 'Paper clips', 'Bubble wrap', 'Pens', 'Fasteners', 'Fasteners', 'Map pins', '*** Item not found ***', 'Glue', '3.5" high density disks']    
#print(pricelist)
#[74.01, 72.7, 74.01, 72.7, 87.72, 26.96, 72.7, 73.27, 60.42, 66.65, 97.84, 49.22, 72.7, 74.07, 31.42, 80.15, 91.62, 46.22, 62.06, 71.94, 77.27, 74.07, 9.92, 93.87, 64.58, 62.49, 27.52, 47.97, 93.83, 26.96, 62.49, 80.15, 71.47, 97.84, 62.06, 27.52, 31.42, 86.2, 71.2, 71.2, 46.22, 0.0, 79.46, 71.47]  
#print(finalqty)
#[125, 235, 125, 235, 194, 72, 370, 258, 253, 139, 113, 249, 479, 463, 14, 173, 298, 33, 360, 354, 135, 72, 238, 116, 211, 323, 222, 258, 434, 11, 172, 354, 414, 246, 197, 31, 178, 38, 475, 112, 456, 447, 402, 229]
#print(totalnum)
#[2, 2, 5, 3, 1, 4, 12, 10, 2, 3]
#print(date3list)
#['11/21/2020', '11/25/2020', '11/21/2020', '11/25/2020', '06/29/2019', '07/14/2019', '08/02/2019', '07/07/2019', '06/18/2019', '06/27/2019', '06/19/2019', '07/11/2019', '06/16/2020', '08/09/2019', '07/18/2019', '09/11/2019', '09/03/2019', '11/15/2020', '10/04/2020', '11/09/2020', '10/11/2020', '09/25/2020', '11/16/2020', '10/06/2020', '10/08/2020', '09/28/2020', '11/06/2020', '10/29/2020', '10/16/2020', '11/03/2020', '10/26/2020', '09/13/2020', '09/15/2020', '11/07/2020', '10/15/2020', '10/02/2020', '11/03/2020', '10/18/2020', '09/26/2020', '07/29/2020', '07/30/2020', '10/28/2020', '09/25/2020', '09/27/2020']
#print(noitem)
#['LO917', 'IL993', 'LO917', 'IL993', 'AF977', 'L223', 'IL993', 'Y337', 'O261', 'LM485', 'N669', 'P530', 'IL993', 'UN941', 'W555', 'TH851', 'O662', 'Q25', 'IW804', 'UC428', 'YJ195', 'UN941', 'O646', 'K233', 'NG108', 'F603', 'NQ813', 'NO204', 'YC871', 'L223', 'F603', 'TH851', 'TD834', 'N669', 'IW804', 'NQ813', 'W555', 'K733', 'PX218', 'PX218', 'Q25', 'T5333', 'R207', 'TD834']
#print(finalqty)
#[125, 235, 125, 235, 194, 72, 370, 258, 253, 139, 113, 249, 479, 463, 14, 173, 298, 33, 360, 354, 135, 72, 238, 116, 211, 323, 222, 258, 434, 11, 172, 354, 414, 246, 197, 31, 178, 38, 475, 112, 456, 447, 402, 229]

    
#print(finalqty)

def cutlist(a, b):#a is long, b is short
    newdata3 = a
    listfinal2=[]
    for i in range(len(b)):
        listfinal=[]
        for j in range(b[i]):
            x = a.pop(0)
            listfinal.append(x)
        listfinal2.append(listfinal)
    return listfinal2
def buildlist(a):
  newlist =[]
  for i in range(len(a)):
    for j in range(len(a[i])):
      newlist.append(a[i][j])

  return newlist
finalqty1=[]
finalqty1 =finalqty
noitem1 = noitem
date3list1=date3list 
pricelist1=pricelist
itemname1 = itemname

list3 =cutlist(finalqty1, totalnum)
#print(newfinalqty)
list2 = cutlist(noitem1, totalnum)
#print(cutlist)
list5 = cutlist(date3list1, totalnum)
#print(newdate3list)
list4 =cutlist(pricelist1, totalnum)
#print(newpricelist)
list1 =cutlist(itemname1, totalnum)
#print(itemnamenew)


finalqty = buildlist(list3)
#print(finalqty)

pricelist = buildlist(list4)

total2=[]
for i in range(len(finalqty)):
    new = finalqty[i]* pricelist[i]
    total2.append(new)
    
    #print(total2)
totalordered = []
total = cutlist(total2, totalnum)


for i in range(len(total)):
  sum1 =sum(total[i])
  totalordered.append(sum1)

    
 #print(totalordered)


totaldue21 = []
for i in range(len(totalordered)):
  totaldue1 = totalordered[i]+ balancelist[i]
  totaldue21.append(totaldue1)

    
  #print(totaldue21)

balancelist2 = balancelist
for i in range(len(namelist)-1):
    for j in range(i+1, len(namelist)):
        if (namelist[i]==namelist[j]):
            balancelist2[j] = totalordered[i]+ balancelist2[i]
#print(balancelist2)
  
totaldue2 = []
for i in range(len(totalordered)):
  totaldue1 = totalordered[i]+ balancelist2[i]
  totaldue2.append(totaldue1)

 
#print(totaldue2)

#print(namelist)
#['Costanza, George Louis', 'Costanza, George Louis', 'Petrie, Ritchie Rosebud', 'Norton, Edward Lilywhite', 'Burns, Frank Marion', '', 'Deveraux, Blanche E', 'Addams, Wednesday Friday', 'Petrie, Ritchie Rosebud', 'Petrie, Ritchie Rosebud']                               
#print(balancelist)
#[515.55, 515.55, 733.83, 1584.38, 19210.32, 0.0, 1607.33, 453.17, 733.83, 733.83]  
#print(itemname)
#['Pencils', 'Spiral notebooks', 'Pencils', 'Spiral notebooks', 'Graph paper', 'Markers', 'Spiral notebooks', 'Padded envelopes', 'Highlighters', 'Color coding labels', 'Calendar', 'Glue sticks', 'Spiral notebooks', 'Erasers', 'Bubble wrap', 'Tape', 'Time cards', 'Map pins', 'Staples', '3-ring binders', 'Manila file folders', 'Erasers', 'Thumbtacks', 'Index dividers', 'Fax paper', 'Pushpins', 'Paper clips', 'Post-it(R) notes', 'Hanging file folders', 'Markers', 'Pushpins', 'Tape', '3.5" high density disks', 'Calendar', 'Staples', 'Paper clips', 'Bubble wrap', 'Pens', 'Fasteners', 'Fasteners', 'Map pins', '*** Item not found ***', 'Glue', '3.5" high density disks']    
#print(pricelist)
#[74.01, 72.7, 74.01, 72.7, 87.72, 26.96, 72.7, 73.27, 60.42, 66.65, 97.84, 49.22, 72.7, 74.07, 31.42, 80.15, 91.62, 46.22, 62.06, 71.94, 77.27, 74.07, 9.92, 93.87, 64.58, 62.49, 27.52, 47.97, 93.83, 26.96, 62.49, 80.15, 71.47, 97.84, 62.06, 27.52, 31.42, 86.2, 71.2, 71.2, 46.22, 0.0, 79.46, 71.47]  
#print(finalqty)
#[125, 235, 125, 235, 194, 72, 370, 258, 253, 139, 113, 249, 479, 463, 14, 173, 298, 33, 360, 354, 135, 72, 238, 116, 211, 323, 222, 258, 434, 11, 172, 354, 414, 246, 197, 31, 178, 38, 475, 112, 456, 447, 402, 229]
#print(totalnum)
#[2, 2, 5, 3, 1, 4, 12, 10, 2, 3]
#print(date3list)
#['11/21/2020', '11/25/2020', '11/21/2020', '11/25/2020', '06/29/2019', '07/14/2019', '08/02/2019', '07/07/2019', '06/18/2019', '06/27/2019', '06/19/2019', '07/11/2019', '06/16/2020', '08/09/2019', '07/18/2019', '09/11/2019', '09/03/2019', '11/15/2020', '10/04/2020', '11/09/2020', '10/11/2020', '09/25/2020', '11/16/2020', '10/06/2020', '10/08/2020', '09/28/2020', '11/06/2020', '10/29/2020', '10/16/2020', '11/03/2020', '10/26/2020', '09/13/2020', '09/15/2020', '11/07/2020', '10/15/2020', '10/02/2020', '11/03/2020', '10/18/2020', '09/26/2020', '07/29/2020', '07/30/2020', '10/28/2020', '09/25/2020', '09/27/2020']
#print(noitem)
#['LO917', 'IL993', 'LO917', 'IL993', 'AF977', 'L223', 'IL993', 'Y337', 'O261', 'LM485', 'N669', 'P530', 'IL993', 'UN941', 'W555', 'TH851', 'O662', 'Q25', 'IW804', 'UC428', 'YJ195', 'UN941', 'O646', 'K233', 'NG108', 'F603', 'NQ813', 'NO204', 'YC871', 'L223', 'F603', 'TH851', 'TD834', 'N669', 'IW804', 'NQ813', 'W555', 'K733', 'PX218', 'PX218', 'Q25', 'T5333', 'R207', 'TD834']
#print(finalqty)
#[125, 235, 125, 235, 194, 72, 370, 258, 253, 139, 113, 249, 479, 463, 14, 173, 298, 33, 360, 354, 135, 72, 238, 116, 211, 323, 222, 258, 434, 11, 172, 354, 414, 246, 197, 31, 178, 38, 475, 112, 456, 447, 402, 229]

for i in range(len(namelist)):
    if(indicatorlist[i] == 'D'):
        if ((nolist[i] in  numlist) == False):
            print("Customer number", nolist[i], "is invalid." )
            print('---------------')
        else:
            print("Order Date:{:>15}".format(newdate[i]))
            print("  Customer:{:>15}{:>30}".format(nolist[i], namelist[i])+ '\n')
            print("{:^3}   {:<18}{:<28}{:^10}{:>11}{:>11}{:>14}".format("Ln#","Item #", "Item Description", "Req Date", "Qty","Price", "Total"))
            for j in range(len(list1[i])):
                 #print("{:^3}   {:<18}{:<28}{:^10}{:>11}{:>11}{:>4}{:>10}".format(j+1,list2[i][j], list1[i][j], list5[i][j], list3[i][j],list4[i][j], list3[i][j]*list4[i][j]))
                 #print("{:^3}   {:<18}{:<28}{:^10}{:>11}{:>11}{:>14}".format(j+1,list2[i][j], list1[i][j], list5[i][j], list3[i][j],list4[i][j], "Total")
                 print("{:^3d}   {:<18}{:<28}{:^10}{:>11d}{:>11.2f}   ${:>10.2f}".format(j+1,list2[i][j], list1[i][j], list5[i][j], list3[i][j],list4[i][j],total[i][j]))
print('\n'+ "{:>80}{:>18.2f}".format('Total Ordered:', totalordered[i]))
            print("{:>80}{:>18.2f}".format('Balance:', balancelist2[i])+'\n')
            print("{:>80}{:>18.2f}".format('Total Due:', totaldue2[i]))
            print('---------------')
            
    elif(indicatorlist[i] == 'S'):
        if ((nolist[i] in  numlist)== False):
            print("Customer number", nolist[i], "is invalid." )
            print('---------------')
        else:
            print("Order Date:{:>15}".format(newdate[i]))
            print("  Customer:{:>15}{:>30}".format(nolist[i], namelist[i])+ '\n')

            print("{:>80}{:>18.2f}".format('Total Ordered:', totalordered[i]))
            print("{:>80}{:>18.2f}".format('Balance:', balancelist2[i])+ '\n')
           
            print("{:>80}{:>18.2f}".format('Total Due:', totaldue2[i]))
            print('---------------')       
