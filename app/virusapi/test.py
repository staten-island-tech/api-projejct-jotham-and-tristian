import vt, requests, cgi, cgitb

form = cgi.FieldStorage()
userURL = form.getvalue("UserURL")
userfile = form.getvalue("userFile")

def FileChecker():
    url = "https://www.virustotal.com/api/v3/files"
    files = {"file": (userfile, open(userfile, "rb"), "image/jpeg")}
    headers = {
    "accept": "application/json",
    "x-apikey": "29909ddf2acb1233e0cab2142ec6ea733e786e4d97ea4b631e70860acf0c61c6"
    }
    
    response = requests.post(url, files=files, headers=headers)

    print(response.text)


def URLChecker():
    url = "https://www.virustotal.com/api/v3/urls"

    payload = userURL
    headers = {
    "accept": "application/json",
    "x-apikey": "29909ddf2acb1233e0cab2142ec6ea733e786e4d97ea4b631e70860acf0c61c6",
    "content-type": "application/x-www-form-urlencoded"
    }

    response = requests.post(url, data=payload, headers=headers)

    print(response.text)


