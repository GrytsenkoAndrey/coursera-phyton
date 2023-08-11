import requests
import time

# Укажите URL сайта, который хотите проверить
url_list = ["https://kstati.dp.ua"]
# Максимальное количество запросов
max_requests = 10
# Максимальное количество запросов в секунду
requests_per_second = 10

def check_sites(url_list, max_requests, requests_per_second):
    for url in url_list:
        for _ in range(max_requests):
            response = requests.get(url)
            if response.status_code == 200:
                print(url + " Запрос успешен (HTTP 200)")
            elif response.status_code == 500:
                print(url + " Ошибка сервера (HTTP 500)")
            elif response.status_code == 503:
                print(url + " Сервис недоступен (HTTP 503)")
            else:
                print(f"Неожиданный HTTP код: {response.status_code}")

            # Добавляем паузу между запросами
            time.sleep(1 / requests_per_second)


if __name__ == "__main__":
    check_sites(url_list, max_requests, requests_per_second)