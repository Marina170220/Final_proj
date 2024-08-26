import json

with open("C:/Users/User-home/Skypro_AT_projects/Final_Project/Final_proj/test_data.json", "r", encoding='utf8') as my_file:
    data = my_file.read()
global_data = json.loads(data)

class DataProvider:

    def __init__(self) -> None:
        self.data = global_data

    def get_token(self) -> str:
        return self.data["token"]
    
    def get_phone(self) -> str:
        return self.data["phone"]
    
    def get_search_book(self) -> str:
        return self.data["search_book"]
    
    def get_user_name(self) -> str:
        return self.data["name"]
    
    def get_comment(self) -> str:
        return self.data["comment"]
