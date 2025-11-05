# Student Performance Prediction


## Overview
This project predicts student academic performance (pass/fail) based on multiple socio-academic factors such as study time, absences, and parental education.  
It uses a **Decision Tree Classifier** trained on the [UCI Student Performance Dataset](https://archive.ics.uci.edu/ml/datasets/student+performance).

## Dataset
UCI Student Performance dataset:
- `student-mat.csv` → Mathematics students  
- `student-por.csv` → Portuguese students

## Model Params
### Max Depth vs Accuracy
<img width="1604" height="886" alt="image" src="https://github.com/user-attachments/assets/22580f07-57cb-4cd1-96aa-0917dfa66fb5" />
-> max_depth = 6

### Feature Importance
<img width="1853" height="904" alt="image" src="https://github.com/user-attachments/assets/12cf10f9-f3f0-45cf-959f-9846d2960ac9" />
-> We've Choosen only these features for deployment

* **failures** - number of past class failures (numeric: n if 1<=n<3, else 4)
* **absences** - number of school absences (numeric: from 0 to 93)
* **goout** - going out with friends (numeric: from 1 - very low to 5 - very high)
* **freetime** - free time after school (numeric: from 1 - very low to 5 - very high)
* **internet** - Internet access at home (binary: yes or no)
* **schoolsup** - extra educational support (binary: yes or no)
* **paid** - extra paid classes within the course subject (Math or Portuguese) (binary: yes or no)
* **Medu** - mother's education (numeric: 0 - none, 1 - primary education (4th grade), 2 – 5th to 9th grade, 3 – secondary education or 4 – higher education)
* **age** - student's age (numeric: from 15 to 22)
* **famsize** - family size (binary: "LE3" - less or equal to 3 or "GT3" - greater than 3)
* **Mjob** - mother's job (nominal: "teacher", "health" care related, civil "services" (e.g. administrative or police), "at_home" or "other")
* **guardian** - student's guardian (nominal: "mother", "father" or "other")
* **health** - current health status (numeric: from 1 - very bad to 5 - very good)
* **traveltime** - home to school travel time (numeric: 1 - <15 min., 2 - 15 to 30 min., 3 - 30 min. to 1 hour, or 4 - >1 hour)
* **Pstatus** - parent's cohabitation status (binary: "T" - living together or "A" - apart)


## How to run

Two ways to run the Streamlit app.

### Option 1 \- Local (pip + Streamlit)
1. Create and activate a virtual environment:
   - `python3 -m venv .venv`
   - `source .venv/bin/activate`
2. Install dependencies:
   - `pip install -r requirements.txt`
   - If `streamlit` is not in `requirements.txt` run `pip install streamlit`
3. Run the app (replace `app.py` with your script path if different, e.g. `src/app.py`):
   - `streamlit run app.py --server.port 8501 --server.address 0.0.0.0`

### Option 2 \- Docker
1. Build the image from the repository root:
   - `docker build -t student-performance .`
2. Run the container:
   - `docker run --rm -p 8501:8501 student-performance`
3. If your Streamlit script is not `app.py`, override the script path:
   - `docker run --rm -p 8501:8501 -e STREAMLIT_APP=src/app.py student-performance`

Troubleshooting:
- If Streamlit reports "File does not exist", inspect the repo files inside the project to find the correct entrypoint, e.g. `ls` or `git ls-files | grep -E 'app|streamlit|main'` and update the command or `STREAMLIT_APP` accordingly.
