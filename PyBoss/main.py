import os
import csv
import datetime

empl_id = []
splitname = []
tempname = []
firstname = []
lastname = []
dateofbirth = []
newstate = []
newssn = []
us_state_abbrev = {'Alabama': 'AL','Alaska': 'AK','Arizona': 'AZ','Arkansas': 'AR','California': 'CA','Colorado': 'CO','Connecticut': 'CT',
	                'Delaware': 'DE','Florida': 'FL','Georgia': 'GA','Hawaii': 'HI','Idaho': 'ID','Illinois': 'IL','Indiana': 'IN','Iowa': 'IA','Kansas': 'KS','Kentucky': 'KY','Louisiana': 'LA',
		            'Maine': 'ME','Maryland': 'MD','Massachusetts': 'MA','Michigan': 'MI','Minnesota': 'MN','Mississippi': 'MS',	
		            'Missouri': 'MO','Montana': 'MT','Nebraska': 'NE','Nevada': 'NV','New Hampshire': 'NH','New Jersey': 'NJ',
		            'New Mexico': 'NM','New York': 'NY',	'North Carolina': 'NC',	'North Dakota': 'ND','Ohio': 'OH','Oklahoma': 'OK','Oregon': 'OR',
		            'Pennsylvania': 'PA','Rhode Island': 'RI','South Carolina': 'SC','South Dakota': 'SD','Tennessee': 'TN','Texas': 'TX',
		            'Utah': 'UT','Vermont': 'VT','Virginia': 'VA','Washington': 'WA','West Virginia': 'WV','Wisconsin': 'WI','Wyoming': 'WY'}


filepath = os.path.join("raw_data",input("Please Enter the Filename : "))

with open(filepath, newline = '') as csvfile:
    filereader = csv.reader(csvfile, delimiter = ",")
    next(filereader, None)
    for row in filereader:
        empl_id.append(row[0])
        tempname = row[1].split()
        firstname = firstname + tempname[:1]  
        lastname = lastname + tempname[1:]
        dateofbirth.append(datetime.datetime.strptime(row[2], '%Y-%m-%d').strftime('%d/%m/%Y'))
        tempssn = row[3].split("-")
        newssn = newssn + tempssn[2:]
        for k,v in us_state_abbrev.items():
            if k == row[4]:
                tempstate = v   
                newstate.append(tempstate)

newssn1 = ["***-**-" + ssn for ssn in newssn]  

outputdata = zip(empl_id, firstname , lastname, dateofbirth, newssn1 , newstate)

output_path = os.path.join('output', 'new.csv')
with open(output_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(['Emp ID','First Name','Last Name','DOB','SSN','State'])
    for row in outputdata:
        csvwriter.writerow(row)
