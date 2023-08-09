import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.image import Image
from pdf2image import convert_from_path


class PDFReaderApp(App):
    def build(self):
        self.title = "PDF Reader"
        self.root = BoxLayout(orientation='vertical')

        # File chooser for selecting PDF files
        self.file_chooser = FileChooserListView()
        self.root.add_widget(self.file_chooser)

        # PDF rendering widget
        self.pdf_image = Image()
        self.root.add_widget(self.pdf_image)

        # Load Button
        self.load_button = Button(text="Load PDF")
        self.load_button.bind(on_press=self.load_pdf)
        self.root.add_widget(self.load_button)

        return self.root

    def load_pdf(self, instance):
        selected_file = self.file_chooser.selection and self.file_chooser.selection[0]  # Get the first selected file

        if selected_file:
            self.render_pdf(selected_file)
        else:
            self.pdf_image.source = ''

    def render_pdf(self, pdf_path):
        images = convert_from_path(pdf_path)
        if images:
            self.pdf_image.texture = images[0].texture


if __name__ == '__main__':
    PDFReaderApp().run()
