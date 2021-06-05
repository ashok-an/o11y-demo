from locust import HttpUser, task, between
import json


class QuickstartUser(HttpUser):
    @task(3)
    def get_bugs(self):
        for i in ['andy', 'randy', 'cindy', 'mindy', 'sandy', 'joe']:
          self.client.get(f'/bugs?user_id={i}')

