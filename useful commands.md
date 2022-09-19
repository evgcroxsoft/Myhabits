# **Useful commands**

## **Celery**

Start **celery beat** from module task_celery 
```bash
celery -A task_celery beat
```
Start **celery worker** from module task_celery 
```bash
celery -A task_celery worker --loglevel=info
```
***
***
***
## **Flower**

Start **flower** from module task_celery 
```bash
celery -A task_celery flower
```
***
***
***
## **Docker**
**Show all containers**
```bash
sudo docker ps
```
**Show all images**
```bash
sudo docker images
```
**Delete images**
```bash
sudo docker image prune
```
**Delete specify image**
```bash
sudo docker rmi -f <images>
```
**Delete all containers**
```bash
sudo docker container prune
```
***
***
***
## **Docker-compose**
**Build or rebuild docker-compose**
```bash
sudo docker-compose -f docker-compose.yml up -d --build
```
**Start docker-compose**
```bash
sudo docker-compose up
```
**Down docker-compose**
```bash
sudo docker-compose down
```
