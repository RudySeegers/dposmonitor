# dposmonitor
This is a monitoring script which monitors the number of missed blocks for a forging delegate on the Ark Ecosystem, Persona and other blockchains which are a fork of the Ark Ecosystem database structure.

##Installation

Install python 3.6

```
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update
sudo apt-get install python3.6-dev

wget https://bootstrap.pypa.io/get-pip.py
sudo python3.6 get-pip.py
sudo pip3.6 install virtualenv
```

Create a virtual environment (replace myvirtualenv with whatever seems appriopriate)
```
virtualenv myvirtualenv -p python3.6
```

Activate the virtualenv
```
source myvirtualenv/bin/activate
```

Configure the script by adding relevant information to the config file.
