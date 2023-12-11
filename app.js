from flask import Flask, jsonify, render_template
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    conn = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        passwd="12345678",
        database="Public_Broadcasting"
    )
    return conn

@app.route('/episodes', methods=['GET'])
def get_episodes():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM episodes")
    episodes = cursor.fetchall()
    cursor.close()
    conn.close()

    print (episodes);
    
    # Convertir los resultados a un formato JSON
    episodes_list = []
    for episode in episodes:
        episode_data = {
            'episode': episode[0],
            'title': episode[1],
            'apple_frame': episode[2],
            'aurora_borealis': episode[3],
            'barn': episode[4],
            'beach': episode[5],
            'boat': episode[6],
            'bridge': episode[7],
            'building': episode[8],
            'bushes': episode[9],
            'cabin': episode[10],
            'cactus': episode[11],
            'circle_frame': episode[12],
            'cirrus': episode[13],
            "cliff": episode[14],
            'clouds': episode[15],
            'conifer': episode[16],
            'cumulus': episode[17],
            'deciduous': episode[18],
            'diane_andre': episode[19],
            'dock': episode[20],
            'double_oval_frame': episode[21],
            'farm': episode[22],
            'fence': episode[23],
            'fire': episode[24],
            'florida_frame': episode[25],
            'flowers': episode[26],
            'fog': episode[27],
            'framed': episode[28],
            'grass': episode[29],
            'guest': episode[30],
            'half_circle_frame': episode[31],
            'half_oval_frame': episode[32],
            'hills': episode[33],
            'lake': episode[34],
            'lakes': episode[35],
            'lighthouse': episode[36],
            'mill': episode[37],
            'moon': episode[38],
            'mountain': episode[39],
            'mountains': episode[40],
            'night': episode[41],
            'ocean': episode[42],
            'oval_frame': episode[43],
            'palm_trees': episode[44],
            'path': episode[45],
            'person': episode[46],
            'portrait': episode[47],
            'rectangle_3d_frame': episode[48],
            'rectangular_frame': episode[49],
            'river': episode[50],
            'rocks': episode[51],
            'seashell_frame': episode[52],
            'snow': episode[53],
            'snowy_mountain': episode[54],
            'split_frame': episode[55],
            'steve_ross': episode[56],
            'structure': episode[57],
            'sun': episode[58],
            'tomb_frame': episode[59],
            'tree': episode[60],
            'trees': episode[61],
            'triple_frame': episode[62],
            'waterfall': episode[63],
            'waves': episode[64],
            'windmill': episode[65],
            'window_frame': episode[66],
            'winter': episode[67],
            'wood_framed': episode[68]
        }
        episodes_list.append(episode_data)

    return render_template('episodes.html', episodes=episodes_list)


if __name__ == '__main__':
    app.run(debug=True)
