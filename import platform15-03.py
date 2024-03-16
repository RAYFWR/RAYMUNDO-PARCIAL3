import platform
import sys
import subprocess
import json
file_name = 'data.json'
sistemaop= sys.platform
sistema = platform.system()
version= platform.win32_ver()
print("Estamos en {}".format(sistema), "en version: {}".format(version))
print ("Tipo SO: {}".format(sistemaop))
if sistema == 'Windows':
    local = subprocess.getoutput("""for /f "tokens=2 delims=[]" %a in ('ping -n 1 -4 "%computername%"') do @echo %a""")
else:
    local = subprocess.getoutput("ifconfig | grep 'inet '| grep -Fv 127.0.0.1 | awk '{print $2}'")
hostname = platform.node()
cpu= platform.processor()

diccionario = {'ip':local, 'so':sistema, 'version':version, 'hostname':hostname, 'cpu':cpu}
dictionaryTojson = json.dumps(diccionario)
print(dictionaryTojson)
file = open(file_name,"w")
json.dump(diccionario, file, indent=4)
file.close()
