import csv
import pandas as pd

data = []
with open(r'C:\Users\euamrag\Desktop\queryoutput.csv') as file:
	reader = csv.DictReader(file)
	
	count = 0

	for row in reader:
		# print(row)
		print(row['LOCATION_ID'])
		print(data)

		if count > 5:
			break

		count += 1

with open(r'C:\Users\euamrag\Desktop\Mig.csv', 'w', newline='') as f:
        fieldnames = ['#migrationBatchId', 'nbncoOrderId', 'appointmentId', 'ticketOfWorkId', 'jobType', 
                      'Relocate / HeightXtn Approved', 'locationId', 'ntdId', 'endUserContactName', 
                      'endUserContactNumber', 'alternateContactName', 'alternateContactNumber', 
                      'ContactEmailAddress (tbc)', 'address - unit number', 'address - site name', 
                      'address - lot number', 'address - street number from', 'address - street number to', 
                      'address - street name', 'address - street type', 'address - suburb', 'address - Postcode', 
                      'stateTerritoryCode', 'Region', 'WSA', 'WCA', 'RSP / Access Seeker ID', 
                      'priority', 'Target Cells (eCGI)']
        the_writer = csv.DictWriter(f, fieldnames=fieldnames)
        the_writer.writeheader()

#         for i in range(1,3):
#         	the_writer.writerow({'jobType' : 'RepanOdu', 'Relocate / HeightXtn Approved' : 'No', 'locationId' : [LOCATION_ID], 'ntdId' : 'NTD_ID',
#                              'endUserContactName' : 'Telco Act', 'endUserContactNumber' : '+61 123 123 123',
#                              'address - lot number' : '29', 'address - street number from' : '79',
#                              'address - street name' : 'KILLEAN', 'address - street type' : 'ST',
#                              'address - suburb' : 'Albany Region', 'address - Postcode' : '2360',
#                              'stateTerritoryCode' : 'NSW', 'Region' : 'Remote', 'WSA' : '6ALN',
#                              'WCA' : '2IVL-51-08-INVE-10-06', 'RSP / Access Seeker ID' : 1,
#                              'priority' : '20', 'Target Cells (eCGI)' : '50562102653699'})




# df = pd.read_csv(r'C:\Users\euamrag\Desktop\queryoutput.csv', nrows=5)

# for index, row in df.iterrows(): 
#     print (row["NTD_ID"])

# frame = pd.DataFrame(df, columns = ['#migrationBatchId', 'nbncoOrderId', 'appointmentId', 'ticketOfWorkId', 'jobType', 
#                       'Relocate / HeightXtn Approved', 'locationId', 'ntdId', 'endUserContactName', 
#                       'endUserContactNumber', 'alternateContactName', 'alternateContactNumber', 
#                       'ContactEmailAddress (tbc)', 'address - unit number', 'address - site name', 
#                       'address - lot number', 'address - street number from', 'address - street number to', 
#                       'address - street name', 'address - street type', 'address - suburb', 'address - Postcode', 
#                       'stateTerritoryCode', 'Region', 'WSA', 'WCA', 'RSP / Access Seeker ID', 
#                       'priority', 'Target Cells (eCGI)'])

# for col in frame.columns:
# 	frame[col].to_csv(r'C:\Users\euamrag\Desktop\res.csv', index=False)
# frame.to_csv(r'C:\Users\euamrag\Desktop\res.csv', index=False)
# for i in range(len(df)):
# 	print(df.loc[i, 'NTD_ID'])

# for index, row in df.iterrows(): 
# 	df2 = df2.append(df)
# #     print (row["NTD_ID"])