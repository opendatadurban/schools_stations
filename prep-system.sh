#apt-get update
#apt-get install emacs
#cd ~/
#git clone https://github.com/kmkingsbury/raspberrypi-weather-station.git

#Get Apache Going
#sudo apt-get install apache2
#update-rc.d apache2 enable

#Install the "basics"
sudo apt-get install -y build-essential python-dev python-smbus python-rpi.gpio gpsd gpsd-clients python-gps rrdtool

#Supporting libraries
sudo apt-get install -y php5 php5-dev php-pear libyaml-dev python-rrdtool php5-rrd
#sudo pecl install yaml-0.6.3
#sudo apt-get install -y python-yaml
#sudo python -m pip install wiringpi

#other projects code:
#git clone https://github.com/PrzemoF/bmp183.git
#git clone git://gist.github.com/3151375.git
#git clone https://github.com/adafruit/Adafruit_Python_MCP3008.git
#cd ../Adafruit_Python_MCP3008
git clone https://github.com/adafruit/Adafruit_Python_DHT.git
cd Adafruit_Python_DHT
sudo python setup.py install

sudo python setup.py install
cd ~

# Install python modules
#sudo apt-get install python-numpy python-

# Set up port forwarding
sudo apt-get update -y
#sudo apt-get install -y weavedconnectd
#sudo apt-get upgrade -y
#sudo apt-get update --fix-missing
