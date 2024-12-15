# Text-to-Speech Converter

A simple Python-based Text-to-Speech (TTS) application using the `gTTS` library to convert user-inputted text into speech. This tool is easy to use, supports multiple languages, and allows you to save the generated speech as an audio file.

---

## Features

- Convert text to speech in just a few steps.
- Save the output audio as an `MP3` file.
- Supports multiple languages (based on Google TTS).
- Option to choose normal or slow speech playback speed.

---

## Prerequisites

Before running the program, ensure you have the following:

1. **Python**: Version 3.6 or higher. Download it from [python.org](https://www.python.org/downloads/).
2. **Required Libraries**: Install the following Python libraries:

   ```bash
   pip install gTTS
   ```

3. **Operating System**: The `os.system` command is used to play the audio file. It is tested on Windows. Adjust commands for other operating systems (e.g., `open` for macOS or `xdg-open` for Linux).

---

## How to Use

1. Clone this repository or download the script file.
2. Open your terminal or command prompt.
3. Run the script using the following command:

   ```bash
   python text_to_speech.py
   ```

4. Follow the on-screen instructions:
   - Enter the text you want to convert to speech.
   - Specify the language code (default is `en` for English).
   - Choose whether the playback should be slow or normal.
5. The generated audio will be saved as `output.mp3` in the current directory and played automatically.

---

## Example

### Input:

- Text: `Hello, welcome to the Text-to-Speech Converter!`
- Language Code: `en`
- Speed: `no`

### Output:

- Audio saved as `output.mp3`.
- The audio will play automatically.

---

## Supported Languages

This application supports various languages. Use the corresponding language codes (e.g., `en` for English, `es` for Spanish, `fr` for French). Refer to the [Google TTS Documentation](https://cloud.google.com/text-to-speech/docs/voices) for a full list of supported languages and their codes.

---

## Known Issues

- An internet connection is required for `gTTS` to function.
- Unsupported language codes will result in an error.
- Audio playback is platform-dependent; adjust the playback command (`os.system`) if necessary.

---

## Future Enhancements

- Add a graphical user interface (GUI) using `tkinter`.
- Support batch processing for multiple text inputs.
- Implement offline TTS using libraries like `pyttsx3`.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Contributing

Contributions are welcome! If you have any suggestions or improvements, feel free to open an issue or submit a pull request.

---

## Author

**Nitin**

Feel free to connect and share your feedback!
