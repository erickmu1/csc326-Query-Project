<<<<<<< HEAD
print("Hello!")
=======
from bottle import route, run
@route('/')
def hello():
    return "Hello World"

run(host='localhost', port=8080, debug=True)
>>>>>>> 3558471af645669105117e07cfa4805ca6a10295
