from flask import Flask, render_template, request
from services.RestService import RestService
from services.GrpcService import GrpcService

app = Flask(__name__)
restService = RestService('http://localhost:5001')
grpcService = GrpcService('localhost:50051')

@app.route('/', methods=['GET', 'POST'])
def index():
  if request.method == 'GET':
    return render_template('index.html', users=_getRestUsersList(restService))
  else:
    if request.form['comm'] == 'REST':
      restService.save(request.form)
      return render_template('index.html', users=_getRestUsersList(restService))
    else:
      grpcService.save(request.form)
      return render_template('index.html', users=_getGrpcUsersList(grpcService))

def _getRestUsersList(restService):
  return restService.get()['body']['message']

def _getGrpcUsersList(grpcService):
  return grpcService.get().users

if __name__ == '__main__':
  app.run(debug=True)
