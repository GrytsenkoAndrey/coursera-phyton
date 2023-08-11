import requests
import time

# Укажите URL сайта, который хотите проверить
url = "https://vesti.ua/"
# Максимальное количество запросов
max_requests = 20
# Максимальное количество запросов в секунду
requests_per_second = 10

def check_site(url, max_requests, requests_per_second):
    for _ in range(max_requests):
        response = requests.get(url)
        if response.status_code == 200:
            print("Запрос успешен (HTTP 200)")
        elif response.status_code == 500:
            print("Ошибка сервера (HTTP 500)")
        elif response.status_code == 503:
            print("Сервис недоступен (HTTP 503)")
        else:
            print(f"Неожиданный HTTP код: {response.status_code}")

        # Добавляем паузу между запросами
        time.sleep(1 / requests_per_second)


if __name__ == "__main__":
    check_site(url, max_requests, requests_per_second)