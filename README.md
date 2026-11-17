# RLO File Masquerading

A small Python project exploring Unicode Right-to-Left Override (RLO, `U+202E`) and its impact on filename presentation in Windows.

## About

This project demonstrates how bidirectional Unicode control characters can manipulate the visual presentation of filenames.

It is intended for cybersecurity education, threat intelligence and security awareness.

## Features

- RLO (`U+202E`) Unicode character handling.
- Custom filename and extension parsing.
- File existence validation.
- Command-line interface using `argparse`.
- Colored terminal output using `colorama`.
- Error handling and debug mode.

## Requirements

- Python 3.8+
- colorama

Install dependencies:

```bash
pip install colorama
```

## Example

Consider a test executable:  
-# The test executable is a windows compiled version of file.c  

```text
example/
└── file.exe
```

1- Run:  
```
python main.py file.exe -n exam -e pdf
```
2- Observe the new created file in your current folder.

## Usage

```bash
python main.py file --name TARGET_NAME --extention TARGET_EXTENTION
```

## Disclaimer

This project is developed strictly for educational and cybersecurity research purposes.

RLO-based filename manipulation can be abused in phishing and malware distribution. Always inspect actual file extensions and file formats rather than trusting their visual presentation.