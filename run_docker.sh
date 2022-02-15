git pull

echo Killing old Docker processes
docker-compose rm -fs

echo Building Docker images
docker-compose build

echo Starting Docker containers
docker-compose up -d kowl
docker-compose up -d stream

docker ps -a | grep Exit
