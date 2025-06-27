from nicegui import ui
import app.counter

def startup() -> None:
    app.counter.create()