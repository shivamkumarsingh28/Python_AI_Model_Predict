
# Python FastAPI and Uvicorn Make API For Model

FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints. It is one of the fastest Python frameworks available, as measured by independent benchmarks.

Uvicorn is a lightning-fast ASGI server implementation, using uvloop and httptools. It's ideal for building high performance asyncio services.



## Installation

move to python script folder: 

```bash
cd Python_Script
```
Installation Process: 

```bash
1. Install FastAPI: pip install fastapi 
2. Install Uvicorn: pip install uvicorn 
3. Run Uvicorn with FastAPI: uvicorn [app]:app --reload

```
FastAPI Documentation 
[Click Link](https://fastapi.tiangolo.com/)
## API Guide

Index Api - GET

```bash
  /

  -output - {"message": "Hello Python Bank Note Check Model"}
```

Welcome Api Page With User Name As You Pass In Url (Parameter) - GET

```bash
  /api/welcome/{name}

  -output - {f'Hello welcome to saeeam world - {name}'}
```

Final Api Page Take Four(Parameter) 
- variance
- skewness
- curtosis
- entropy

Output show on console.

```bash
  /api/predict/{variance, skewness, curtosis, entropy}

- output - {"predict": "Its is real note"}
- output - {"predict": "fake note"}
```

final you can test all above mention API go /docs

```bash
  /docs

```
