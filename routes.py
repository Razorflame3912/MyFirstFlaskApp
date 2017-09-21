from flask import Flask

app = Flask(__name__)

@app.route('/')
def root():
    print 'Root Accessed'
    return '<h1><i></b>Main Page!</b></i></h1><hr>'

@app.route('/secret')
def secret():
    print 'SECRET TEXT ACCESSED OH NO'
    return 'psst...the password is "blueberries"'

@app.route('/decoy')
def decoy():
    source = open('beemovie.txt','rU')
    sourcetext = source.read()
    source.close()
    print 'AHA THEY TOOK THE BAIT'
    return sourcetext

if __name__ == '__main__':
    app.debug = True
    app.run()
