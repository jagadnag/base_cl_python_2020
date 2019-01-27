# cluer_python_2019

## Python scripts for network automation

### Python virtual environment settings on CentOS

* Enable the EPEL repository with:
  * yum install epel-release
* Install python and python-pip packages with:
  * yum install python python-pip
* Install git
  * yum install git
* Clone the git repo
  * git clone https://github.com/jagadnag/cluer_python_2019.git
* Navigate to the directory
  * cd cluer_python_2019
* Create a python virtual environment
  * virtualenv venv --python=python2.7
* Activate the venv
  * source venv/bin/activate
* Install the python package
  * pip install netmiko
* Verify the python pip packages
  * pip list
* Deactivate the virtual environment 
  * deactivate
