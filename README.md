# API DE PONTOS TURíSTICOS
Uma API que permitirá ver e cadastrar novos pontos turisticos juntamente 
com sua atrações.

Possibilidades:

- Deixar uma avalição do ponto turístico
- Deixar um comentário sobre o ponto turístico


Possui uma documentação de apoio:

![alt text](https://github.com/Felipe500/api-pontos-turisticos-drf/blob/main/screen_1.png?raw=true)

Para rodar o projeto em sua maquina com docker, instale o docker e docker compose e depois execute o seguinte comando:

    git clone https://github.com/Felipe500/api-pontos-turisticos-drf.git && 
    
    cd ./api-pontos-turisticos-drf/ && 
    
    mv .env.example .env &&

    docker-compose up 

# Para rodar sem o docker:
 - Renomeio o arquivo ".env.example" para ".env"

         mv .env.example .env

    
 - instale as dependencias caso seu ambiente de desenvolvimento seja linux: 
    
        sudo apt-get install build-essential install postgresql libpq-dev postgresql-client postgresql-client-common

 - Configure e crie o banco de dados conforme está no arquivo ".env"
 - Entre na pasta "api-pontos-turisticos" e rode os seguintes comandos:
      
       make migrate && make runserver
