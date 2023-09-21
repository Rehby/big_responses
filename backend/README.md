python -m venv .env

переходишь в папку backend
.\.env\Scripts\activate

Если будет ошибка, то от админа в консоли
Set-ExecutionPolicy Unrestricted -Force

Запуск сервера
uvicorn app:app --reload

ip:port/docs посмотреть и потрогать апи