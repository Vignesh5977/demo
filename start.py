import os
import sys
import django
from django.core.management import execute_from_command_line

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'final.settings')

    django.setup()
    
    execute_from_command_line([sys.argv[0], 'migrate'])

    execute_from_command_line([sys.argv[0], 'runserver', '0.0.0.0:8000', '--noreload'])

if __name__ == "__main__":
    main()
