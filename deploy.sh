sudo docker stop polyhistor_backend_1
echo y | sudo docker system prune
sudo docker-compose up --force-recreate -d --build backend
