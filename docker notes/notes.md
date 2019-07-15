- Creating machine:
docker-machine create <name>

- Starting machine:
docker-machine start <name>

- Connecting:
docker-machine ssh <name>

- Running container:
docker container run <params> <port> <image>
ex: docker container run -it -p 80:80 nginx
	params:
		-it: Running as foreground
		-d: Running as background
		--name <name>: renames the container that will be run

Acessing toolbox container: http://192.168.99.100/ (always)

- Showing all containers
docker container ls -a
docker ps -a

- Removing container
docker container rm <id>
# Note: Only first 3 chars required for container id

- Showing all images saved locally
docker images

- Removing image
docker image rm <id>
	-f: remove while running

- Pulling image manually
docker pull <name>

- Editing files
docker container exec <params> <name> <option>

- Removing all containers
docker rm $(docker ps -aq) -f

### Ports:
default ignx: 8080
httpd: 8081
mysql: 3306

### IF A PORT DOES NOT CONNECT:

- Go to virtualbox
- Machine config, network
- Advanced, port
- New rule: host and guest ports for the target one (like 8081 for httpd), others empty
- Done!






















