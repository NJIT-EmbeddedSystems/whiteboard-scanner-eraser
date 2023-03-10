from python-statemachine import StateMachine, State
import physical.physical
# import scanning.scanning
# import UI.UI

class whiteboardEraser(StateMachine):
    # state definitions
    start       = State(initial=True)
    idle        = State()
    move_fwd    = State()
    idle2       = State()
    process_img = State()
    move_back   = State(final=True)

    def __init__(self):
        # conditions for state changes
        self.execute = False
        self.scanFlag = False
        self.scanEnable = False
        self.eraseFlag = False
        self.eraseEnable = False
        self.limitSwitchE = False
        self.limitSwitchF = False
        # creates controller for fsm
        super(fsmControl, self).__init__()



exit()
