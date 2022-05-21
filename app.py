import csv

def generate_data():

    columns = []
    data = {}

    id_columns = 3

    csv_file = open('dados/music_features_10_samples.csv')
    csv_reader = csv.reader(csv_file)
    columns = next(csv_reader)

    # Removing row index: music id, music title and artist
    for i in range(id_columns):
        columns.pop(0)

    for row in csv_reader:

        # dict key: music id, music title and artist
        music_identification = (row.pop(0), row.pop(0), row.pop(0))
        
        features_data = {}
        for feature_index, feature_value in enumerate(row):
            if feature_value != "":
                features_data.update({columns[feature_index]: float(feature_value)})

        data.update({music_identification : features_data})

    return data

print(generate_data())