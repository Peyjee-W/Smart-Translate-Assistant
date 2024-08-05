# Smart-Translate-Assistant

## Project Overview

Smart-Translate-Assistant is a desktop application that provides translation functionalities, including English-to-Chinese, Chinese-to-English, and more. It supports various translation styles such as academic and colloquial expressions. The application uses a free API from the [free\_chatgpt\_api](https://github.com/popjane/free_chatgpt_api) project for text translation, and it saves translation records in text files, displaying results in a graphical user interface.

## Features

*   Supports multiple translation directions, including English-to-Chinese, Chinese-to-English, Chinese-to-Japanese, and Japanese-to-Chinese.
*   Offers translation style options, including academic style, colloquial expressions, formal tone, and informal tone.
*   Automatically saves each translation's source text and translated text into text files.
*   Custom text editor supports cut, copy, paste, and select all functionalities.
*   Displays the window at the center of the screen.
*   The program icon is `Tr.ico`.

## Installation

1.  **Clone the Repository**:
    
    ```bash
    git clone https://github.com/Peyjee-W/Smart-Translate-Assistant.git
    cd Smart-Translate-Assistant
    ```
    
2.  **Create a Virtual Environment and Install Dependencies**:
    
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```
    
3.  **Install PyQt5 and OpenAI Libraries**:
    
    ```bash
    pip install PyQt5 openai
    ```
    
4.  **Add API Key**:
    
    In the `api_utils.py` file, replace `openai.api_key` with your OpenAI API key.
    
    ```python
    import openai
    
    # Configure API request base URL and headers
    openai.base_url = "https://free.gpt.ge/v1/"
    openai.default_headers = {"x-foo": "true"}
    ```
    *   `openai.base_url`: Sets the base URL for API requests. Here, `https://free.gpt.ge/v1/` is used, which is the URL for the free API obtained from the [free\_chatgpt\_api](https://github.com/popjane/free_chatgpt_api) project.
    *   `openai.default_headers`: Configures default headers for API requests. Here, a custom header `{"x-foo": "true"}` is set. Adjust or remove this setting as needed.

## Usage

1.  **Start the Application**:
    
    ```bash
    python main.py
    ```
    
2.  **Interface Operations**:
    
    *   Select the desired translation direction from the "Select Translation Direction" dropdown.
    *   Choose the translation style from the "Select Translation Style" dropdown.
    *   Enter the text to be translated in the "Input Text" box.
    *   Click the "Translate" button to view the translation result.
    *   Translation records will be automatically saved in the `Translations` folder, named by date and time.

## File Structure

*   `main.py`: Entry point of the application.
*   `translator_app.py`: Main window and application logic.
*   `custom_text_edit.py`: Custom text editor component.
*   `api_utils.py`: Handles API requests.
*   `file_utils.py`: Handles file operations.

## Contributing

Contributions are welcome in any form, including submitting issues, suggesting features, or providing code contributions. Please follow these steps before submitting code:

1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature-branch`).
3.  Commit your changes (`git commit -am 'Add new feature'`).
4.  Push to the branch (`git push origin feature-branch`).
5.  Create a new Pull Request.

## License

This project is licensed under the MPL License.

## Contact

If you have any questions or suggestions, please contact me at peyjee@outlook.com or [GitHub Issues](https://github.com/Peyjee-W/Smart-Translate-Assistant/issues).
