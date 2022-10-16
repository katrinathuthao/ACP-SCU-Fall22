from flask import Flask
import random
import os
# Make this file a minimalist API endpoint that randomly offers a 
# random pick out of 15 meal recommendations along with a price
# The endpoint delivers 1 meal recommendation in JSON format

app =   Flask(__name__)
data = [{'name': 'burger', 'price':10.89},
        {'name':'salad', 'price':9.89},
        {'name':'spaghetti', 'price':11.78},
        {'name':'taco', 'price':4.54},{'name':'ramen', 'price':14.45},
        {'name':'burrito', 'price':9.89},
        {'name':'banana', 'price':0.99},{'name':'veggies', 'price':1.45},
        {'name':'apple', 'price':0.99}, {'name':'strawberry', 'price':0.99},
        {'name':'peach', 'price':0.99},
        {'name':'pear', 'price':0.99},
        {'name':'coffee', 'price':3.78}, {'name':'tea', 'price':3.78},
        {'name':'pizza', 'price':6.89}]


api_endpoint = os.environ.get('API_ENDPOINT',  'meal')
@app.route('/'+api_endpoint)
def get_meal():
    index=random.randint(0,14)
    value = data[index]  
    return value
   
if __name__ == '__main__':
    port=os.environ.get('API_PORT')
    app.run(host="0.0.0.0", debug=True, port=port )
  