from nautobot.extras.jobs import StringVar
from nautobot.apps.jobs import Job, register_jobs
import subprocess

from nautobot.apps.jobs import Job, register_jobs

class TestDeviceAccess(Job):
    device_ip = StringVar(description="Device IP to test")

    class Meta:
        name = "Test Device Access"

    def run(self, device_ip):
        self.log(message=f"{device_ip}")
        ip = device_ip
        result = subprocess.run(["ping", "-c", "3", ip], capture_output=True, text=True)
        if result.returncode == 0:
            self.logger.info(f"Device {ip} is reachable from worker.")
        else:
            self.logger.error(f"Device {ip} not reachable. Output:\n{result.stderr}")
register_jobs(TestDeviceAccess)
