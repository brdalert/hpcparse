Set-Location .\HPCSAP_package\
python.exe setup.py sdist bdist_wheel
python.exe -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*
Set-Location ../