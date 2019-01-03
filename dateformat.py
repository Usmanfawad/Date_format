months1_pre=['jan','mar','may','july','aug','oct','dec']
months2_pre=['apr','jun','sept','nov']
months3_pre=['feb']
months1=[1,3,5,7,8,10,12]
months2=[4,6,9,11]
months3=[2]
complete_day=['0']
complete_month=['0']
complete_day1=['0']
complete_month1=['0']
complete_date= []
complete_date1=[]

def date_type1(x):
    #ddmmyyyy
    #checking the number of hyphens inputted
    if x.count('-')==2:
        datelst = x.split('-')
    elif x.count('/')==2:
        datelst = x.split('/')

    print(datelst)
    #checking lenght of date
    if len(datelst[0])< 2 and len(datelst[0]) >0 :
        complete_day.append(datelst[0])
        conca_day=''.join(complete_day)
        complete_date.append(conca_day)
    elif len(datelst[0])==2:
        complete_date.append(datelst[0])
    else:
        print("Invalid Day.")
    #checking lenght of month
    if len(datelst[1])<2 and len(datelst[1]) >0 :
        complete_month.append(datelst[1])
        conca_month=''.join(complete_month)
        complete_date.append(conca_month)
    elif len(datelst[1])==2:
        complete_date.append(datelst[1])
    else:
        print("Invalid Month.")
    complete_date.append(datelst[2])
    #checking valid days and months
    if int(complete_date[0])>31 or int(complete_date[0])==0 and int(complete_date[1]) in months1:
        print('-'.join(complete_date),"\nInvalid day.")
    elif int(complete_date[0])>31 or int(complete_date[0])==0 and int(complete_date[1]) not in months1:
        print('-'.join(complete_date),"\nInvalid month and day.")
    elif int(complete_date[0])<=31 and int(complete_date[1]) not in months1:
        print('-'.join(complete_date),"\nInvalid month.")
    elif int(complete_date[0])>31 and int(complete_date[1]) in months1:
        print('-'.join(complete_date), "\nThe following month can only have a maximum of 31 days.")
    elif int(complete_date[0])<=31 and int(complete_date[1]) in months1:
        print('-'.join(complete_date),"\nIs a valid date.")
    elif int(complete_date[0])>30 and int(complete_date[1]) in months2:
        print('-'.join(complete_date),"\nThe following month can only have a maximum of 30 days.")
    elif int(complete_date[0]) <= 30 and int(complete_date[1]) in months2:
        print('-'.join(complete_date),"\nIs a valid date.")
    elif int(complete_date[0]) > 28 and int(complete_date[1]) in months3:
        print('-'.join(complete_date), "\nThe following month can only have a maximum of 28 days.")
    elif int(complete_date[0]) <= 28 and int(complete_date[1]) in months3:
        print('-'.join(complete_date),"\nIs a valid date.")



def date_type2(x):
    #mmddyyyy
    # checking the number of hyphens inputted
    if x.count('-')==2:
        datelst = x.split('-')
    elif x.count('/')==2:
        datelst = x.split('/')

    print(datelst)
    #checking lenght of month
    if len(datelst[0])<2 and len(datelst[0])>0:
        complete_month1.append(datelst[0])
        conca_month1=''.join(complete_month1)
        complete_date1.append(conca_month1)
    elif len(datelst[0])==2:
        complete_date1.append(datelst[0])
    else:
        print("Invalid month.")

    #checking lenght of date
    if len(datelst[1])< 2 and len(datelst[1]) >0 :
        complete_day1.append(datelst[1])
        conca_day1=''.join(complete_day1)
        complete_date1.append(conca_day1)
    elif len(datelst[1])==2:
        complete_date1.append(datelst[1])
    else:
        print("Invalid Day.")
    complete_date1.append(datelst[2])

    # checking valid days and months
    if int(complete_date1[1])>31 or int(complete_date1[1])==0 and int(complete_date1[0]) not in months1:
        print('-'.join(complete_date1),"\nInvalid month and day.")
    elif int(complete_date1[1])<31 and int(complete_date1[0]) not in months1:
        print('-'.join(complete_date1),"\nInvalid month.")
    elif int(complete_date1[1]) > 31 and int(complete_date1[0]) in months1:
        print('-'.join(complete_date1),"\nThe following month can only have a maximum of 31 days.")
    elif int(complete_date1[1]) <= 31 and int(complete_date1[0]) in months1:
        print('-'.join(complete_date1), "Is a valid date.")
    elif int(complete_date1[1])>30 or int(complete_date1[1])==0 and int(complete_date1[0]) not in months2:
        print('-'.join(complete_date1),"\nInvalid Day and month.")
    elif int(complete_date1[1])<30  and int(complete_date1[0]) not in months2:
        print('-'.join(complete_date1),"\nInvalid month.")
    elif int(complete_date1[1])>30 and int(complete_date1[0]) in months2:
        print('-'.join(complete_date1),"\nThe following month can only have a maximum of 30 days.")
    elif int(complete_date1[1]) <= 30 and int(complete_date1[0]) in months2:
        print('-'.join(complete_date1),"\nIs a valid date.")
    elif int(complete_date1[1]) > 28 or int(complete_date1[1]) ==0 and int(complete_date1[0]) not in months3:
        print('-'.join(complete_date1),"\nInvalid Day and month")
    elif int(complete_date1[1]) > 28 and int(complete_date1[0]) in months3:
        print('-'.join(complete_date1),"\nThe following month can only have a maximum of 28 days.")
    elif int(complete_date1[1]) <= 28 and int(complete_date1[0]) in months3:
        print('-'.join(complete_date1), "Is a valid date.")

print("Please choose the format your wish to check\n1) dd-mm-yy\n2)mm-dd-yy")
user_inp=input("1 Or 2?  -")
if user_inp=='1':
    for x in range(10):
        user_date=input("Enter The Date You Wish to check:  -")
        date_type1(user_date)
        complete_day = ['0']
        complete_month = ['0']
        complete_date = []

