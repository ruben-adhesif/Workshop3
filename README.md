## From Local to Decentralized Computation
```bash
# Compute all your model with pickle
python main.py

# Run the API
python api.py
```
On another terminal
- To get the prediction : 
```bash
curl -X GET "http://127.0.0.1:5000/predict?sepal_length=5.1&sepal_width=3.5&petal_length=1.4&petal_width=0.2"

{
  "models//logistic": 0,
  "models//random": 0,
  "models//svm": 0
}
```
- To get the concensus
```bash
curl -X GET "http://127.0.0.1:5000/consensus?sepal_length=5.1&sepal_width=3.5&petal_length=1.4&petal_width=0.2"

{
  "consensus_prediction": 0
}
```
- To get a balances model (do it on Postman or bash)
```bash
curl --location 'http://127.0.0.1:5000/update_balances' \
--header 'Content-Type: application/json' \
--data '{
    "model_name": "svm", 
    "correct": "True"
}'

{
    "message": "Balance updated successfully"
}
```