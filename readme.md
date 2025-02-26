#  RunTrak

Simple web app made to learn flask and python.
![index.html](/images/index.png "Main Page")

The main idea is to record the progress of the training/running sessions in real life, so I can check the progress or evolution (if there's any).

The data is entered through a form, to sqlite, and it's represented in some simple graphs.
![table.html](/images/table.png "Table showing data")

And then showed in a basic chart.
![table.html](/images/chart.png "Line Chart for distance")


## Deploy with docker:
Docker build:
```bash
docker build -t runtrak.v01 .
```

Run the container
```bash
docker run -d -p 5000:5000 --name runtrak runtrak.v01
```
Docker compose example:
```yaml
services:
  runtrak:
    build:
      context: .
      dockerfile: Dockerfile
    image: runtrak.v01
    container_name: runtrak
    ports:
      - 5000
    restart: unless-stopped
```

Backup the sqlite file from the container to the host.
```bash
current_date=$(date +%d%m%Y) | docker cp runtrak:/app/data.db runtrak${current_date}.db
```

To do the opposite and load a backup to the container:
```bash
docker cp ${backup_filename}.db runtrak:/app/data.db
```

### TODO:
+ Secure db input/output

