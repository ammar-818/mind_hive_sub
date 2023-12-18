# Mind Hive Assessment
## Repository Tree
```
.
├── app
│   ├── data
│   │   ├── zus_data.json
│   │   └── zus_geolocation.json
│   ├── coordinate.py
│   ├── main_api.py
│   ├── main_ui.py
│   ├── scraper.ipynb
│   └── utils.py
├── .gitignore
├── LICENCE
├── README.md
└── requirements.txt
```

# Getting Started
1. Fork and clone this repository.
2. Within the repo, create virtual environment with the following command
```
python3.9 -m venv venv
```
3. Activate the environment with
```
venv/Scripts/Activate.ps1        # powershell
venv/Scripts/Activate            # gitbash
source venv/bin/activate         # zsh
```
4. Install packages and libraries with
```
pip install -r requirements.txt
```

# Run API locally
1. `cd` into `/app`
2. Execute the following command
```bash
uvicorn main_api:app --reload
```
3. See the API docs from http://127.0.0.1:8000/docs
3. Request from the endpoint to see the response body.

## API Endpoints

- `/location`
  - Given parameter `branch_name` of the outlet, this endpoint will return the *latitude* and *longitude* of the outlet.
- `/distance`
  - Given two points of outlet, this endpoint will return the distance between the outlets and check whehter it is within 5 km of radius by returning Boolean.
 
## Database
- Assumed `json` file as a simple database. 
