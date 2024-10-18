# uuv_mission/control.py
class PIDController:
    def __init__(self, KP=0.15, KD=0.6):
        self.KP = KP
        self.KD = KD
        self.previous_error = 0

    def compute_control_action(self, reference, output):
        error = reference - output
        derivative = error - self.previous_error
        control_action = self.KP * error + self.KD * derivative
        self.previous_error = error
        return control_action
    


