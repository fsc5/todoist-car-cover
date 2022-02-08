# todoist-car-cover

A python script that creates a new [Todoist](https://todoist.com) task when you should cover youre car in the evening to protect it from frost.  
It is best suited to run on a small server like a Raspberry pi.

The project uses the todoist api and the openweather api so you will need keys for those.  
Before running the project you should create a `config.yaml` file.  
You can edit the `config.yaml.example` file to youre needs and save it as `config.yaml`.  
To get the project running you should use poetry. To install poetry follow these [instructions](https://python-poetry.org/docs/).  
You can then install all dependencys with `poetry install` and start the script with `poetry run python todoist_cover_car/scheudler.py`
