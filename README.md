# Bluetooth Chat Client and Server

This repository contains a simple Bluetooth chat client and server implemented in Python.

## Client

### client.py

The `client.py` script allows users to connect to a Bluetooth server and send/receive messages.

#### Usage

```bash
python client.py -m [MAC_ADDRESS]
```
Replace `[MAC_ADDRESS]` with the Bluetooth address of the server.

## Server

### server.py

The server.py script sets up a Bluetooth server and waits for clients to connect. Once connected, it allows bidirectional communication with the client.

#### Usage

```bash

python server.py -m [MAC_ADDRESS]

```

Replace `[MAC_ADDRESS]` with the Bluetooth address you want the server to bind to.
Dependencies

Both scripts depend on the following Python packages:

    colorama: For colored terminal output.
    argparse: For parsing command-line arguments.

You can install the dependencies using the following command:

```bash

pip install colorama argparse

```

## Compatibility

These scripts are compatible with Python 3.
