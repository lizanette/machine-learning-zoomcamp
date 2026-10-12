import requests

url = 'http://localhost:9696/predict'

customer_id = "xyz-123"
customer = {
  "gender": "female",
  "seniorcitizen": 0,
}

response = requests.post(url, json=customer).json()
print(response)

if response["churn"] == True:
  print('Sending promo email to %s' % customer_id)
else:
  print('Not sending promo email to %s' % customer_id)
