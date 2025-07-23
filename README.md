# 🖱️ AI Virtual Mouse Using Hand Tracking

This project uses **Computer Vision** and **Hand Gesture Recognition** to simulate mouse control using your webcam. Move the cursor, perform clicks, and scroll—all by just using your fingers!

---

## 📌 Features

- 👉 Move cursor with your index finger
- ✌️ Click using index + middle finger gesture
- 🖐️ Scroll with custom gestures (optional)
- 👋 Real-time hand detection using MediaPipe
- 💡 Smooth movement with interpolation

---

## 🛠️ Tech Stack

- Python 3.8+
- OpenCV
- MediaPipe
- NumPy
- AutoPy

---

## 📷 How It Works

1. Detect hand landmarks using **MediaPipe**
2. Track index and middle fingers
3. Use gestures to:
   - Move mouse
   - Click when fingers come close
4. Convert camera coordinates → screen coordinates
5. Move the system mouse with **AutoPy**

---

## 🔧 Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/yashita099/ai-virtual-mouse.git
cd ai-virtual-mouse
