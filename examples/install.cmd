python -m venv .venv
call .venv\Scripts\activate
pip install build
python -m build --outdir dist ..\
pip install dist\rapyd_sdk-1.0.9-py3-none-any.whl --force-reinstall
