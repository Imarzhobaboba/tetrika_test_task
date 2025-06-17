import requests
import time

S = requests.Session()
URL = "https://ru.wikipedia.org/w/api.php"

def get_category_members(category_title, cmtype=None):
    """
    Получает список всех элементов категории (страниц и подкатегорий) с обработкой пагинации.
    """
    params = {
        'action': 'query',
        'format': 'json',
        'list': 'categorymembers',
        'cmtitle': category_title,
        'cmlimit': 500,
        'cmtype': cmtype or 'page|subcat'
    }
    members = []
    while True:
        response = S.get(URL, params=params)
        data = response.json()
        if 'error' in data:
            raise Exception(f"API Error: {data['error']}")
        if 'query' in data:
            members.extend(data['query']['categorymembers'])
        if 'continue' in data:
            params.update(data['continue'])
        else:
            break
        time.sleep(0.1)
    return members

def main():
    root_category = "Категория:Животные_по_алфавиту"
    russian_letters = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    counts = {letter: 0 for letter in russian_letters}
    alphabets = get_category_members(root_category, cmtype='subcat')
    
    all_pages = []
    
    # Страницы корневой категории
    all_pages.extend(get_category_members(root_category, cmtype='page'))
    
    for alphabet in alphabets:
        # Страницы в подкатегориях алфавита
        all_pages.extend(get_category_members(alphabet['title'], cmtype='page'))
        
        # Подкатегории букв внутри алфавита
        letter_subcats = get_category_members(alphabet['title'], cmtype='subcat')
        for subcat in letter_subcats:
            all_pages.extend(get_category_members(subcat['title'], cmtype='page'))
    
    # Подсчёт количества животных по русским буквам
    for page in all_pages:
        first_char = page['title'][0]
        if first_char in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя':
            first_char = first_char.upper()
        if first_char in counts:
            counts[first_char] += 1
    
    # Запись результатов в файл
    with open('beasts.csv', 'w', encoding='utf-8') as f:
        for letter in russian_letters:
            f.write(f"{letter},{counts[letter]}\n")

if __name__ == "__main__":
    main()