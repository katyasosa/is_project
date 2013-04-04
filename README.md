is_project
==========

Installation
------------
- Install Python 2.7
- Make sure you have pip(python package manager),
  otherwise, follow the instructions [here] [install-pip].
- Install virtualenv(virtual environment tool,
  against works on my machine illness).
- git clone https://github.com/katyasosa/is_project.git
- Do the usual Django boilerplate:
   ```bash
   $ virtualenv .
   $ source bin/activate
   $ pip install -r requirements.txt
   $ ./manage.py syncdb && ./manage.py migrate
   $ ./manage.py runserver
   ```

   **Note** source Scripts/activate on Windows; pillow installation on windows
   can be painful.
- Go to [http://localhost:8000](http://localhost:8000).

**Note**: admin site is at [/admin](http://localhost:8000/admin).

[pip]: http://www.pip-installer.org/en/1.3.X
[install-pip]: http://www.pip-installer.org/en/1.3.X/installing.html
