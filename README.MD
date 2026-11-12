# Mouse-Controlled Robotic Arm

A Python project for controlling a three-axis robotic arm from a computer mouse. The planned interface uses Pygame to display the arm's movement and communicates with an Arduino over a serial (UART) connection.

> **Status:** Work in progress. The serial communication and arm-control logic are not yet fully implemented.

## Requirements

- Python 3
- An Arduino connected over USB
- `make`
- `arduino-cli` for Arduino tooling

Python dependencies are listed in [`requirements.txt`](requirements.txt).

## Setup

Create and activate a virtual environment from the project directory:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the Python dependencies:

```bash
make build
```

Install and configure [`arduino-cli`](https://arduino.github.io/arduino-cli/latest/installation/) separately if you need to build or upload the Arduino firmware.

## Usage

Connect the Arduino, then start the application with:

```bash
make run
```

The Makefile provides:

| Command | Description |
| --- | --- |
| `make build` | Install the Python dependencies |
| `make run` | Start the Python application |

## Hardware and communication

The computer communicates with the Arduino through a serial UART connection. Before running the application, verify the Arduino port and baud rate match the firmware configuration. The current Python configuration uses a baud rate of `112500`; the serial port still needs to be configured.

## Project layout

| File | Purpose |
| --- | --- |
| [`main.py`](main.py) | Application configuration and entry point |
| [`serial.py`](serial.py) | Serial communication wrapper |
| [`requirements.txt`](requirements.txt) | Python dependencies |
| [`Makefile`](Makefile) | Build and run commands |
