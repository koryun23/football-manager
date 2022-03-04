class TeamNotFoundException(RuntimeError):
    def __init__(self, team):
        super().__init__(f"Team with name '{team.name}' not found.")