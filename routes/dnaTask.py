import cv2
from flask import Response, Blueprint, request, jsonify
from routes.utils.photoToText import extractText
from routes.utils.findDNASequence import searchSpecies, serialize_sets
import os
import json

dnaTask = Blueprint('dnaTask', __name__)

@dnaTask.route('/getCoralSpecie', methods=['GET'])
def getCoralSpecie():

    mainDir = os.getcwd()
    #get into utils
    print(mainDir)
    ut = mainDir + r"\routes" + r"\utils" #windows
    os.chdir(ut)    

    #extract text from photo in array
    eDNA_array = []
    eDNA_array = extractText()

    #get out of utils
    os.chdir(mainDir)


    foundSpecies = searchSpecies(eDNA_array)

    return Response(
        json.dumps(foundSpecies, default=tuple),
        status=200,
        mimetype = 'application/json'
    )

