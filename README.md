## Requirements
- python 3.9.x
- postgresql 14.x

### 1. Create virtual environment
python3 -m venv venv

#### Activate virtual environment (Mac/Linux)
source venv/bin/activate

#### Activate virtual environment (Windows)
venv\Scripts\activate

### 2. Set up Environment Variables
Create a .env file in the root directory and add your environment variables:
<br/> you can copy the .env_sample file and rename it to .env

### 3. Install dependencies
pip install -r requirements.txt

### 4. Migrate Database
- python manage.py migrate
- python manage.py runserver

### Run tests
python manage.py test

### Api documentation using swagger
http://127.0.0.1:8000/api/docs/



