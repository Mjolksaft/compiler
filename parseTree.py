class parse_tree():
    def __init__(self) -> None:
        self.root = node(None)
        self.assignment = node("assignment").add_child(node("indentifier")).add_child(node("=")).add_child(node("expression"))
        self.expression = node("expression").add_child(node("term"))
        pass
    
    def add(self,lexes):
        self.root = self.get_first_non_terminal(lexes)
        ## expand all non terminals
        non_terminal = self.check_non_terminal(self.root)
        while non_terminal:
            non_terminal = self.check_non_terminal(non_terminal)
        
        print(self.get_values(self.root))

        
    def get_first_non_terminal(self, lexes):
        for lex in lexes:
            if lex[1] == 'assignment':
                return self.expand_assignment()
            
            if lex[1] == 'expression':
                return self.expand_expression()
            
    def check_non_terminal(self, current):
        for child in current.children:
            if child.value == "expression":
                if len(child.children) == 0: ## if the non-terminal does not have children 
                    current.add_child(self.expand_expression()) 
                    return child
            self.check_non_terminal(child)        

    def expand_assignment(self):
        new_node = node("assignment")
        new_node.add_child(node("indentifier"))
        new_node.add_child(node("="))
        new_node.add_child(node("expression"))
    
        return new_node # assigment -> indetifier = expression
    
    def expand_expression(self):
        new_node = node("term")
        return new_node # expressio -> term
    


    def get_values(self, current, visited=[]):
        visited.append(current.value)
        for child in current.children: 
            self.get_values(child, visited)
        
        return visited
    
    # def checkType(lexes):

    #     return # expression -> term
    
class node() : 
    def __init__(self,  value) -> None:
        self.value = value
        self.children = []
        pass
    
    def add_child(self, value): 
        if value in self.children:
            return
        self.children.append(value)