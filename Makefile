
build:
	docker build -t autocompany .

run:
	 docker run --name my_app -p 8000:80 -d autocompany

