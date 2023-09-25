import subprocess
from typing import Any

class MinioClient:
    def __init__(self, endpoint: str, access_key: Any = None, secret_key: Any = None, secure: bool = True, cert_check: bool = True):
        self.endpoint = endpoint
        self.access_key = access_key
        self.secret_key = secret_key
        self.secure = secure
        self.cert_check = cert_check
        self.set_alias()

    def set_alias(self):
        protocol = ''
        if self.secure == True:
            protocol = "https://"
        elif self.secure == False:
            protocol = "http://"
        command = ''
        if self.cert_check == True:
            command = f"mc alias set mcadminclient {protocol}{self.endpoint} {self.access_key} {self.secret_key}"
        else:
            command = f"mc alias set mcadminclient {protocol}{self.endpoint} {self.access_key} {self.secret_key} --insecure"
        subprocess.run(command, shell=True)

    def create_user(self, access_key, secret_key):
        if self.cert_check == True:
            full_command = f"mc admin user add mcadminclient {access_key} {secret_key}"
        else:
            full_command = f"mc admin user add mcadminclient {access_key} {secret_key} --insecure"
        process = subprocess.Popen(full_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        if process.returncode != 0:
            return f"An error occurred: {stderr.decode()}"
        return stdout.decode()