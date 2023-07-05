import re

with open('immobilierVendu2022.csv', 'r') as bien_file:
    bien_data = bien_file.readlines()

evaluations = ['\n']
count = 0


for i, entry in enumerate(bien_data):
    if entry == bien_data[i-1]:
        bien_data.remove(entry)

for immo in bien_data:
    immo = immo.strip()
    data = immo.split(',')
    lat = data[6]
    long = data[7]

    lat_num = re.findall(r'\d+\.\d+', lat)
    bien_latitude = float(lat_num[0])

    long_num = re.findall(r'\d+\.\d+', long)
    bien_longitude = float(long_num[0])



    with open('arbresremarquablesparis.csv', 'r') as tree_file:
        tree_data = tree_file.readlines()

    for entry in tree_data:
        sample = entry.replace(';', ',')
        sample = sample.split(',')

        lat = sample[0]
        long = sample[1]

        lat_num = re.findall(r'\d+\.\d+', lat)
        if len(lat_num) > 0:
            tree_latitude = float(lat_num[0])

        long_num = re.findall(r'\d+\.\d+', long)
        if len(long_num) > 0:
            tree_longitude = float(long_num[0])


# The difference here is 0.001 degrees latitude = 10 meters, 0.001 longitude = 111 meters at equator (around 85 in Paris)
# The code below measure if it is 30 meters from a tree

        lat_result = bien_latitude - tree_latitude
        long_result = bien_longitude - tree_longitude

        if abs(lat_result) < 0.001 and abs(long_result) < 0.0002:
            addition = f"{immo},10\n"
            if addition != evaluations[count - 1]:
                evaluations.append(addition)
                count += 1
                print(count)

        elif abs(lat_result) < 0.002 and abs(long_result) < 0.0003:
            addition = f"{immo},20\n"
            if addition != evaluations[count - 1]:
                evaluations.append(addition)
                count += 1
                print(count)

        elif abs(lat_result) < 0.003 and abs(long_result) < 0.0004:
            addition = f"{immo},30\n"
            if addition != evaluations[count - 1]:
                evaluations.append(addition)
                count += 1
                print(count)

        elif abs(lat_result) < 0.004 and abs(long_result) < 0.0005:
            addition = f"{immo},40\n"
            if addition != evaluations[count - 1]:
                evaluations.append(addition)
                count += 1
                print(count)

        elif abs(lat_result) < 0.005 and abs(long_result) < 0.0006:
            addition = f"{immo},50\n"
            if addition != evaluations[count - 1]:
                evaluations.append(addition)
                count += 1
                print(count)

        elif abs(lat_result) < 0.01 and abs(long_result) < 0.002:
            addition = f"{immo},100\n"
            if addition != evaluations[count - 1]:
                evaluations.append(addition)
                count += 1
                print(count)

        else:
            addition = f"{immo},0\n"
            if addition != evaluations[count - 1]:
                evaluations.append(addition)
                count += 1
                print(count)



for i, entry in enumerate(evaluations):
    try:
        if entry == evaluations[i-1]:
            evaluations.remove(entry)
    except IndexError:
        print("Out of range")

with open('immoVenduArbres.csv', 'a') as file:
    for i, entry in enumerate(evaluations):
        file.write(entry)