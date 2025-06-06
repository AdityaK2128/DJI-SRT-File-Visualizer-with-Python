import re
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import folium
import os

# input your srt file here 
srt_file = '/Users/adityakumar/Downloads/Lucknow Air3S/JaneshwarPark/DJI_20250605180438_0056_D.SRT'  # Update for your system

# output HTML map path ---
srt_folder = os.path.dirname(srt_file)
html_filename = os.path.splitext(os.path.basename(srt_file))[0] + '_GPS_Map.html'
output_map = os.path.join(srt_folder, html_filename)

# --- Parse SRT ---
timestamps, latitudes, longitudes, altitudes = [], [], [], []
with open(srt_file, 'r') as f:
    lines = f.readlines()

for i in range(len(lines)):
    line = lines[i].strip()
    if re.match(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{3}', line):
        try:
            timestamps.append(datetime.strptime(line, "%Y-%m-%d %H:%M:%S.%f"))
            meta_line = lines[i + 1].strip()
            lat = float(re.search(r'\[latitude:\s*([0-9\.\-]+)\]', meta_line).group(1))
            lon = float(re.search(r'\[longitude:\s*([0-9\.\-]+)\]', meta_line).group(1))
            alt = float(re.search(r'\[rel_alt:\s*([0-9\.\-]+)', meta_line).group(1))
            latitudes.append(lat)
            longitudes.append(lon)
            altitudes.append(alt)
        except:
            continue

# --- Create DataFrame ---
df = pd.DataFrame({
    'Time': timestamps,
    'Latitude': latitudes,
    'Longitude': longitudes,
    'Altitude (m)': altitudes
})
df.dropna(inplace=True)

# --- Plot Altitude Over Time ---
plt.ion()
plt.figure(figsize=(12, 6))
plt.plot(df['Time'], df['Altitude (m)'], color='blue', marker='o', linewidth=1)
plt.title("Drone Altitude Over Time")
plt.xlabel("Timestamp")
plt.ylabel("Altitude (m)")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()
plt.pause(10)
plt.ioff()

# --- Create Folium Map ---
start_coords = [df['Latitude'].iloc[0], df['Longitude'].iloc[0]]
m = folium.Map(location=start_coords, zoom_start=16)

coords = list(zip(df['Latitude'], df['Longitude']))
folium.PolyLine(locations=coords, color='blue', weight=3).add_to(m)
folium.Marker(coords[0], tooltip="Start", icon=folium.Icon(color='green')).add_to(m)
folium.Marker(coords[-1], tooltip="End", icon=folium.Icon(color='red')).add_to(m)

# --- Save Map (No Auto Open) ---
try:
    m.save(output_map)
    print("\n✅ Altitude graph completed.")
    print("✅ GPS map has been saved as an HTML file.")
    print(f"📂 You can open this file after closing the plot window:\n{output_map}")
except Exception as e:
    print("❌ Error saving map:", e)
