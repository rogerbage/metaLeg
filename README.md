# metaLeg
Metadados sobre a legislação brasileira (Decretos Presidenciais e Leis Ordinárias)

A MetaLeg é um gerador de gráficos para análise de Decretos Presicenciais e Leis Ordinárias do Brasil, feito com Python e Django. 

Instruções:
 - Instale o Python em sua maquina (python3);
 - Copie o código do projeto do github;
    - git clone https://github.com/rogerbage/metaLeg.git
 - Baixe o banco de dados com os decretos e leis ordinárias (de 1851 a 15 de janeiro de 2023) e ponha o arquivo na raiz do projeto. 
    -  https://drive.google.com/file/d/1zLkAmPo0Bt-jtHH-jSM2XszHbZIuHSOZ/view?usp=share_link

 - Execute os comandos:
    - pip install --upgrade pip
    - pip install --no-cache-dir -r requirements.txt
    - python3 manage.py makemigrations
    - python3 manage.py migrate
    - python3 manage.py runserver
