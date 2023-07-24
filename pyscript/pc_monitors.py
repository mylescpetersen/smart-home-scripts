# --- PC & Monitors ---
import pyscript_modules.devices as d
import pyscript_modules.device_info.mac as mac


# Send WOL packet to PC if monitors turn on
@service
@state_trigger(f"{d.monitors} == 'on'")
def wol_pc():
    wake_on_lan.send_magic_packet(mac=mac.pc_mac)

