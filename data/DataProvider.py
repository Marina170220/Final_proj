import json

my_file = open('test_data.json')
global_data = json.load(my_file)


class DataProvider:

    def __init__(self) -> None:
        self.data = global_data

    def get_token(self) -> str:
        return self.data.get("token")
    
    def get_phone(self) -> str:
        return self.data.get("phone")
    
    def get_search_book(self) -> str:
        return self.data.get("search_book")
    
    def get_user_name(self) -> str:
        return self.data.get("name")
    
    def get_comment(self) -> str:
        return self.data.get("comment")
    