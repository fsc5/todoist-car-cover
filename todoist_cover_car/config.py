import yaml

class Config:
    todoist_key:str
    project_id:int
    section_id:int
    task_content:str
    openweather_key:str
    latitude:str
    longitude:str
    checking_time:str
    log_folder:str
    log_base_name:str


    def load(self,path:str):
        config = yaml.safe_load(open(path))
        self.todoist_key = config["todoist_key"]
        self.project_id = config["project_id"]
        self.section_id = config["section_id"]
        self.task_content = config["task_content"]
        self.openweather_key = config["openweather_key"]
        self.latitude = str(config["latitude"])
        self.longitude = str(config["longitude"])
        self.checking_time = config["checking_time"]
        self.log_folder = config["log_folder"]
        self.log_base_name = config["log_base_name"]