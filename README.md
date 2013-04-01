RoboPi

RoboPi code for use with Raspberry Pi to build a controllable robot.

This is the code I've used to get a two geared motor robot up and running on my raspberry pi. It allows control over http and streams from a webcam attached to the front.

Dependencies needed
python 2.7.3 or greater (tested only on 2.7.3)
python RPi.GPIO
Adafruit occidentalis operating system.
nginx

Installation steps

1. Install nginx
    sudo apt-get install nginx

2. Clone this github code to the Pi.
3. Copy the contents of the www folder to /usr/share/nginx/www/
4. Copy server.py to /home/pi/
5. Copy mjpg_streamer and robopi-server to /etc/init.d/ and make executable:
    sudo chmod +x /etc/init.d/mjpg_streamer
    sudo chmod +x /etc/init.d/robopi-server
6. Set mjpg_streamer and robopi-server to start on boot:
    sudo update-rc.d mjpg_streamer defaults
    sudo update-rc.d robopi-server defaults
7. Install mjpg_streamer - this is outside the scope of this README, head over to http://sourceforge.net/projects/mjpg-streamer/
8. Edit /etc/nginx/sites-enabled/default and under the server directive add these two locations at the end:
        location /webcam/ {
                proxy_pass http://127.0.0.1:8080/;
        }
        location /json/ {
                proxy_pass http://127.0.0.1:8090/;
        }
9. Edit /home/pi/server.py and set the pin configuration that you have chosen to use to connect your motors.
10. Reboot your Pi.
11. Login to http://ip.ip.ip.ip/ and start to control your RoboPi :)
