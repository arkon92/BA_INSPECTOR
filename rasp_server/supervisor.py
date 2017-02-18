import inspector as ins
import time

class Supervisor:
    class __Supervisor:
        def __init__(self, inspector):
            self.inspector = None
        def __str__(self):
            return repr(self)

    instance = None

    def __init__(self, inspector):
        if not Supervisor.instance:
            Supervisor.instance = Supervisor.__Supervisor(inspector)
        else:
            Supervisor.instance.val = id

    def __getattr__(self, inspector):
        return getattr(self.instance, inspector)

    def reset_supervisor(self, id):
            if Supervisor.instance.inspector:
                   Supervisor.instance.inspector.stop_inspector()
                   Supervisor.instance.inspector.join()
            Supervisor.instance = Supervisor.__Supervisor()
            
    def create_inspector(self, inspector):
        if Supervisor.instance.inspector:
                   Supervisor.instance.inspector.stop_inspector()
                   Supervisor.instance.inspector.join()
        Supervisor.instance.inspector = ins.Inspector("1")
        Supervisor.instance.inspector.start_inspector()

    def kill_inspector(self):
        Supervisor.instance.inspector.stop_inspector()

