from flask import Flask,render_template

FAI=Flask(__name__)

@FAI.route('/Raj/<name>')
def Raj(name):
    return (f'This is {name} second Flask project.....!')

@FAI.route('/Rajesh')
def Rajesh():
    return render_template('Raj.html')
if __name__=='__main__':
    FAI.run(debug=True)