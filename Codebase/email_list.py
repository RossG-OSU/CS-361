#list of emails
import csv
lis = []

with open('email_list.csv', 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        lis.append(row)

while True:

    print("Hello, please enter your email address. If you are on the list, "
          "entering your email address will remove you from the list. If you are not on the list "
          "entering your email address will add you to the list.")
    address = [str(input())]

    if address not in lis:
        lis.append(address)
        print('Your address has been added to the email list!')
    else:
        lis.remove(address)
        print('Your address has been removed from the email list.')
    #print(lis)
    print('Would you like to quit? Yes or No?')
    ans = input()
    if ans == 'yes':
        with open('email_list.csv', 'w') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(header)
            for l in lis:
                csvwriter.writerow(l)
        break
    else:
        continue