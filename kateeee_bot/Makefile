all:
	sudo docker build -t kate_test .
	sudo docker run -d --name kate_test kate_test

del: 
	sudo docker stop kate_test
	sudo docker rm kate_test
	sudo docker rmi kate_test	

shell: 
	sudo docker exec -it kate_test sh 