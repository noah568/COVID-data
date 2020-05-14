import csv

# made variables for the rows because the different data sets do not have the same structure
date_colum = 0
county_colum = 1
state_colum = 2
death_colum = 5
deaths = [0]
i=int(0)


#state = raw_input('State: ')
#county = raw_input('County: ')

state = "Pennsylvania"
county = "Philadelphia"
print(state)
with open("us-counties.csv", "r") as csv_file:
    has_header = csv.Sniffer().has_header(csv_file.read(1024)) #checks if the first line in CSV file is a header or a number
    csv_file.seek(0)  # Rewind.
    csv_reader = csv.reader(csv_file)
    if has_header: #if the first line is a header, not a number, it skips it
        next(csv_reader)  # Skip header row.
    for row in csv_reader:
        if state == row[state_colum]:
            if county == row[county_colum]:
                print(i,int(row[death_colum]))
                deaths.append(int(row[death_colum]) - i)
                print(row[date_colum],row[county_colum],'deaths that day: ', deaths[-1])
                i = int(row[death_colum])

#note: not sure why some days there are negative deaths. A few bad data points, possibly
