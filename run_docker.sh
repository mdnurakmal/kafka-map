git pull

echo Killing old Docker processes
docker-compose rm -fs

echo Building Docker images
docker-compose build

echo Starting Docker containers
docker-compose up -d kowl
docker-compose up -d stream
#docker-compose up -d stream2
docker-compose up -d frontend
docker-compose up -d temp

sudo docker ps -a | grep Exit
