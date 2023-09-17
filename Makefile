
build:
	docker build -t autocompany .

run:
	 docker run -p 8000:80 -d autocompany

