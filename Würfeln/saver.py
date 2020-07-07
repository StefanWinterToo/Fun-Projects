import csv

def create_csv():
    with open('data/results.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Face"])

def write_csv(player, face):
    with open('data/results.csv', 'a') as outfile:
        writer = csv.writer(outfile)
        writer.writerow([player, face])
