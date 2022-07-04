from kivy.app import App
from kivy.clock import Clock
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from time import strftime
import random

class ClockApp(App):
    sw_started = False
    sw_seconds = 0
    
    def on_start(self):
        Clock.schedule_interval(self.update, 0)
        
    def update(self, nap):
        if self.sw_started:
            self.sw_seconds += nap

        self.root.ids.date.text = strftime("%B %d, %Y")
        self.root.ids.time.text = strftime("[b]%I[/b]:%M:%S")
        
        m, s = divmod(self.sw_seconds, 60)
        self.root.ids.stopwatch.text = ("%02d:%02d.[size=40]%02d[/size]" % (int(m), int(s), int(s * 100 % 100)))
        
    def start_stop(self):
        self.root.ids.start_stop.text = "Start" if self.sw_started else "Stop"
        self.sw_started = not self.sw_started
        
    def reset(self):
        if self.sw_started:
            self.root.ids.start_stop.text = "Start"
            
            self.sw_started = False

        self.sw_seconds = 0
        
if __name__ == "__main__":
    Window.clearcolor = get_color_from_hex(str(random.randint(000000, 999999)))
    LabelBase.register(name="Roboto", fn_regular="Roboto-Medium.ttf", fn_bold="Roboto-Bold.ttf")

    ClockApp().run()