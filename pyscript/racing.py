# --- Racing ---
import pyscript_modules.mqtt_topics as m

# Change PC's default monitor + audio output based on physical button presses
# Helpful for programs opening on the correct monitor

# Single press --> Racing monitor, no VR
@service
@mqtt_trigger(m.racing_button_mqtt, "payload == 'single'")
def set_racing_no_vr():
    button.press(entity_id="button.myles_pc_audio_monitor")
    button.press(entity_id="button.myles_pc_main_monitor_racing")

# Double press --> Racing monitor, no vr
@service
@mqtt_trigger(m.racing_button_mqtt, "payload == 'double'")
def set_racing_vr():
    button.press(entity_id="button.myles_pc_audio_vr")
    button.press(entity_id="button.myles_pc_main_monitor_racing")


# Single press --> Reset to normal main monitor
@service
@mqtt_trigger(m.racing_button_mqtt, "payload == 'long'")
def disable_racing():
    button.press(entity_id="button.myles_pc_audio_headphones")
    button.press(entity_id="button.myles_pc_main_monitor_4k")
    