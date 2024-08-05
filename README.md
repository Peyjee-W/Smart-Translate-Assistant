**Smart Translation Assistant** is a desktop application based on OpenAI API, designed for translating text. Users can choose different translation directions and styles, and the program provides corresponding translation results. The application offers custom context menus with options like cut, copy, paste, select all, and displays keyboard shortcuts.

### Features

*   Supports multiple translation directions: English to Chinese, Chinese to English, Chinese to Japanese, Japanese to Chinese.

*   Offers multiple translation styles: Academic, Natural Expression, Formal Tone, Informal Tone.

*   Custom context menus with common operations and keyboard shortcut hints.

*   Saves translation results to text files, grouped by date.


### Project Structure

```bash
translation_app/
│
├── main.py                  # Entry file, starts the application

├── translator_app.py        # Main window and application logic

├── custom_text_edit.py      # Custom text editor components

└── utils.py                 # Utility functions (API requests, file saving)

```

### Installation

1.  Clone the project:
    
    ```bash
    git clone https://github.com/yourusername/translation_app.git

    cd translation_app
    ```
    
2.  Install dependencies:
    
    Ensure you have [Python 3.6+](https://www.python.org/downloads/) installed, then use the following command to install the required Python packages:

    
    ```复制代码

    pip install PyQt5 openai

    ```
    
3.  Configure the API:
    
    *   You can obtain a free API interface from the [free\_chatgpt\_api](https://github.com/popjane/free_chatgpt_api) project.

    *   Set the API endpoint and key in `utils.py` as `openai.api_key` and `openai.base_url
`.

### Usage

1.  Run the application:
    
    Start the application by running the following command in the terminal:

    
    ```css
    python main.py
    ```
    
2.  Application Interface:
    
    *   **Translation Direction**: Select the direction for translation.

    *   **Translation Style**: Choose the translation style.

    *   **Input Text**: Enter the text to be translated.

    *   **Translation Result**: View the translated result.

3.  Context Menu:
    
    *   Both input and output text boxes support custom context menus.

    *   The input box supports cut, copy, paste, and select all operations.

    *   The output box only supports copy and select all operations.


### File Structure and Functionality


*   `main.py`: Entry file to start the application.

*   `translator_app.py`: Contains the `TranslatorApp` main window class, handling the user interface and application logic.

*   `custom_text_edit.py`: Defines the custom text editor classes `InputTextEdit` and `OutputTextEdit`, handling context menu logic.

*   `utils.py`: Contains functions for handling OpenAI API requests (`translate_text`) and file saving (`save_translation
`).

### Notes

*   Ensure a stable internet connection for communication with the API.

*   The `Tr.ico` file provided is used to set the application icon; place it in the same directory as the project root.


### License

This project is licensed under the MIT License. For more details, see the `LICENSE` file.
