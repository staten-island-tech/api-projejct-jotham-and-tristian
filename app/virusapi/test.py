import vt, requests


url = 'https://www.virustotal.com/vtapi/v3/file/scan'
filehash = requests.form.get("userfile")
params = {'apikey': '<29909ddf2acb1233e0cab2142ec6ea733e786e4d97ea4b631e70860acf0c61c6>'}

files = {'file': ('userfile', open('userfile', 'rb'))}

response = requests.post(url, files=files, params=params)

print(response.json())