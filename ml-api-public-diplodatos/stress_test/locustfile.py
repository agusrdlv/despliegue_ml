import time
from locust import HttpUser, task

class QuickstartUser(HttpUser):

    @task(1)
    def index(self):
        #raise NotInplementedError
        self.client.get('/')

    @task(3)
    def predict(self):
        #raise NotInplementedError
        self.client.post('/predict', params={'text':'Estoy feliz!'})

    def on_start(self):
        pass
