### Development

1. Deactivate conda with command ```conda deactivate```
2. Check python version (current 3.12) with ```python3 --version```
3. Navigate to project root directory and activate venv ```source ro-calc-env/bin/activate```
4. Run development server ```python3 manage.py runserver```

### Deployment

1. Ensure venv is activated
2. Run ```pip freeze > requirements.txt```
3. Run ``` flyctl deploy```