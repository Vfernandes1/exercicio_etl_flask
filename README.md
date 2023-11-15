## Flask ETL OpenWeather

#### Este projeto demonstra uma aplicação Flask para realizar uma extração, transformação e carga (ETL) de dados meteorológicos da API OpenWeather em um banco de dados SQLite.

### Aluno: Vinícius Oliveira Fernandes
### Curso: Sistemas de Informação
### Professor: Afonso Cesar Lelis Brandão

### Requisitos

- Python 3.x instalado
- Pacotes necessários, instaláveis via `pip install flask requests flask_sqlalchemy`

### Passo a Passo

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

### Estrutura do Projeto

- `app.py`: Arquivo principal da aplicação Flask.
- `test_app.py`: Arquivo de teste automatizado.
- `test_app_double_ver.py`: Arquivo de teste automatizado mais robusto.
- `instance/weather_data.db`: Pasta para armazenar o banco de dados SQLite.

### Observações para rodar projeto:

- Certifique-se de que sua máquina está conectada à internet, pois a aplicação faz chamadas à API da OpenWeather;
- Caso deseje utilizar um banco de dados diferente, ajuste a configuração no `app.py`;
- Modificações adicionais podem ser feitas para personalizar ou estender a funcionalidade da aplicação.

### Referências:

OpenAI. (2022). GPT-3.5 Architecture. Em OpenAI. https://www.openai.com/ 
