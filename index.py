from flask import Flask, render_template, json, request
import pandas as pd
import re
app = Flask(__name__)


# Getting the excel file which contains the data


@app.route('/', methods=['post', 'get'])
def home():

    data = pd.read_excel('data.xls')
    df = pd.DataFrame(data)
    df = df.head(n=5)
    min_cost = []  # an empty list to contain all the min values from each variable
    # for i in range(0, len(df.columns)):
    #     # calculating min and adding to the list
    #     min_cost.append(min(df.iloc[:, i]))

    if request.method == 'POST':
        u1 = request.form.get('item1')
        u2 = request.form.get('item2')
        u3 = request.form.get('item3')
        if u1 == "item1":
            min_cost.append(df['Item_1'].min())
        if u2 == "item2":
            min_cost.append(df['Item_2'].min())
        if u3 == "item3":
            min_cost.append(df['Item_3'].min())
        optimised_cost = sum(min_cost)
        return render_template('home.html', total=optimised_cost)
    else:
        return render_template('home.html')

    # return '%d' % optimised_cost
