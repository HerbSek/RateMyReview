from fastapi import FastAPI
from preprocessing import function_out

app = FastAPI()


@app.post("/")
async def output(review: str):
  my_output = function_out(review)
  return my_output

