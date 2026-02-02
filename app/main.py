from fastapi import FastAPI, UploadFile, File, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pathlib import Path
import shutil

from parsing.parser import parse_file
from extraction.skill_extractor import extract_skills
from recommendation.recommender import recommend_roles


# -------------------- App Initialization --------------------
app = FastAPI()

BASE_DIR = Path(__file__).resolve().parent.parent

UPLOAD_DIR = BASE_DIR / "data" / "uploads"
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

templates = Jinja2Templates(directory=BASE_DIR / "app" / "templates")

app.mount(
    "/static",
    StaticFiles(directory=BASE_DIR / "app" / "static"),
    name="static"
)


# -------------------- Routes --------------------

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )


@app.post("/upload", response_class=HTMLResponse)
async def upload_resume(
    request: Request,
    resume: UploadFile = File(...)
):
    file_path = UPLOAD_DIR / resume.filename

    # Save uploaded resume temporarily
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(resume.file, buffer)

    # -------- Core Resume Analysis Pipeline --------
    text = parse_file(str(file_path))
    skills = extract_skills(text)
    recommendations = recommend_roles(skills)

    # Delete resume after processing (privacy-safe)
    file_path.unlink(missing_ok=True)

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "results": recommendations
        }
    )
