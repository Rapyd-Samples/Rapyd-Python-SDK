  
python -m venv .venv
call .venv\Scripts\activate
pip install build
python -m build --outdir dist ..\ 
pip install dist\rapydsdk-1.0.5-py3-none-any.whl --force-reinstall