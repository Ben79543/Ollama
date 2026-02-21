from core.base_agent import BaseAgent
from child_agents.agent_exemple1.agent import AgentExemple1

class Chatbot(BaseAgent):
    """Agent principal (chatbot) qui orchestrer les appels aux agents enfants."""

    def __init__(self):
        super().__init__(name="chatbot")
        self.child_agents = {
            "exemple1": AgentExemple1()
        }

    def execute(self, user_input: str) -> str:
        """Traite l'entrée utilisateur et délègue aux agents enfants si nécessaire."""
        if "exemple1" in user_input.lower():
            return self.child_agents["exemple1"].execute(user_input)
        else:
            return self.query_model(f"Réponds à l'utilisateur: {user_input}")

    def route_to_child(self, agent_name: str, task: str) -> str:
        """Achemine la tâche vers un agent enfant spécifique."""
        if agent_name in self.child_agents:
            return self.child_agents[agent_name].execute(task)
        else:
            return f"Agent {agent_name} non trouvé."
