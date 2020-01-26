# cl_python_2020

## Python scripts for network automation lab

### Python virtual environment settings on CentOS

* Enable the EPEL repository with:
  * yum install epel-release
* Install python and python-pip packages with:
  * yum install python python-pip
* Install git
  * yum install git
* Install virtualenv
  * pip install -U virtualenv  
* Clone the git repo
  * git clone https://github.com/jagadnag/cl_python_2020.git
* Navigate to the directory
  * cd cl_python_2020
* Create a python virtual environment
  * virtualenv venv --python=python2.7
* Activate the venv
  * source venv/bin/activate
* Install the python package
  * pip install netmiko
  * pip install napalm
  * pip install jupyter
* Verify the python pip packages
  * pip list
* Run the scripts
  * python <script_name>.py 
* Deactivate the virtual environment 
  * deactivate
