import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    JENKINS_URL = os.getenv('JENKINS_URL', 'http://192.168.6.13:8080')
    JENKINS_JOB_ITEMS = os.getenv('JENKINS_JOB_ITEMS', 'Minecraft%20Items')
    JENKINS_JOB_TELEPORT = os.getenv('JENKINS_JOB_TELEPORT', 'Minecraft%20Teleport')
    JENKINS_USER = os.getenv('JENKINS_USER', 'bryan')
    JENKINS_TOKEN = os.getenv('JENKINS_TOKEN', 'your-default-token')
