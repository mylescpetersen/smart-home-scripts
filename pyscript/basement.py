# --- Misc for all 'basement' related automations ---
import pyscript_modules.devices as d
import pyscript_modules.mqtt_topics as m
import pyscript_modules.scenes as s


@mqtt_trigger(m.door_button_mqtt, "payload == 'single'")
def door_button_leave():
    scene.turn_on(entity_id=s.away)

@mqtt_trigger(m.door_button_mqtt, "payload == 'double'")
def door_button_arrive():
    light.turn_on(entity_id=d.ceiling_light)
    light.turn_on(entity_id=d.desk_lights)
    switch.turn_on(entity_id=d.monitors)
    