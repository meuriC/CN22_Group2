from locust import HttpUser, between, task


class ApiUser(HttpUser):

    @task
    def recommendedGames(self):
        self.client.get('api/steam/recommendedGames')

    @task
    def activeusers(self):
        self.client.get('/api/steam/activeusers')

    @task
    def postUser(self):
        self.client.post('/api/users', json={"username": "Bearer","language": "english"})
