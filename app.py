import falcon
import json

personal_details = {
    'name': 'Honza\n',
    'surname': 'Javorek\n',
    'socks_size': '69\n'
}

class PersonalDetailsResource():

    def on_get(self, request, response):
        response.status = '200 OK'
        response.set_header('Content-Type', 'application/json')
        response.body = json.dumps(personal_details)

app = falcon.API()
app.add_route('/', PersonalDetailsResource())

if __name__ == "__main__":
    app.run()