import requests

api_key = '84dad13096ab45cbb08fe1cbcbe1c487'
url = 'https://newsapi.org/v2/everything'

params = {
    'q': 'apple',
    'from': '2024-07-24',
    'to': '2024-07-24',
    'sortBy': 'popularity',
    'apiKey': api_key  
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    articles = data['articles']
    for article in articles:
        title = article['title']
        description = article['description']
        print(f"Title: {title}")
        print(f"Description: {description}")
        print()
else:
    print(f"Error: {response.status_code} - {response.text}")
