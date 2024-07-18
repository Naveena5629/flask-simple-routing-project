from flask import Flask
app=Flask('__name__')
@app.route('/')
def hello():
    return "<h1>My first routing</h1>"
@app.route('/ab')
def hi1():
    return "<h1>simple routing project</h1>"
@app.route('/cd')
def hi2():
    return "<h1>Today project</h1>"
if __name__=='__main__':
    app.run(debug=True)
