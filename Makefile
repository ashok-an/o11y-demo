all: clean build push deploy test
	@echo "All done"

test:
	curl localhost:12345/ping
	curl localhost:23456/ping

clean:
	-docker rm -f test-bugs test-notes

build: clean
	docker build -f Dockerfile.bugs -t ashoka007/test-bugs .
	docker build -f Dockerfile.notes -t ashoka007/test-notes .

push:
	docker push ashoka007/test-bugs
	docker push ashoka007/test-notes

deploy:
	./run_containers.sh
