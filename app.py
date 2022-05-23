import csv
from flask import Flask, request
from flask_cors import cross_origin
from content_filtering import recomender

# --------------------------------------------------------------------------------------------


def generate_data():

    columns = []
    data = {}

    id_columns = 3

    csv_file = open('dados/music_profiles_2000.csv')
    csv_reader = csv.reader(csv_file)
    columns = next(csv_reader)

    # Removing row index: music id, music title and artist
    for i in range(id_columns):
        columns.pop(0)

    for row in csv_reader:

        # dict key: music id, music title and artist
        music_identification = row.pop(0)
        row.pop(0)
        row.pop(0)

        features_data = {}
        for feature_index, feature_value in enumerate(row):
            if feature_value != "":
                features_data.update(
                    {columns[feature_index]: float(feature_value)})

        data.update({music_identification: features_data})

    return data

# --------------------------------------------------------------------------------------------


def get_songs_data():

    csv_file = open('dados/music_profiles_2000.csv')
    csv_reader = csv.reader(csv_file)
    columns = next(csv_reader)

    songs = []
    for row in csv_reader:
        songs.append({"id": row[0], "song": row[1], "artist": row[2]})

    csv_file.close()

    return songs

# --------------------------------------------------------------------------------------------


app = Flask(__name__)
SONGS_NAMES = get_songs_data()
SONGS = generate_data()


# --------------------------------------------------------------------------------------------


@app.route("/get-songs", methods=['GET'])
@cross_origin()
def get_songs():
    return {"total": len(SONGS_NAMES), "data": SONGS_NAMES}

# --------------------------------------------------------------------------------------------


@app.route("/get-recomendations", methods=['POST'])
@cross_origin()
def get_recomentadions():

    def dict_mean(dict_list):
        mean_dict = {}
        for key in dict_list[0].keys():
            mean_dict[key] = sum(d[key] for d in dict_list) / len(dict_list)
        return mean_dict

    songs = request.get_json()

    profiles = []
    songsAux = SONGS.copy()
    for song in songs:
        del songsAux[song['id']]
        profiles.append(SONGS[song['id']])

    profile = dict_mean(profiles)

    recomendations = recomender(profile, songsAux)
    return {"total": len(recomendations), "data": recomendations}

# --------------------------------------------------------------------------------------------
