import json
import random
import numpy as np
from numpy import matlib
from flask import Flask, render_template, request, redirect, Response, jsonify
import pandas as pd
from sklearn.cluster import KMeans
from sklearn import preprocessing
from sklearn.preprocessing import scale
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import prepandas
import pickle

app = Flask(__name__)

@app.route("/", methods = ['POST', 'GET'])
def index():
    data_bubble = pd.read_csv("static/bubble.csv")
    data = pd.read_csv('2011top20.csv',delimiter=',')
    data1 = pd.read_csv('static/spending_all_top100.csv')
    data1.fillna(0,inplace = True)
    medicines = list(set(data1["drugname_generic"].values))
    print ("pandas values",type(medicines[1]))


    fr1 = open("stacked_bar_dict.pkl",'rb')
    fr2 = open("chart_line1_dict.pkl",'rb')
    fr3 = open("chart_line2_dict.pkl",'rb')
    fr4 = open("chart_line3_dict.pkl",'rb')
    fr5 = open("chart_line4_dict.pkl",'rb')
    fr6 = open("chart_line5_dict.pkl",'rb')

    stacked_bar_dict = pickle.load(fr1)
    chart_line1_dict = pickle.load(fr2)
    chart_line2_dict = pickle.load(fr3)
    chart_line3_dict = pickle.load(fr4)
    chart_line4_dict = pickle.load(fr5)
    chart_line5_dict = pickle.load(fr6)


    print ("the global dicts are ready")

    if request.method == 'POST':
        if request.form.get('caller') == 'stacked_bar':
            med_name = request.form.get('data')
            print ("post received val",type(med_name))
            #print ("medicine name",med_name)
              
            return jsonify(stacked_bar_dict[med_name])    

        elif request.form.get('caller') == "chart_line1":
            med_name = request.form.get('data')
                  
            return jsonify(chart_line1_dict[med_name])    

        elif request.form.get('caller') == "chart_line2":
            med_name = request.form.get('data')
            #print ("medicine name",med_name)

            return jsonify(chart_line2_dict[med_name])   

        elif request.form.get('caller') == "chart_line3":
            med_name = request.form.get('data')
           # print ("medicine name",med_name)

            return jsonify(chart_line3_dict[med_name])  

        elif request.form.get('caller') == "chart_line4":
            med_name = request.form.get('data')

            return jsonify(chart_line4_dict[med_name]) 

        elif request.form.get('caller') == "chart_line5":
            med_name = request.form.get('data')
           # print ("medicine name",med_name)

            return jsonify(chart_line4_dict[med_name])   


    print ("be")
    chart_data = data.to_dict(orient='records')
    print ("af")
    chart_data = json.dumps(chart_data,indent=2)
    data = {'chart_data': chart_data}
    data_x= json.dumps(data1.to_dict(orient='records'))
    return render_template("index.html", dataa=data,data2 = json.loads(data_x))

app.run(debug=True)  