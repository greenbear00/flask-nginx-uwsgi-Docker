### 구성
- docker-compose로 flask+uwsgi+nginx를 붙임
- request --[http://localhost:8080]--> nginx --[8080:5000]--> flask+uwsgi [app]

### build
```
./build.sh [start|stop]
```