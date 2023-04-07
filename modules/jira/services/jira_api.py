import requests
import base64

# Данные для авторизации в Jira
username = 'zhibinov.victor.lvl99@gmail.com'
password = 'qyfgoq-qapnaq-xaNwo2'

# Ключ задачи, к которой нужно прикрепить файл
issue_key = 'AP-18'

# Путь к файлу, который нужно прикрепить
file_path = '/home/zeus/PycharmProjects/jira_controller/modules/github/111.zip'

# Получаем содержимое файла в Base64 формате
with open(file_path, 'rb') as f:
    file_content = base64.b64encode(f.read()).decode('utf-8')

# Формируем запрос
url = f'https://lvl99-betapps.atlassian.net/rest/api/2/issue/{issue_key}/attachments'
headers = {
    'Authorization': f'Basic {base64.b64encode(f"{username}:{password}".encode("utf-8")).decode("utf-8")}',
    'Content-Type': 'multipart/form-data'
}
data = {
    'file': ('111.zip', file_content)
}

# Отправляем запрос
response = requests.post(url, headers=headers, files=data)

# Обрабатываем ответ
if response.status_code == 200:
    attachment = response.json()
    print(f"Файл {attachment['filename']} успешно прикреплен к задаче {issue_key}")
else:
    print(f"Не удалось прикрепить файл к задаче {issue_key}. Код ошибки: {response.status_code}")
