## Flask ETL OpenWeather

#### Este projeto demonstra uma aplicação Flask para realizar uma extração, transformação e carga (ETL) de dados meteorológicos da API OpenWeather em um banco de dados SQLite.

### Aluno: Vinícius Oliveira Fernandes
### Curso: Sistemas de Informação
### Professor: Afonso Cesar Lelis Brandão

### Requisitos:

- Python 3.x instalado
- Pacotes necessários, instaláveis via `pip install flask requests flask_sqlalchemy`

### Passo a Passo:

**1. Configuração do Ambiente Virtual (Opcional, no entanto utilizei nesse exercício porque achei legal :P )**
      Em seu terminal, digite e confirme o seguinte:

    python -m venv venv

**2. Ativação do Ambiente Virtual (Windows)**:
    
Ainda em seu terminal, digite:

Para Windows:
   
    
    .\venv\Scripts\activate
    

Para Linux/Mac, use:
    

    source venv/bin/activate
    

**3. Instalação das Dependências (esse comando instala todas as bibliotecas que utilizei)**

   
    pip install flask requests flask_sqlalchemy
    

**4. Execução da Aplicação**

    
    python app.py
    

**5. Acesso à Aplicação**

   Acesse a aplicação no navegador: [http://127.0.0.1:5001/](http://127.0.0.1:5001/)

A aplicação irá extrair dados meteorológicos de várias cidades da API OpenWeather e armazená-los no banco de dados SQLite.

**6. Teste Automatizado**

Para executar os testes automatizados, rode, subsequentemente, os seguintes comandos:

   
    python test_app.py
   
    python test_app_double_ver.py


Cada arquivo de teste contem conjuntos de testes relacionados a uma determinada funcionalidade ou componente da aplicação. 

Neste caso, um possui um teste mais robusto que o outro (test_app_double_ver.py é o mais robusto). E como boa prática orientada pelo professor, é necessário que haja execução seletiva dos testes para garantir que não haja nenhum gargálo.

Sendo assim, o segundo teste é esperado que haja uma "falha" e que retorne erro para que haja a evidência das possíveis fraquezas e melhoría contínua do desenvolvimento

### Estrutura do Projeto:

- `app.py`: Arquivo principal da aplicação Flask.
- `test_app.py`: Arquivo de teste automatizado.
- `test_app_double_ver.py`: Arquivo de teste automatizado mais robusto (É IMPORTANTE CITAR QUE ESTE É ESPERADO QUE DÊ ERRO para visualização de gargálos)
- `instance/weather_data.db`: Pasta para armazenar o banco de dados SQLite.

### Observações para rodar projeto:

- Certifique-se de que sua máquina está conectada à internet, pois a aplicação faz chamadas à API da OpenWeather;
- Caso deseje utilizar um banco de dados diferente, ajuste a configuração no `app.py`;
- Modificações adicionais podem ser feitas para personalizar ou estender a funcionalidade da aplicação.

### Exemplo do código rodando:

Com a utilização do Visual Code, pude rodar diretamente na IDE utilizando a ferramenta "RUN". A porta 5001 já estava configurada, e o código testado (apenas primeiro teste):

![image_720](https://github.com/Vfernandes1/exercicio_etl_flask/assets/99264567/e1a8b63f-9594-48f1-9fcb-49404ad2ae97)


![image](https://github.com/Vfernandes1/exercicio_etl_flask/assets/99264567/ce2d5038-0bfb-40b6-bfd6-28e5dbf6e882)

Resultado:

![image_720](https://github.com/Vfernandes1/exercicio_etl_flask/assets/99264567/85c0471a-c6cb-4200-af6c-e889a969402c)


### Tecnologia e Ferramentas que foram utilizadas:

**OpenWeather:**

- O OpenWeather é uma plataforma que disponibiliza informações meteorológicas em tempo real para diversas localidades ao redor do mundo. Neste projeto, essa tecnologia é empregada para obter dados sobre as condições climáticas das cidades necessárias, visando análise e armazenamento.

**Python:**

- Python é uma linguagem de programação versátil e de alto nível, amplamente utilizada no desenvolvimento de aplicativos e scripts. No contexto deste projeto, Python é a linguagem principal, sendo empregada na implementação de scripts para manipulação de dados, integração com a API OpenWeather e no desenvolvimento da aplicação Flask.

**Flask:**

- Flask é um framework web em Python que simplifica o desenvolvimento de aplicativos web. Neste projeto, Flask é utilizado para criar uma API simples que consome dados do OpenWeather e disponibiliza informações climáticas.


**SQLite:**

- SQLite é um sistema de gerenciamento de banco de dados relacional leve e incorporado. No projeto, o SQLite é escolhido como o banco de dados para armazenar as informações meteorológicas coletadas. Sua simplicidade e eficiência o tornam uma escolha adequada para projetos menores, proporcionando funcionalidades de banco de dados sem a necessidade de um servidor dedicado.

**SQLAlchemy:**

- SQLAlchemy é uma biblioteca em Python que fornece uma abstração sobre bancos de dados relacionais. No projeto, o SQLAlchemy é utilizado em conjunto com o Flask para facilitar a interação com o banco de dados SQLite. Ele oferece uma maneira mais intuitiva e orientada a objetos de lidar com operações de banco de dados em comparação com o SQL tradicional.

**Unittest:**

- Unittest é o módulo de teste integrado no Python, fornecendo uma estrutura para escrever e executar testes automatizados. No projeto, o Unittest é utilizado para criar testes que verificam o correto funcionamento de diferentes partes da aplicação, garantindo que estas estejam em conformidade com as especificações e evitando regressões durante o desenvolvimento.

### Referências:

Installation — Flask Documentation (3.0.X). (n.d.). https://flask.palletsprojects.com/en/3.0.x/installation/#virtual-environments

datagy. (2023, March 22). Build YOUR OWN Weather App in Python with Flask (COMPLETE Beginner Tutorial) [Video]. YouTube. https://www.youtube.com/watch?v=JCD7YdOSsWI

OpenWeatherMap.org. (n.d.). Weather API - OpenWeatherMap. https://openweathermap.org/api

OpenAI. (2022). GPT-3.5 Architecture. Em OpenAI. https://www.openai.com/ 
