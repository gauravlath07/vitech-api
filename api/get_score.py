import falcon
import json
import sys
from insurance_predict import insurance_predict

class get_score(object):

    def __init__(self):
        self.ins = insurance_predict()

    def on_get(self, req, resp):
        msg = {
            'works?': 'YEAH GET WORKS !!'
        }
        resp.body = json.dumps(msg)
        resp.status = falcon.HTTP_200
        print(resp.status)

    def on_post(self, req, resp):
        # print('post')
        # resp.body = json.dumps("yeah we can post")

        data = req.stream.read(req.content_length or 0)
        data = data.decode("utf-8") 
        json_data = json.loads(data)
        customer_data = json_data['customer_data']
        result = self.ins.get_data(customer_data)
        result = str(result)

        resp.status = falcon.HTTP_201
        msg = {
            'cust_data': result
        }

        resp.body = json.dumps(msg)

