python -m venv .venv
. .venv/bin/activate
pip install build
python -m build --outdir dist ../
pip install dist/rapyd_sdk-1.0.6-py3-none-any.whl --force-reinstall
