import json

aDict = {"employee_details":[{"Name": "Mallika", "Age": "38"},{"Name":"Santa", "Age":"27"}]}
jsonString = json.dumps(aDict)#changes into a json
jsonFile = open("data.json", "w")
jsonFile.write(jsonString)
jsonFile.close()