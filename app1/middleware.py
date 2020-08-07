import requests
import json
class IMDBMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response
        print("Constructor")
        imdbweb()
    def __call__(self,request, *args, **kwargs):
        response = self.get_response(request)
        print("CALL")
        return response
def imdbweb():
    url = "https://imdb8.p.rapidapi.com/title/get-most-popular-movies"

    querystring = {"purchaseCountry": "India", "homeCountry": "India", "currentCountry": "India"}

    headers = {
        'x-rapidapi-host': "imdb8.p.rapidapi.com",
        'x-rapidapi-key': "74338f0debmsh16c76033e22d3aep1455e1jsnd9a79579570c"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    data=json.loads(response.text)
    list = []
    count=0
    for x in data:
        movie_id=x.split('/')[2]
        url = "https://imdb-internet-movie-database-unofficial.p.rapidapi.com/film/"+movie_id
        headers = {
        'x-rapidapi-host': "imdb-internet-movie-database-unofficial.p.rapidapi.com",
        'x-rapidapi-key': "74338f0debmsh16c76033e22d3aep1455e1jsnd9a79579570c"
        }
        response = requests.request("GET", url, headers=headers)
        dict_data =json.loads(response.text)
        if dict_data['title']:
            list.append(dict_data)
            count+=1
            if count == 5:
               break
    json.dump(list,open("app1/raw/imdbweb.json","w"))
    print("data written to file")
