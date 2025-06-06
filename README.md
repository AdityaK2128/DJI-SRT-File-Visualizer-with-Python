# DJI-SRT-File-Visualizer-with-Python

This Python tool parses DJI drone `.SRT` metadata files to visualize:

- 📈 Altitude over time (`matplotlib`)
- 🗺️ GPS flight path on an interactive map (`folium`)

## 🚀 Features

- Works with DJI `.SRT` metadata
- Compatible with Windows, macOS, Linux
- Altitude graph and GPS map visualization
- Automatically saves map as HTML (does not open it automatically)

## 📦 Requirements

Install dependencies using:
```bash
pip install -r requirements.txt
```

## ▶️ How to Use

1. Update the `srt_file` variable in `dji_srt_visualizer.py` to your DJI `.SRT` file path.
2. Run the script:
```bash
python dji_srt_visualizer.py
```

## 📁 Output

- Altitude plot shown for 10 seconds
- HTML map saved in the same folder as the `.SRT` file
- You can open the HTML file manually in your browser

## 📂 Example Folder

```
dji-srt-visualizer/
├── dji_srt_visualizer.py
├── README.md
├── requirements.txt
└── sample_data/
    └── example.srt  # optional demo
```

## 📄 License

MIT License
