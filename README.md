# devopslab4

## build dockerfile

```
docker build -t devopslab:0.0.1 -f Dockerfile .            
```

## run container

```
docker run -ti -p 5000:5000 --network host -e NEW_RELIC_LICENSE_KEY=license_key devopslab:0.0.1
```

Obs: altere license_key para o valor da sua licença