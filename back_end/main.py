import os
from fastapi import FastAPI ,Depends
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from dependencies import checkToken
import uvicorn

from routers import user
from routers import item


app = FastAPI(
    # dependencies=[Depends()]
)

app.include_router(user.router)
app.include_router(item.router)




app.mount(
    "/assets",
    StaticFiles(directory="./front_end/dist/assets",html=True),
    name="static"
)

# @app.get("/{full_path:path}", response_class=HTMLResponse)
# async def serve_vue_app(full_path: str):
#     file_path = f"front_end/dist/{full_path}"
#     with open(file_path, encoding='utf-8') as f:
#         return HTMLResponse(f.read())

@app.get("/")
async def get_index():
    return FileResponse('./front_end/dist/index.html')

@app.get("/{whatever:path}")
async def get_static_files_or_404(whatever):
    # try open file for path
    file_path = os.path.join("public",whatever)
    if os.path.isfile(file_path):
        return FileResponse(file_path)
    return FileResponse('./front_end/dist/index.html')


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)