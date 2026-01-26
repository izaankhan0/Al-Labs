class Threat:
    def __init__(self, threat_id, name, severity):
        self.threat_id = threat_id
        self.name = name
        self.severity = severity

    def display(self):
        print(f"Threat ID: {self.threat_id}\nName: {self.name}\nSeverity: {self.severity}")

class PhishingThreat(Threat):
    def analyze_email(self):
        print(f"Analyzing emails for {self.name}...")

class RansomwareThreat(Threat):
    def scan_files(self):
        print(f"Scanning files for {self.name}...")

class BotnetThreat(Threat):
    def detect_traffic(self):
        print(f"Detecting network traffic for {self.name}...")

phishing = PhishingThreat(1, "Phishing Attack", "High")
ransomware = RansomwareThreat(2, "Ransomware Attack", "Critical")
botnet = BotnetThreat(3, "Botnet Attack", "Medium")

phishing.display()
phishing.analyze_email()
print("-" * 20)
ransomware.display()
ransomware.scan_files()
print("-" * 20)
botnet.display()
botnet.detect_traffic()