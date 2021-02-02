pipenv shell
pipenv install requests
PY_DIR='build/python/lib/python3.8/site-packages'
mkdir -p $PY_DIR
pipenv lock -r > requirements.txt
pip install -r requirements.txt --no-deps -t $PY_DIR
cd build
zip -r requests_layer.zip .
aws lambda publish-layer-version \
--layer-name requests \
--compatible-runtimes python3.8 \
--zip-file fileb://requests_layer.zip
