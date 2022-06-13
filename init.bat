python -m venv venv
REM (proxy opcional) --proxy=http://proxyServer:8080
venv\Scripts\pip3 install charset-normalizer Jinja2
venv\Scripts\activate
REM iniciar pytool con 'python src/main.py'