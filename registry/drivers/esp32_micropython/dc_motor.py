# MorphLab - DC motor spec
# Documents the 25GA-370's ratings. Does not actuate itself - actuation goes
# through an L298NDriver channel; see registry/components/dc_joint.py.
# See docs/datasheets/25GA-370-motor-datasheet.pdf


class DCMotor:
    def __init__(self, name, rated_voltage=12, no_load_rpm=330,
                 stall_torque_kgcm=1.0, rated_current_a=2.8):
        self.name = name
        self.rated_voltage = rated_voltage
        self.no_load_rpm = no_load_rpm
        self.stall_torque_kgcm = stall_torque_kgcm
        self.rated_current_a = rated_current_a
