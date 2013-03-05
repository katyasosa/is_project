is_project
==========

Installation
------------

1. Make sure you have pip, otherwise, follow the instructions
   [here] [install-pip].
2. Do the usual Django boilerplate:
   ```bash
   $ pip install -r flowers/requirements.txt
   $ cd flowers
   $ ./manage.py syncdb && ./manage.py migrate
   $ ./manage.py runserver
   ```
3. Go to [http://localhost:8000] [http://localhost:8000].

**Note**: admin site is at [/admin] [http://localhost:8000/admin].

[pip]: http://www.pip-installer.org/en/1.3.X
[install-pip]: http://www.pip-installer.org/en/1.3.X/installing.html
