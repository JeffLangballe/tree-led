# Tree LED

Controls WS2811 LED lights on Christmas tree

## Usage
sync code to Raspberry Pi with `./sync.sh`

Run code (on Pi) with `./serve.sh`

## Endpoints

App is served from Pi (assumed 192.168.0.122) on port 5000. The tree
can be controlled using HTTP requests

`POST /brightness/<brightness>` Where brightness is between 0.0 and 1.0

`POST /colour/<r>/<g>/<b>` Where r,g,b are between 0 and 255
