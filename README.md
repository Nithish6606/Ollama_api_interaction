# Ollama API
> Creating venv
```shell
python -m venv .venv
source .venv/bin/activate
```
> Add .env with:
```shell
API_KEY="secretkey"
```
> Install requirements
```
pip install -m requiremnts.txt
```

>Start
```shell
uvicorn main:app --reload
```
>Testing
```shell
pyhton test-api.py
```
