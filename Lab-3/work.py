class Envoirnment:
    def __init__(self, components):
        self.components = components
    def getPercept(self):
        return self.components
    def patchVun(self, index):
        self.components[index] = "safe"
        
class securityAgent:
    def __init__(self, env):
        self.env = env
        print("\nDisplaying System Status...")
        print(env.components)
    def scanSystem(self):
        print("\n\nInitiating Sys Scanning Protocol...")
        for i in range(len(self.env.components)):
            print(f"Index #{i}: ", end="")
            if (self.env.components[i] != "safe"):
                print(f"Warning: Status {self.env.components[i]}")
            else:
                print(f"Success! Secure")
    def patchSystem(self):
        print("\nInitiating Patching Protocol...")
        for i in range(len(self.env.components)):
            if (self.env.components[i] != "safe"):
                self.env.patchVun(i)
                print(f"Index #{i}: ", end="")
                print(f"Patched")
    def display(self):
        print("\nDisplaying System Status...")
        print(self.env.components)

grid = ["safe", "vunerable", "cracked","safe", "vunerable", "cracked","safe", "vunerable", "cracked"]
env = Envoirnment(grid)
agent = securityAgent(env)
agent.scanSystem()
agent.patchSystem()
agent.display()