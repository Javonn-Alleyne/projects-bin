import eel
from random import randint

eel.init("web")

# expose the random_python fucntion to javascript
@eel.expose
def random_python():
    print("random function running")
    return randint(1,100)

# start the index.html file
eel.start("index.html")