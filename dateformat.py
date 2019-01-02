months1_pre=['jan','mar','may','july','aug','oct','dec']
months2_pre=['apr','jun','sept','nov']
months3_pre=['feb']
months1=[1,3,5,7,8,10,12]
months2=[4,6,9,11]
months3=[2]
complete_day=['0']
complete_month=['0']
complete_date= []

def date_type1(x):
    #ddmmyyyy
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
    if int(complete_date[0])>31 and int(complete_date[1]) in months1:
        print("The following month can only have a maximum of 31 days.")
    elif int(complete_date[0])<=31 and int(complete_date[1]) in months1:
        print('-'.join(complete_date),"Is a valid date.")
    if int(complete_date[0])>30 and int(complete_date[1]) in months2:
        print("The following month can only have a maximum of 30 days.")
    elif int(complete_date[0]) <= 30 and int(complete_date[1]) in months2:
        print('-'.join(complete_date),"Is a valid date.")
    if int(complete_date[0]) > 28 and int(complete_date[1]) in months3:
        print("The following month can only have a maximum of 28 days.")
    elif int(complete_date[0]) <= 28 and int(complete_date[1]) in months3:
        print('-'.join(complete_date),"Is a valid date.")

        complete_date.append(datelst[2])














dateinp=input("Enter: ")

date_type1(dateinp)

