import asyncio
import sys

try:
    import aioserial
except ImportError:
    sys.exit("aioserial was not found, try running make or make build")


class Serial:
    def __init__(self, port: str, baud: int):
        self.ser = aioserial.Aioserial(port=port, baudrate=baud)
        self.ser_lock = asyncio.Lock()
    def sendcmd(self):
        pass
    def readcmd(self) -> str:
        return ""