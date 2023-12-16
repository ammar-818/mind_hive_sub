# mind_hive_sub
Mind Hive assessment submission.

# Pre-requisite
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
3. See the API docs from 
3. Request from the endpoint to see the response body.
