import threading, shutil
from pathlib import Path
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from face_backend import app as flask_app

class Root(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", padding=20, spacing=20, **kwargs)
        self.status = Label(text="Flask not running", size_hint_y=None, height=40)
        self.btn = Button(text="Start Flask Server", size_hint_y=None, height=50,
                          on_press=self.start_server)
        self.add_widget(self.status)
        self.add_widget(self.btn)

    def start_server(self, *args):
        user_dir = Path(App.get_running_app().user_data_dir)
        user_dir.mkdir(exist_ok=True)
        asset_src = Path(App.get_running_app().directory) / "assets" / "haarcascade_frontalface_default.xml"
        asset_dst = user_dir / "haarcascade_frontalface_default.xml"
        if not asset_dst.exists():
            shutil.copy(asset_src, asset_dst)
        threading.Thread(target=self._serve, daemon=True).start()
        self.status.text = "Flask running on http://127.0.0.1:5000"
        self.btn.disabled = True

    def _serve(self):
        flask_app.run(host="127.0.0.1", port=5000, debug=False, threaded=True)

class FaceApp(App):
    def build(self):
        return Root()

if __name__ == "__main__":
    FaceApp().run()
