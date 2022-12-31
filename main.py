from flask import Flask, request, render_template
import datetime
import time

# Flask constructor
app = Flask(__name__)  
 
# A decorator used to tell the application
# which URL is associated function

def change_value(data):
  print('Hoing to write '+data)
  with open('file.txt','w') as file:
    file.write(data)
  time.sleep(5)
  with open('file.txt','w') as file:
    file.write('doing-nothing')

@app.route('/')
def home():
  with open('file.txt','r') as file:
    data = file.read()
  return data

@app.route('/access', methods =["GET", "POST"])
def gfg():
    if request.method == "POST":
       first_name = request.form.get("fname")
       change_value(first_name)
       return render_template('form.html')
    return render_template("form.html")

@app.route('/save',methods=['GET','POST'])
def image():
  if request.method == 'POST':
    photo = request.files['file']
    photo.save(f'{datetime.datetime.now()}.png')
  return 'got it'

if __name__=='__main__':
   app.run(host='0.0.0',debug=True)