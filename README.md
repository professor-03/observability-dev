# observability-dev
This is my final project as an intern at Elevate_labs where i would be building a complete-observability-system using tools such as prometheus, grafana, loki and jaeger.

Steps:-

1. Apart from establishing the ec2 connection and setting up the required dependencies in the enviroment.
2. I created app directory apart from the root directory inorder to create main.py, requirements.txt, and the dockerfile.
3. Then i created the supporting files in the root directory such as prometheus.yml, loki-config.yml and other files.
4. After finishing the scripting and other things i started building the project using the docker command docker-compose up --build -d.
5. Since i am performing all my projects in ec2 instance so inorder to access the sites, one needs to edit the inbound rules under the security settings and add the required ports such as 3000 (Grafana), 3100 (Loki), 9090 (Prometheus), 16686 (Jaeger), 8000 8001 (App + Metrics).
6. Then the project comes to and end and i pushed everything to this github repo.
7. Attaching the images and signing off.




   See you on board!!
