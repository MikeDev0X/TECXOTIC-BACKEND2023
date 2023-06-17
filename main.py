from threading import Thread
import os
import sys
import json

from flask import Response, request, abort

from werkzeug.utils import secure_filename

import cv2
from flask import Response, request, abort, Flask
from flask_cors import CORS
from werkzeug.utils import secure_filename

from routes.utils.findDNASequence import searchSpecies
import os
import json


sys.path.insert(1,os.getcwd())

from routes.CamServer import camServer, cap1
#from routes.DNATask import DNATask

UPLOAD_FOLDER = r'.\routes\utils'

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.gif','.jpeg']

CORS(app)
app.register_blueprint(camServer)
#app.register_blueprint(buttons_functionality)


@app.route('/getCoralSpecie', methods=['POST'])
def getCoralSpecie():
 
    eDNA_object = request.get_json()

    if eDNA_object:
        eDNA_Array = []

        # turn into array
        decoyString = ""
        for i in range (3):
            decoyString = eDNA_object[str(i+1)]
            decoyString = decoyString.replace(" ","")
            eDNA_Array.append(decoyString)

        print(eDNA_Array)
        mainDir = os.getcwd()
        ut = mainDir + r"\routes" + r"\utils" #windows
        #ut = mainDir + r"/routes" + r"/utils" #MacOS
        os.chdir(ut)

        #get out of utils
        os.chdir(mainDir)

        foundSpecies = searchSpecies(eDNA_Array)

        return Response(
            json.dumps(foundSpecies, default=tuple),
            status=200,
            mimetype = 'application/json'
        )
    else:

        return Response(
            json.dumps('eDNA Array is empty', default=tuple),
            status=200,
            mimetype = 'application/json'
        )
    

if __name__ == '__main__':
    try:
        # Running the server that delivers video and the task, each request runs on diferent thread
        Thread(
                target=lambda: app.run(host='0.0.0.0', port=8080, debug=False, use_reloader=False, threaded=True)).start()
        # Running the websocket server that manage the manual control of the ROV
        #websocket_server()
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print("Releasing video") #TODO: CHECK WHETHER THIS CODE IS TRULY EXECUTING
        cap1.release()
        #cap2.release()
        pass
