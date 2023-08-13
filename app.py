import tkinter as tk
from googletrans import Translator

class LanguageTranslatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Language Translator")

        self.translator = Translator()

        self.label = tk.Label(root, text="Enter text to translate:")
        self.label.pack()

        self.input_text = tk.Text(root, height=5, width=40)
        self.input_text.pack()

        self.lang_label = tk.Label(root, text="Enter target language:")
        self.lang_label.pack()

        self.lang_entry = tk.Entry(root)
        self.lang_entry.pack()

        self.translate_button = tk.Button(root, text="Translate", command=self.translate_text)
        self.translate_button.pack()

        self.output_label = tk.Label(root, text="Translated text:")
        self.output_label.pack()

        self.output_text = tk.Text(root, height=5, width=40)
        self.output_text.pack()

    def translate_text(self):
        input_text = self.input_text.get("1.0", "end-1c")
        target_lang = self.lang_entry.get()
        
        try:
            translated = self.translator.translate(input_text, dest=target_lang)
            translated_text = translated.text
            self.output_text.delete("1.0", "end")
            self.output_text.insert("1.0", translated_text)
        except Exception as e:
            self.output_text.delete("1.0", "end")
            self.output_text.insert("1.0", f"Error: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = LanguageTranslatorApp(root)
    root.mainloop()

            

                               
