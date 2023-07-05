import requests

# Reads the file of real estate sold in Paris in 2022 and stores the data
with open('immobilierArbresParis.csv', 'r') as file:
    data = file.readlines()

# Extract the address from the entry
count = 0
for entry in data:
    sample = entry
    sample = sample.split(',')
    address = sample[1]
    zip = address[-5:]
    address = address[0:-5] + 'Paris ' + zip



    # url = f'http://api.positionstack.com/v1/forward?access_key=6296bcd89c004339427a7e9e34d07df1&query={address}'
    url = f'http://api.positionstack.com/v1/forward?access_key=c619322158e7e929e07d29fc871ac104&query={address}'

# Send the address to the api to get the latitude and longitude
    try:
        response = requests.get(url)
        api_values = response.json()

    except:
        print("An error occured")

    coordinates = api_values['data'][0]

    latitude = coordinates['latitude']
    longitude = coordinates['longitude']
    latitude = str(latitude)
    longitude = str(longitude)



# Reorganize the data and write it into a file
    with open('file.csv', 'a') as file:
        price = sample[0]
        address = sample[1]
        zip = sample[2]
        size = sample[3]
        rooms = sample[4]
        m2 = sample[5].strip()
        entry = f"{price},{address},{zip},{size},{rooms},{m2},{latitude},{longitude}\n"
        file.write(entry)
        print(count)
        count += 1

