import urllib, json

base_url = None

def get_quote():
    url="http://quotes.stormconsultancy.co.uk/random.json"
    with urllib.request.urlopen(url) as url:
        res_json = url.read()
        response = json.loads(res_json)
    
        return response
