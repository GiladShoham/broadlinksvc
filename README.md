# Broadlinksvc Docker
__________________________________________

Ubuntu based image running python script that Allows us to interact with Brodlink Devices over http <br/>
In order to list, learn and send commands.

## Base Image
`From ubuntu:18.04` described [here](https://hub.docker.com/_/ubuntu).


## Usage
### Run from hub
#### docker run from hub
```text
docker run --name broadlinksvc -p "7020:7020" techblog/broadlinksvc:latest
```

#### docker-compose from hub
```yaml
version: "3.6"
services:
  redalert:
    image: techblog/broadlinksvc
    container_name: broadlinksvc
    restart: always
    restart: unless-stopped
    ports: 
      - "7020:7020"
```



