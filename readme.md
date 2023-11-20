### Development

1. Deactivate conda with command ```conda deactivate```
2. Check Python version with ```python3 --version``` (current recommended 3.12)
3. Navigate to project root directory and activate venv ```source ro-calc-env/bin/activate```
4. Run development server ```python3 manage.py runserver```
5. Navigate to (localhost) /calculator

### Deployment

Production application is hosted on Fly.io, current url: 
https://ro-calc.fly.dev/calculator

1. Ensure venv is activated ("ro-calc" in command line)
2. Run ```pip freeze > requirements.txt```
3. Run ```flyctl deploy```