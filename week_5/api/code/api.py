from flask import Flask, jsonify
import random
import os
import psycopg2
# Make this file a minimalist API endpoint that randomly offers a 
# random pick out of 15 meal recommendations along with a price
# The endpoint delivers 1 meal recommendation in JSON format

app =   Flask(__name__)

# data = [{'name': 'burger', 'price':10.89},
#         {'name':'salad', 'price':9.89},
#         {'name':'spaghetti', 'price':11.78},
#         {'name':'taco', 'price':4.54},{'name':'ramen', 'price':14.45},
#         {'name':'burrito', 'price':9.89},
#         {'name':'banana', 'price':0.99},{'name':'veggies', 'price':1.45},
#         {'name':'apple', 'price':0.99}, {'name':'strawberry', 'price':0.99},
#         {'name':'peach', 'price':0.99},
#         {'name':'pear', 'price':0.99},
#         {'name':'coffee', 'price':3.78}, {'name':'tea', 'price':3.78},
#         {'name':'pizza', 'price':6.89}]
#SQL query
RECOMMENDATION = (
    """SELECT meal, price FROM meal_rec ORDER BY RANDOM() LIMIT 1;"""
)


api_endpoint = os.environ.get('API_ENDPOINT')

@app.get('/'+api_endpoint)
def get_meal():
   
    db_name = os.environ.get('POSTGRES_DB')
    db_host = os.environ.get('DB_HOST')
    db_pass = os.environ.get('POSTGRES_PASSWORD')
    db_port  = os.environ.get('DB_PORT')
    db_user  = os.environ.get('POSTGRES_USER')
    # db_connection = psycopg2.connect()
    db_connection = psycopg2.connect(database=db_name, 
                                user=db_user, 
                                  password=db_pass, 
                                  host=db_host,
                                  port=db_port)
    cursor = db_connection.cursor()
    cursor.execute(RECOMMENDATION)
    result = cursor.fetchone() 
    print(result)
    print(type(result))
    db_connection.close()
    value = {"meal": result[0], "price": result[1]}
   
    return jsonify(value)
    
   
if __name__ == '__main__':
    port=os.environ.get('API_PORT')
    app.run(host="0.0.0.0", debug=True, port=port )
  