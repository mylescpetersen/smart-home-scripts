# --- TV ---
import pyscript_modules.devices as d

@state_trigger(f"{d.tv} == 'off'")
def tv_turns_off():

    TV_LIGHT_LOOP_SEC = 15

    # Turn off TV speakers
    switch.turn_off(entity_id=d.speakers)

    # Turn TV light back on if TV restarts within window
    if eval(d.tv_light) == 'on':

        light.turn_off(entity_id=d.tv_light)

        sec = 0
        while sec < TV_LIGHT_LOOP_SEC: 
            if eval(d.tv) == "on":
                light.turn_on(entity_id=d.tv_light)
                return
            task.sleep(1)
            sec += 1


@state_trigger(f"{d.tv} == 'on'")
def tv_turns_on():
    log.debug(d.speakers)
    switch.turn_on(entity_id=d.speakers)

