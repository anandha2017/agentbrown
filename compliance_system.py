from autogen import AssistantAgent, UserProxyAgent, GroupChat, GroupChatManager
import json
from datetime import datetime
import os

class ComplianceAudit:
    def __init__(self):
        self.log = []
        
    def record(self, agent, message, decision):
        entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "agent": agent.name,
            "message": message,
            "decision": decision,
            "fca_references": self._extract_fca_refs(message)
        }
        self.log.append(entry)
        return entry

    def _extract_fca_refs(self, text):
        return [ref.strip() for ref in text.split() if ref.startswith("FCA")]

class ComplianceSystem:
    def __init__(self):
        self.config = self.load_config()
        self.audit = ComplianceAudit()
        self.agents = self.initialize_agents()
        
    def load_config(self):
        config_path = os.getenv("COMPLIANCE_CONFIG_PATH", "config/azure_openai_config.json")
        with open(config_path) as f:
            config = json.load(f)
            config["api_key"] = os.getenv("AZURE_OPENAI_API_KEY")  # Get key from environment
            return config
            
    def initialize_agents(self):
        return {
            "text_reviewer": AssistantAgent(
                name="FCA_Text_Validator",
                system_message="""Specialist in FCA TEXT 2.1 guidance. Validate:
                - Clear, fair, not misleading statements (FCA COBS 4.2)
                - Balanced risk/reward presentation (FCA PRIN 2.1)
                - No absolute security claims (FCA COBS 4.7)
                - Proper 'capital at risk' disclosures (FCA COBS 14.3)""",
                llm_config={"config_list": [self.config]}
            ),
            "risk_analyst": AssistantAgent(
                name="Risk_Disclosure_Checker",
                system_message="""Validate risk disclosures against:
                - FCA DISP 3.1.4R (prominent warnings)
                - FCA COBS 14.3.2 (withdrawal restrictions)
                - FCA COBS 4.2.5 (past performance disclaimers)""",
                llm_config={"config_list": [self.config]}
            ),
            "compliance_manager": GroupChatManager(
                groupchat=GroupChat(agents=[], messages=[]),
                system_message="Orchestrate compliance reviews between specialists"
            )
        }

    def review_content(self, content):
        review_process = [
            self.agents["text_reviewer"],
            self.agents["risk_analyst"]
        ]
        
        for agent in review_process:
            response = agent.send(content)
            self.audit.record(agent, response, "REVIEWED")
            
        return self.audit.log

if __name__ == "__main__":
    system = ComplianceSystem()
    test_content = "Sample banking content requiring compliance review"
    audit_log = system.review_content(test_content)
    print("Compliance Review Completed. Audit Log:")
    print(json.dumps(audit_log, indent=2))
