import os

import gi
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk
from pydub import AudioSegment
from pydub.playback import play


class AppWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Nooooo App")

        self.button = Gtk.Button(label="Nooooo")
        self.button.connect("clicked", self.on_button_clicked)
        self.add(self.button)

        self.nooooo_audio = AudioSegment.from_mp3(os.path.abspath("assets/nooo.mp3"))

    def on_button_clicked(self, widget):
        play(self.nooooo_audio)


def main():
    app_window = AppWindow()
    app_window.connect("delete-event", Gtk.main_quit)
    app_window.show_all()
    Gtk.main()

if __name__ == '__main__':
    main()