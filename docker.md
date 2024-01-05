Docker installation 
`sudo pacman -S docker
`sudo systemctl start docker
`sudo systemctl enable docker
To run Docker commands without using `sudo`, add your user to the `docker` group:
`sudo usermod -aG docker $USER

**Install Docker Compose:**`
`sudo pacman -S docker-compose


**Install bWAPP On Docker Compose**

`version: '3'
`services:
  `bwapp:
    `image: raesene/bwapp
    `ports:
      `- "80:80"
      `- "3306:3306"
    `restart: always
`
Save this content in a file named `bwapp-compose.yml`

To Start bwapp docker
`docker-compose -f bwapp-compose.yml up -d

To Stop
`docker-compose -f bwapp-compose.yml down
`

`
