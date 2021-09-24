from flask import Flask, render_template, request
from services.RestService import RestService
from services.GrpcService import GrpcService

app = Flask(__name__)
restService = RestService('http://localhost:5001')
grpcService = GrpcService('localhost:50051')

@app.route('/', methods=['GET', 'POST'])
def index():
  if request.method == 'POST':
    if request.form['comm'] == 'REST':
      restService.save(request.form)
      return renderIndex('REST')
    else:
      grpcService.save(request.form)
      return renderIndex('GRPC')

  return renderIndex()

def renderIndex(comm = 'REST'):
  if comm == 'REST':
    return render_template('index.html', users=_getRestUsersList(restService))
  else:
    return render_template('index.html', users=_getGrpcUsersList(grpcService))

def _getRestUsersList(restService):
  return restService.get()['body']['message']

def _getGrpcUsersList(grpcService):
  return grpcService.get().users

if __name__ == '__main__':
  app.run(debug=True)
