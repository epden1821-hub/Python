class User:
    
    def __init__(self, first_name: str, last_name: str):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
    
    def print_first_name(self):
        print(f"Имя пользователя: {self.first_name}")

    def print_last_name(self):
        print(f"Фамилия пользователя: {self.last_name}")

    def print_full_name(self):
        print(f"Пользователь: {self.first_name} {self.last_name}")
