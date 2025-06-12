# Prerequisites
- Python 3.8 or higher
- pip (Python package installer)
- Docker (for containerization)
- virtualenv (recommended)

# Local Testing Lambda Guide
## 1. Clone the Repository
```bash
git clone lone the Repository
```
## 2. build docker image
```bash
cd lambda-python-ocr/app/fastapi
docker build -t fastapi .
```
## 3. run docker image
```bash
docker run -p 8000:8000 fastapi
```
## 4. test the API
```bash
curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" \
  -d '{"version":"2.0","routeKey":"GET /","rawPath":"/","rawQueryString":"","headers":{"accept":"*/*","content-length":"0","host":"localhost:9000","user-agent":"curl/7.64.1","x-forwarded-proto":"http","x-forwarded-port":"9000"},"requestContext":{"accountId":"123456789012","apiId":"api-id","domainName":"localhost:9000","domainPrefix":"localhost","http":{"method":"GET","path":"/","protocol":"HTTP/1.1","sourceIp":"127.0.0.1","userAgent":"curl/7.64.1"},"requestId":"request-id","routeKey":"GET /","stage":"$default","time":"12/Mar/2020:19:03:58 +0000","timeEpoch":1583348638390},"isBase64Encoded":false}'
```

# Local Testing FastApi Guide
## 1. Clone the Repository
```bash
git clone lone the Repository
```
## 2. build docker image
```bash
cd lambda-python-ocr/app/fastapi
docker build -t fastapi-local -f Dockerfile.app .
```
## 3. run docker image
```bash
docker run -p 8000:8000 fastapi-local
```
## 4. test the API
```bash
curl http://localhost:8000/  
```