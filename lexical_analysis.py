import string
import parseTree

types = {
    'operators': {
        '=': 'assignment',
        '+': 'expression',
        '-': 'expression',
        '*': 'expression',
        '/': 'expression',
        '<': 'condition'
    }
}
class lexical_analysis():
    def __init__(self, file_name) -> None:
        self.file_name = file_name
    
    def get_file(self):
        with open(f'{self.file_name}', 'r') as file:
            lines = []
            for line in file:
                striped_line = line.strip() # remove the whitespace and newlines
                if '#' in striped_line:
                    striped_line = striped_line.split('#')[0].strip() # if it contains comments remove split the line and append the code and remove the comments
                    
                if striped_line == '': # if the line is empty go to the next line 
                    continue
                
                lines.append(striped_line)
            return lines 
        
    def tokenization(self, lines): 
        # convert the lines into token such as variables names values 
        for line in lines: 
            asd = []
            tree = parseTree.parse_tree()
            splitLine = line.split(" ")
            for word in splitLine:
                if word[0] in string.ascii_lowercase:
                    # if it starts with a letter it is either a indentifier or a keyword
                    asd.append([word, "indentifier"])
                    pass
                
                if word in types.get("operators"):
                    # if the word is a operator 
                    asd.append([word, types['operators'][word]])
                    pass         
                       
                if word[0].isnumeric() or word[0] == '"' and word[len(word)-1] == '"':
                    # if it is numerical we can assume that its a literal
                    # if it starts and ends with a "" the it is a string literal 
                    asd.append([word, "literal"])
                    pass
            tree.add(asd)
            # for i in tree.root.children:
            #     print(i.value)
        pass
    
lexical = lexical_analysis('test.py')

lines = lexical.get_file()
# print(lines)
tokens = lexical.tokenization(lines)