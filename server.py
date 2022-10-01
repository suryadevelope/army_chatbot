
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import tabula
import pandas as pd
import csv

app = Flask(__name__)

app.config["UPLOAD_FOLDER"] = "static/"



@app.route('/display', methods = ['GET', 'POST'])
def save_file():
    if request.method == 'POST':
        f = request.files['file']
        filename = secure_filename(f.filename)
        f.save(app.config['UPLOAD_FOLDER'] + filename)
        tabula.convert_into("./static/"+f.filename, "./static/foo.csv", output_format="csv", pages='all')
        condition = 0

        # reading two csv files
        # data1 = pd.read_csv('./static/foo.csv')
        # data2 = pd.read_csv('./assets/foo.csv')

        # output1 = data1.merge(data2)
        # print(output1)
        print("okokokok")


        df_master = pd.read_csv('./assets/foo.csv')
        df = pd.read_csv('./static/foo.csv')
        df.to_csv('./assets/foo.csv', mode='a', header=False, index=False)
        # with open('./assets/foo.csv', 'wb') as outfile:
        #     for item in output1:
        #         outfile.write(item)

        # with open("./assets/foo.csv", 'w') as tempfile:
        #     writer = csv.DictWriter(tempfile, fieldnames=['Name',"Position","Office","Age","Start date","Salary"])
        #     for row in output1:
        #         print(row)
        #         # writer.writerow(row)
        #     condition = 1
        # while(condition == 0):   
            
        #     if(condition == 1):
        #         break
        # return


        # file = open(app.config['UPLOAD_FOLDER'] + filename,"r")
        # content = file.read()
        
        

if __name__ == '__main__':
    app.run(host="localhost", port=2456, debug = False)
