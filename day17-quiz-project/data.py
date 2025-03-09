import requests

re = requests.get(
    "https://opentdb.com/api.php?amount=10&category=18&difficulty=medium&type=boolean"
)

question_data = re.json().get("results")
