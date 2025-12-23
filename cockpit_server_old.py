from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.wsgi import WSGIMiddleware
from fastapi.responses import FileResponse
from gradio.routes import mount_gradio_app

# Import your organs
from spaces.cyber_arena_app.app import demo as cyber_app
from spaces.heatmap_app.app import demo as heatmap_app
from spaces.raster_app.app import demo as raster_app
from spaces.fuzz_generator_app.app import demo as fuzz_app
from spaces.token_visualizer_app.app import demo as token_app
from spaces.model_card_app.app import demo as modelcard_app

# Flask robotics organ (if you have one)
from robotics_arena_app import flask_app

app = FastAPI()

# Mount cockpit static files
app.mount("/", StaticFiles(directory="cockpit", html=True), name="cockpit")

# Mount Gradio organs
mount_gradio_app(app, cyber_app, path="/cyber")
mount_gradio_app(app, heatmap_app, path="/heatmap")
mount_gradio_app(app, raster_app, path="/raster")
mount_gradio_app(app, fuzz_app, path="/fuzz")
mount_gradio_app(app, token_app, path="/tokens")
mount_gradio_app(app, modelcard_app, path="/modelcard")

# Mount Flask organ
app.mount("/robotics", WSGIMiddleware(flask_app))