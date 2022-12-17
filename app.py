import os, pyttsx3, PyPDF2

def pdfAudio(pdf_file:str):
    #File locations
    output_mp3_file = os.path.abspath(f"outputs\{os.path.basename(pdf_file)}.mp3")

    pdf_reader = PyPDF2.PdfFileReader(open(pdf_file, 'rb'))

    audio = pyttsx3.init()

    for page_num in range(pdf_reader.numPages):
        text = pdf_reader.getPage(page_num).extract_text()
        clean_text = text.strip().replace('\n',' ')

    audio.save_to_file(clean_text, output_mp3_file)
    audio.runAndWait()
    audio.stop()

if __name__ == "__main__":
    pdfAudio(pdf_file = os.path.abspath("pdfs\TheGameDesignerPlaybook_EBook.pdf")) #TODO be update to prompt the user to select a file
    pass