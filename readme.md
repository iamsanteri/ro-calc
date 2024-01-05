### Development

1. Deactivate conda with command ```conda deactivate```
2. Check Python version with ```python3 --version``` (current recommended 3.12)
3. Make sure to choose Conda based Python interpreter selected to resolve imports in VSCode
4. Navigate to project root directory and activate venv ```source ro-calc-env/bin/activate```
5. Run watcher for Tailwind CSS ```npm run dev```
6. Run development server ```python3 manage.py runserver```
7. Navigate to (localhost) /calculator

#### Troubleshooting

- Check Node is installed and "init" so the Tailwind CSS build process runs. 

### Deployment

Production application is hosted on Fly.io, past url has been: 
https://ro-calc.fly.dev

1. Ensure venv is activated ("ro-calc" in command line)
2. Run ```pip freeze > requirements.txt```
3. Run ```flyctl deploy```