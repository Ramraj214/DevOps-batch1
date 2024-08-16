from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/divide/{num1}/{num2}")
async def divide(num1: int, num2: int):
    try:
        result = num1 / num2
        return {"result": result}
    except ZeroDivisionError:
        raise HTTPException(status_code=400, detail="Cannot divide by zero")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {e}")