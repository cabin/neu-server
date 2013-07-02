# Initial NEU site API

To set up a development and build environment, assuming [virtualenvwrapper][]
and [pip][] are installed:

    % mkvirtualenv -a $(pwd) -r requirements.txt neu
    % pip install -r dev-requirements.txt
    % alembic upgrade head
    % ./manage.py runserver


## Migrations

Data migrations are handled by [Alembic]. Use `alembic upgrade head` to ensure
your development database is up to date. After changing model definitions in
`neu/models.py`, you can ask alembic to automatically create a new revision for
you:

    % alembic revision --autogenerate -m 'Short description'

Read and edit the new revision (in `alembic/versions`), then apply the
migration as usual.


[pip]: https://pypi.python.org/pypi/pip
[virtualenvwrapper]: https://pypi.python.org/pypi/virtualenvwrapper
[Alembic]: http://alembic.readthedocs.org/en/latest/
