# --- Networking-related ---
import pyscript_modules.entities as e

# Send phone notification if home IP changes
@service
@state_trigger(f"{e.home_ext_ip} != {e.home_ext_ip}.old")
def notify_ip_change():
    eval(e.notify_pixel_6)(title="Home IP Address Changed", message=f"New IP: {eval(e.home_ext_ip)}")
    eval(e.notify_pixel_tablet)(title="Home IP Address Changed", message=f"New IP: {eval(e.home_ext_ip)}")

