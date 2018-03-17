class ModuleIR:
    def __init__(self, functions):
        self.functions = functions

class FunctionIR:
    def __init__(self, name):
        self.name = name
        self.entryBlock = BlockIR()
        self.arguments = []

    def addArgument(self):
        reg = VirtualRegister()
        self.arguments.append(reg)
        return reg

class BlockIR:
    def __init__(self):
        self.instructions = []

    def append(self, instruction):
        self.instructions.append(instruction)

    def __repr__(self):
        return "\n".join(map(str, self.instructions))

class InstructionIR:
    pass

class TwoOpInstrIR(InstructionIR):
    def __init__(self, operation, target, a, b):
        self.operation = operation
        self.target = target
        self.a = a
        self.b = b

    def __repr__(self):
        return f"{self.target} = {self.a} {self.operation} {self.b}"

class InitializeInstrIR(InstructionIR):
    def __init__(self, vreg, value):
        self.vreg = vreg
        self.value = value

    def __repr__(self):
        return f"{self.vreg} = {self.value}"

class MoveInstrIR(InstructionIR):
    def __init__(self, target, source):
        self.target = target
        self.source = source

    def __repr__(self):
        return f"{self.target} = {self.source}"

class ReturnInstrIR(InstructionIR):
    def __init__(self, vreg = None):
        self.vreg = vreg

    def __repr__(self):
        return f"return {self.vreg}"

class VirtualRegister:
    def __init__(self):
        self._name = newUniqueName()

    @property
    def name(self):
        return self._name

    def __repr__(self):
        return self.name

uniqueNameCounter = 0
def newUniqueName():
    global uniqueNameCounter
    uniqueNameCounter += 1
    return f"#{uniqueNameCounter}"