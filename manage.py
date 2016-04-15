#!/usr/bin/env python
from app import create_app
from flask.ext.script import Manager
import coverage
import os

COV = None
COV = coverage.coverage(branch=True, include='app/*')
COV.start()

app = create_app("development")
manager = Manager(app)

# run unittest
@manager.command
def test(coverage=False):
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
    if COV:
        COV.stop()
        COV.save()
        print('Coverage Summary:')
        COV.report()
        basedir = os.path.abspath(os.path.dirname(__file__))
        covdir = os.path.join(basedir, 'testreport/coverage')
        COV.html_report(directory=covdir)
        print('HTML version: file://%s/index.html' % covdir)
        COV.erase()

if __name__ == '__main__':
    manager.run()
