import requests


class Request:

    @staticmethod
    def post_request(url, data, headers):
        response = requests.post(url, data=data, headers=headers)
        return response
    
    @staticmethod
    def get_request(url, headers):
        response = requests.get(url, headers=headers)
        return response
    
    @staticmethod
    def put_request(url, data, headers):
        response = requests.put(url, data=data, headers=headers)
        return response
    
    @staticmethod
    def delete_request(url, headers):
        response = requests.delete(url, headers=headers)
        return response