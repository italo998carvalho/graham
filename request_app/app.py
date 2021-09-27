from flask import Flask, render_template, request
from setup import restService, grpcService
from services.RequesterService import RequesterService

app = Flask(__name__)
requesterService = RequesterService(restService, grpcService)

@app.route('/', methods=['GET', 'POST'])
def index():
  if request.method == 'POST':
    return requesterService.save(request.form)
  else:
    return requesterService.show()

if __name__ == '__main__':
  app.run(debug=True)
