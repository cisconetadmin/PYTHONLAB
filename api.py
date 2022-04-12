from os import device_encoding
from typing import Optional
from fastapi import FastAPI
from main import *
from getpass import getpass

app = FastAPI()


@app.get("/")
def get_not_use_interfaces():
    return get_cout()


@app.get("/devices/{hostname}")
def get_not_use_interfaces_on_device(hostname: str):
    device = get_device(hostname)
    
    if device is not None:
        count = get_interface_count_clear_on_device(device)
        return {'interfaces_count': str(count)}
    
    return None

@app.get("/devices")
def get_all_devices():
    return get_devices()
