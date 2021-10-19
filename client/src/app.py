from flask import Flask, render_template, request
from setup import restService, grpcService
from services.requester_service import RequesterService

app = Flask(__name__)
requesterService = RequesterService(restService, grpcService)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        requesterService.save(request.form)

    usersList = requesterService.show()
    return render_template('index.html', users=usersList)


if __name__ == '__main__':
    app.run(debug=True)
