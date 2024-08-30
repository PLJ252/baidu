import requests
from bs4 import BeautifulSoup

def fetch_baidu_results(query, num_results=10):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    search_url = f"https://www.baidu.com/s?wd={query}"
    
    response = requests.get(search_url, headers=headers)
    response.raise_for_status()  # Ensure we notice bad responses
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    results = []
    for i, result in enumerate(soup.find_all('h3', class_='t'), start=1):
        if i > num_results:
            break
        title = result.get_text()
        link = result.find('a')['href']
        results.append({'title': title, 'link': link})
    
    return results

def save_results_to_file(results, filename="results.txt"):
    with open(filename, 'w', encoding='utf-8') as f:
        for result in results:
            f.write(f"Title: {result['title']}\nLink: {result['link']}\n\n")

if __name__ == "__main__":
    query = "美白"
    num_results = 10
    results = fetch_baidu_results(query, num_results)
    save_results_to_file(results)
    print(f"Saved {num_results} results to results.txt")
