class Menu:
    def __init__(self,title,action_handler):
        self.options=[]
        self.title=title
        self.action_handler=action_handler
        self.active=False
    def add_option(self,option):
        self.options.append(option)
    def deactivate(self):
        self.active=False
    def activate(self):
        self.active=True
        print("-"*len(self.title))
        print(self.title)
        print("-"*len(self.title))
        while self.active:
            x=1
            for option in self.options:
                print(f"{x}. {option}")
                x+=1
            choice=input("Enter your choice: ")
            try:
                choice=int(choice)
            except:
                print(f"Invalid choice: {choice}") 
                continue
            if choice<1 or choice>len(self.options):
                print(f"Invalid choice: {choice}") 
                continue
            self.action_handler(self,choice)        