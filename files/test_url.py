import requests

import json

debut = 'https://pod.unistra.fr/media/'

with open('./import/Pod.json') as f:
  pods = json.load(f)
print( "Test url fichiers origine")
for x, res in enumerate(pods): 
  url = debut + res['fields']['video'] 
  r = requests.get(url)
  response = str(r.status_code)
  if str('404') in response:
    print(url+ " non trouvee ")
  else:
    print(url+ " trouvee ")
    exit(0)

exit('foutu')

with open('./import/thumbnails.json') as f:
  thumbnails = json.load(f)
print( "Test url fichiers thumbnails")
for key, value in thumbnails.items():
  #print(key, ":", value)
  thumbnail = value[0]['thumbnail'] 
  if (len(thumbnail) > 0 ):
    url = 'https:'+ thumbnail
    r = requests.head(url)
    length = r.headers['content-length']
    if not (length > 0):
      exit(url +' not exist')
    else:
      print(url)




with open('./import/docpods.json') as f:
  data = json.load(f)
print( "Test url fichiers documents")
for value in data.values():
  if (len(str(value))>3):
    url = debut + value[0]
    #print(url)
    r = requests.head(url)
    length = r.headers['content-length']
    if not (length > 0):
      exit(url +' not exist')


with open('./import/encodingpods.json') as f:
  encodings = json.load(f)
print( "Test url fichiers encodage")
for key, value in encodings.items():
  #print(key, ":", value)
  url = debut + value[0]['efile']
  #print(url)
  r = requests.head(url)
  length = r.headers['content-length']
  if not (length > 0):
    exit(url +' not exist')


  









