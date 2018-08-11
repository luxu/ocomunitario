[![Coverage Status](https://coveralls.io/repos/github/MarcusMann/ocomunitario/badge.svg)](https://coveralls.io/github/MarcusMann/ocomunitario) [![Build Status](https://travis-ci.org/MarcusMann/ocomunitario.svg?branch=master)](https://travis-ci.org/MarcusMann/ocomunitario)

# Ocomunitário

Você precisa do docker e docker-compose instalado, antes de continuar.
Também irá precisar configurar as variáveis de ambiente, então crie dois arquivos um chamado .env e o outro .env-psql

Você precisa criar um banco de dados primeiro:

    docker-compose run --service-ports --rm ocomunitario flask db init
	docker-compose run --service-ports --rm ocomunitario flask db migrate
	docker-compose run --service-ports --rm ocomunitario flask db upgrade

Agora rode a aplicação:

    docker-compose run --service-ports --rm ocomunitario flask run -h 0.0.0.0
 