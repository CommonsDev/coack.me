coack.me
========
FIXIT

Instal coack.me:

    apt-get install virtualenv
    virtualenv --no-site-packages coack
    cd coack
    source bin/activate
    git clone https://github.com/UnissonCo/coack.me.git
    cd coack.me
    pip install -r requirements.txt
    python manage.py syncdb --all
    python manage.py migrate --fake
    python manage.py runserver


Translation
========

    pip install --upgrade transifex-client
    tx init
    cd services
    mkdir locale
    cd locale
    ../manage.py makemessages -l en
    tx set --auto-local -r coack.services 'services/locale/<lang>/LC_MESSAGES/django.po' \
      --execute --source-lang en --source-file services/locale/en/LC_MESSAGES/django.po
    tx push -s -t
