# File Transfer (Python)

A simple TCP file sender and receiver in Python.

---

## Features

- Send and receive files over TCP.
- Shows real-time progress in terminal.
- Automatic file renaming if file already exists.

---

## Usage

**Important:** You must run the sender first before starting the receiver.

### Sender

```
python main.py sender <filename>
```

Example:

```
python main.py sender myfile.txt
```

### Receiver

```
python main.py receiver [host] [port]
```

Example:

```
python main.py receiver 127.0.0.1 8000
```

---

## Notes

- Receiver automatically renames file if a file with the same name exists.
- Shows progress in percentage and file size format.

---

## License

This project is licensed under the MIT License.
