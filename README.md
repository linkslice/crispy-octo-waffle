# crispy-octo-waffle
A Minecraft Admin Web App

Assuming you have jenkins and ansible and a docker host running a minecraft bedrock server, you too can run this flask app to allow your users to cheat at minecraft if you so desire. 

![Alt text](/screenshots/items.png?raw=true "Give yourself crap")

![Alt text](/screenshots/teleport.png?raw=true "Go anywhere")



Usage:
````
 docker run -p 5000:5000 \
   -e JENKINS_URL=http://<your.jenkins.host>:8080 \
   -e JENKINS_JOB_ITEMS="Minecraft%20Items" \
   -e JENKINS_USER="<username>" \
   -e JENKINS_TOKEN="<your token>" \
   linkslice/minecraft-webapp
````
