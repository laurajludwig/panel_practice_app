from subprocess import Popen

def load_jupyter_server_extension(nbapp):
    """serve the PanelAppDemo.ipynb directory with bokeh server"""
    Popen(["panel", "serve", "PanelAppPractice.ipynb", "--allow-websocket-origin=*"])