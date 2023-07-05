
with open("immobiliersParisArbres.csv") as file:
    data = file.readlines()

print(len(data))
print(type(data))
data.remove(data[0])
print(len(data))


# Code to get the price per square meter from the price and size data
with open('filtered_data.csv', 'a') as file:
    for entry in data:

        entry = entry.split(',')
        print(entry)

        if entry[0] != '':
            price = float(entry[0])
            # entry.append(price)
        else:
            price = 0



        address = entry[1].split()
        zip = int(address[-1])

        size = float(entry[2])

        rooms = int(entry[4])

        m2 = round(price/size)
        file.write(f"{price},{entry[1]},{zip},{size},{rooms},{m2}\n")