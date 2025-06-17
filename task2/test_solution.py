import os
import csv
import pytest
from solution import main

@pytest.fixture
def setup_file():
    # Запускаем основную функцию для создания файла
    main()
    yield
    # Удаляем файл после тестов
    if os.path.exists('beasts.csv'):
        os.remove('beasts.csv')

def test_file_creation(setup_file):
    """Проверяет, что файл создается"""
    assert os.path.exists('beasts.csv')

def test_file_content_structure(setup_file):
    """Проверяет структуру файла"""
    with open('beasts.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            assert len(row) == 2
            assert row[0] in 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
            assert row[1].isdigit()

def test_all_letters_present(setup_file):
    """Проверяет, что все буквы алфавита присутствуют"""
    with open('beasts.csv', 'r', encoding='utf-8') as f:
        letters = {row[0] for row in csv.reader(f)}
        assert len(letters) == 33
        for letter in 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ':
            assert letter in letters

def test_counts_non_negative(setup_file):
    """Проверяет, что все счетчики неотрицательные"""
    with open('beasts.csv', 'r', encoding='utf-8') as f:
        for row in csv.reader(f):
            assert int(row[1]) >= 0

def test_specific_letter_counts(setup_file):
    """Проверяет конкретные значения для некоторых букв"""
    with open('beasts.csv', 'r', encoding='utf-8') as f:
        counts = {row[0]: int(row[1]) for row in csv.reader(f)}
        # Проверяем, что Ъ, Ы, Ь действительно 0
        assert counts['Ъ'] == 0
        assert counts['Ы'] == 0
        assert counts['Ь'] == 0
        # Проверяем, что другие буквы имеют положительные значения
        assert counts['А'] > 0
        assert counts['Б'] > 0
        assert counts['К'] > 1000  # Обычно много животных на К