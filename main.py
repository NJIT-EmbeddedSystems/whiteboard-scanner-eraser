from statemachine import StateMachine, State
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
    cams_off    = State()
    motors_off  = State()
    move_back   = State()

    # state transitions
    execute = start.to(idle)
    idle.to(move_fwd)
    move_fwd.to(idle2)
    
    idle2.to(process_img)
    process_img.to(idle2)
    idle2.to(move_back)
    move_back.to(start)

    # events

    def __init__(self):
        # conditions for state changes
        self.execButton   = False
        self.scanFlag     = False
        self.scanEnable   = False
        self.eraseFlag    = False
        self.eraseEnable  = False
        self.limitSwitchE = False
        self.limitSwitchF = False
        # creates controller for fsm
        super(fsmControl, self).__init__()

    
    def flagSatisfied(self):
        #checks for scanFlag,eraseFlag



exit()
