# Query PDF using AI

This Python project allows users to extract text from a PDF and query an AI model using the extracted content. It utilizes `pdfminer.six` for text extraction and an AI API for generating responses.

## Features
- Extracts text from a given PDF file
- Queries an AI model with user-provided questions
- Uses extracted text to generate relevant responses
- Ensures responses are based strictly on provided content

## Technologies Used
- Python
- `requests` (for API calls)
- `json` (for data formatting)
- `pdfminer.six` (for extracting text from PDFs)

## Setup & Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/query-pdf-using-ai.git
   cd query-pdf-using-ai
   ```
2. Install dependencies:
   ```sh
   pip install requests pdfminer.six
   ```
3. Set up your API key (replace with your actual key in the script):
   ```python
   "Authorization": "Bearer YOUR_API_KEY"
   ```

## Usage
1. Run the script:
   ```sh
   python main.py
   ```
2. Enter your question when prompted.
3. The script extracts text from `ainsmq.pdf` and queries the AI model.
4. The AI responds based on the extracted content.

## Example
```
type your question: What is artificial intelligence?
AI Response: Artificial intelligence is defined as...
```

## Contributing
Feel free to contribute by submitting pull requests or reporting issues.

## License
This project is open-source under the MIT License.

