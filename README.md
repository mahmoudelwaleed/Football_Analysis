# ⚽ Football Player Tracking & Analysis Using YOLOv5  

A computer vision-based football match analysis tool that detects and tracks players, referees, and the ball using **YOLOv5**. The system classifies players by team, measures movement and speed, and analyzes ball possession from **pre-recorded match videos**.  

> 📌 **Inspired by**: [AI Sports Analytics - Football Player & Ball Tracking](https://www.youtube.com/watch?v=neBZ6huolkg&list=WL&index=52)  

---

## 🚀 Features  

✔ **Player & Ball Detection** – Detects players, referees, and the ball using **fine-tuned YOLOv5**.  
✔ **Team Classification** – Uses **K-means clustering** to classify players based on jersey colors (pixel-based).  
✔ **Tracking & Motion Analysis** – Utilizes **ByteTrack** for multi-object tracking.  
✔ **Ball Possession Estimation** – Determines possession based on **player proximity to the ball**.  
✔ **Speed & Distance Measurement** – Calculates movement in **absolute meters** using perspective transformation.  
✔ **Optical Flow & Perspective Calibration** – Ensures **accurate tracking and position mapping**.  

---

## 📊 How It Works  

1️⃣ **Object Detection**: YOLOv5 detects players, referees, and the ball.  
2️⃣ **Team Classification**: K-means clustering assigns players to teams based on jersey colors.  
3️⃣ **Tracking**: ByteTrack maintains identity consistency over frames.  
4️⃣ **Motion & Distance Analysis**: Measures player speed and movement in meters.  
5️⃣ **Ball Possession**: Determines which team controls the ball using proximity tracking.  

---

## 🛠 Technical Details  

- **Model**: YOLOv5 (fine-tuned for football tracking)  
- **Tracking Algorithm**: ByteTrack  
- **Team Classification**: K-means clustering on jersey colors  
- **Distance Measurement**: Absolute (meters) using perspective transformation  
- **Input**: Pre-recorded football match videos  

---

## 🔧 Installation  

1️⃣ **Clone the repository**  
```bash
git clone https://github.com/mahmoudelwaleed/Football_Analysis.git
cd Football_Analysis
