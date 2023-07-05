
# Extracts all of the entries from the French government data, filters for only Paris real estate and reads the entries into a file
with open('valeursfoncieres-2022.txt', 'r') as file:
    data = file.readlines()

for entry in data:
    data_entry = []
    if 'paris' in entry.lower() and '750' in entry:
        value = entry.split('|')
        if value[-7] == "Appartement":
            if value[18] == '75':
                price = value[10].replace(',', '.')


                data_entry.append(price)
                address = value[11] + ' ' + value[13].lower() + ' ' + value[15].lower() + ' ' +  value[16]
                data_entry.append(address)
                size = value[-5]
                data_entry.append(size)

                type = value[-7]
                data_entry.append(type)

                rooms = value[-4]
                data_entry.append(rooms)

                data = ','.join(data_entry)
                with open('immobiliersParisArbres.csv', 'a') as file:
                    file.write(f"{data}\n")
