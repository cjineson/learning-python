https://trinket.io/library/trinkets/create?lang=python3

docker build . --tag passwordgen:0.0.1
docker run passwordgen:0.0.1

docker run -d -p 5000:5000 --restart always --name registry registry:2
docker pull alpine:3.7
docker tag alpine:3.7 localhost:5000/alpine:3.7
docker push localhost:5000/alpine:3.7
docker pull localhost:5000/alpine:3.7

