# GPT-3 generator of scientific abstracts.

## Install

```
conda create --name gpt-3-uranium
conda activate gpt-3-uranium
conda install pip
pip install -r requirements.txt
```

## Visual demo

Run the project using

```
streamlit run ui_streamlist.py --server.port 5001
```

## Run the API

```
gunicorn -b 0.0.0.0:5000 app:app --timeout 500
```

API call for topics with `curl`

```
curl -X GET -H "Content-Type: application/json" -d '{"topic":["machine learning", "finance"]}' http://IP:5000/
```

and for title

```
curl -X GET -H "Content-Type: application/json" -d '{"topic":"All you need is a Python"}' http://IP:5000/
```
#   G h o s t w r i t e r C h e c k  
 