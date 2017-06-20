import os, time
from flask import Flask, Response, render_template, jsonify
from geojson import Point, Feature, FeatureCollection
import geojson

app = Flask(__name__)
app.debug = True

ACCESS_KEY = 'pk.eyJ1Ijoicm9hZHRyaXBwZXJzIiwiYSI6ImNqNDAzOXQycTBhY28zM3FyaHE2Y2dlNGkifQ.cMTxTxGa48kl4LUbPHSegg'

@app.route('/')
def index():
    return render_template('index.html', ACCESS_KEY=ACCESS_KEY)

@app.route('/grid/all')
@app.route('/grid')
def grid():

    return render_template('grid_v2.html', ACCESS_KEY=ACCESS_KEY, grid1_geojson=None)

@app.route('/choices')
def choices():
    return render_template('choices.html', ACCESS_KEY=ACCESS_KEY)

@app.route('/heatmap/<persona>')
def heat(persona):
    file_name = persona.lower() + ".geojson"
    with open('sources/'+file_name, 'r') as f:
        geo_string = f.read()
        geo_json = geojson.loads(geo_string)
    print len(geo_json)
    return render_template('single_persona_heat.html', ACCESS_KEY=ACCESS_KEY, geo_json=geo_json)

@app.route('/heatmap/all')
def heatmap_all():
    with open('sources/family_education.geojson', 'r') as f:
        geo_string = f.read()
        family_edu_geojson = geojson.loads(geo_string)
    with open('sources/family_fun.geojson', 'r') as f:
        geo_string = f.read()
        family_fun_geojson = geojson.loads(geo_string)

    with open('sources/outdoor_nature.geojson', 'r') as f:
        geo_string = f.read()
        outdoor_nature_geojson = geojson.loads(geo_string)

    with open('sources/outdoor_adventure.geojson', 'r') as f:
        geo_string = f.read()
        outdoor_adventure_geojson = geojson.loads(geo_string)
    with open('sources/luxury.geojson', 'r') as f:
        geo_string = f.read()
        luxury_geojson = geojson.loads(geo_string)



    return render_template('choices_heat.html', ACCESS_KEY=ACCESS_KEY, family_edu_geojson=family_edu_geojson,family_fun_geojson=family_fun_geojson,
                            outdoor_nature_geojson=outdoor_nature_geojson, outdoor_adventure_geojson=outdoor_adventure_geojson,
                            luxury_geojson=luxury_geojson)



# @app.route('/result')
# def process():
#     point = Point((-77.0366048812866, 38.89784666877921))
#     feature = Feature(geometry=point)
#     feature_collection = FeatureCollection([feature])
#     return jsonify(result=feature_collection)
#
# @app.route('/process')
# def long_running_process():
#       def generate():
#         for row in range(1, 10):
#             yield 'data: Processing \n\n'
#             time.sleep(2)
#       return Response(generate(), mimetype='text/event-stream')

app.run(threaded=True, host='0.0.0.0')
