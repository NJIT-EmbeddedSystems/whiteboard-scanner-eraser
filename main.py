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

exit()
