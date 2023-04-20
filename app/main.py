from fastapi import FastAPI
from fastapi.responses import JSONResponse
from utils.connect_redis import RedisConnector

app = FastAPI()

@app.get('/prime/{value}')
def get_prime(value: str):
    try:
        val = RedisConnector().get_prime(val=value)
        if val:
            return {f"prime {value}": val}
        else:
            return {"value": f"{value} not exists!!"}
    except Exception as e:
        return JSONResponse(content={'error': str(e)}, status_code=404)
