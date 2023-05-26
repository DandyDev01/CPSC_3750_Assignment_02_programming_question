
from Models.Agents.Agent import Agent
from Models.Grid import Grid
from Views.GridView import GridView
from Views.StartView import StartView

class MainController:
    def __init__ (self, startView:StartView, gridView:GridView, defaultInitialState:list, agentX:Agent, agentO:Agent):
        self.startView = startView
        self.gridView = gridView
        self.agentX = agentX
        self.agentO = agentO
        self.defaultStartState = Grid(defaultInitialState)

    def run(self):
        gameState = self.defaultStartState
        
        self.gridView.display(gameState)

        for i in range(0, 6):
            gameState = self.agentX.make_move(gameState)
            self.gridView.display(gameState)
            gameState = self.agentO.make_move(gameState)
            self.gridView.display(gameState)
        
        self.gridView.display(gameState)
        


    def check_for_winner(self, agentX:Agent, agentO:Agent, gameState:Grid):
        if agentX.has_goal(gameState, agentX.team):
            return True

        if agentO.has_goal(gameState, agentO.team):
            return True

        return False