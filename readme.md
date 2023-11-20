### Development

1. Deactivate conda with command ```conda deactivate```
2. Check Python version with ```python3 --version``` (current recommended 3.12)
3. Navigate to project root directory and activate venv ```source ro-calc-env/bin/activate```
4. Run watcher for Tailwind CSS ```npm run dev```
5. Run development server ```python3 manage.py runserver```
6. Navigate to (localhost) /calculator

#### Troubleshooting

- Check Node is installed and "init" so the Tailwind CSS build process runs. 

### Deployment

Production application is hosted on Fly.io, current url: 
https://ro-calc.fly.dev

1. Ensure venv is activated ("ro-calc" in command line)
2. Run ```pip freeze > requirements.txt```
3. Run ```flyctl deploy```