import datetime
from rest.req_methods.methods import post, get
from SpeedTest import SpeedTest

spdTest = SpeedTest(post, get)

starting = datetime.datetime.now()

spdTest.runPost()
print('Finished posting after: ' + str(datetime.datetime.now() - starting))

spdTest.runGet()
print('Finished getting after: ' + str(datetime.datetime.now() - starting))
