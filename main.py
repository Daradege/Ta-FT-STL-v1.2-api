from fastapi import FastAPI

# Initialize the FastAPI app
app = FastAPI()

# Define a route for the API
@app.get("/")
def index():
    return {"result":"hello from darg"}

# Define a route for a JSON endpoint
@app.get("/api/data")
def get_data():
    data = {
        "message": "This is a JSON response",
        "status": "success"
    }
    return data

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8888)
