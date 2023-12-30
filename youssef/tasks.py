from celery import shared_task
import subprocess

@shared_task
def add(x, y):
    result = x + y
    print(result)
    return result

@shared_task
def scan(host=None):
    command = ['nmap', '-p', '8080,443,5000,8000', host]
    result = subprocess.run(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    return result.stdout.decode()
