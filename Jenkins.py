# !/bin/python3

import jenkins
from time import sleep


token = '118c8df204629792403c6898be4c42ef0b'


def jenkins_conn():
    print("connecting to Jenkins...")
    sleep(2)

    jconn = jenkins.Jenkins('http://192.168.137.1:8080', username='pratik025', password=token)
    version = jconn.get_version()
    print('Hello from Jenkins {}'.format(version))

jenkins_conn()
