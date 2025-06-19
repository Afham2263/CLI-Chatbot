class ChatMemory:
    def __init__(self, max_turns=3):
        self.max_turns = max_turns
        self.history = []

    def add_turn(self, user_input, bot_response):
        self.history.append(f"User: {user_input}")
        self.history.append(f"Bot: {bot_response}")

        # Keep only the last `max_turns * 2` lines (user + bot per turn)
        if len(self.history) > self.max_turns * 2:
            self.history = self.history[-self.max_turns * 2:]

    def get_context(self):
        return "\n".join(self.history)
