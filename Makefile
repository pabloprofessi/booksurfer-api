build:
	docker-compose build

run:
	docker-compose up

testing:
	docker-compose run booksurfer-api py.test --cov-report html:report_html --cov-report term-missing --cov=app tests
