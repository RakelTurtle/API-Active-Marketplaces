## 🛒 API-Active-Marketplaces
API que retorna quais Marketplaces estão sendo executados no momento. 

<br>

### 🛠️ Instalando o projeto:

- Clone o repositório:
```
$ git clone https://github.com/RakelTurtle/API-Active-Marketplaces.git
$ cd API-Active-Marketplaces/
```

- Crie seu ambiente virtual:
```
$ python3 -m venv venv
```

- E ative seu ambiente virtual:
```
$ source venv/bin/activate
```

- Instale as depencências:
```
$ pip install -r requirements.txt
```

- Crie a estrutura no banco de dados:
``` 
$ python3 manage.py migrate
``` 

- Inicie o servidor de desenvolvimento:
```
$ python3 manage.py runserver
```
<br>

- Visite em seu navegador o endpoint abaixo =D
```
http://127.0.0.1:8000/api/v1/marketplaces/
```
<br>
