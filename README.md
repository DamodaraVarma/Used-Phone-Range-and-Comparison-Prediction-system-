Used Smartphone Price Prediction and Comparison System
📌 Project Overview

This project is a machine learning-based web application that predicts the resale price range of used smartphones and allows users to compare multiple devices. The system uses smartphone specifications such as brand, RAM, storage, camera, battery, display size, and device age to provide accurate and data-driven price estimations.

🚀 Features
🔮 Price Prediction: Predicts resale price range of used smartphones
📊 Phone Comparison: Compare two smartphones based on predicted prices
🏆 Flagship Phones Section: Displays premium smartphones with specifications
⚡ Real-Time Results: Instant predictions using trained ML model
🌐 Interactive UI: Built using Streamlit for easy user interaction
🛠️ Technologies Used
Programming Language: Python
Frontend Framework: Streamlit
Machine Learning: Scikit-learn (Random Forest Regressor)
Libraries: Pandas, NumPy, Matplotlib, Seaborn, Joblib
Dataset: CSV file (collected from Kaggle / resale platforms)
📂 Project Structure
phone_prediction/
│
├── app.py                # Main application file
├── used_phone_data.csv   # Dataset
├── model.pkl             # Saved model (optional)
├── requirements.txt      # Dependencies
└── assets/               # Images (optional)
⚙️ Installation & Setup
1. Clone the Repository
git clone https://github.com/your-username/phone-prediction.git
cd phone-prediction
2. Install Dependencies
pip install -r requirements.txt

Or manually:

pip install pandas numpy scikit-learn streamlit matplotlib seaborn joblib
▶️ Running the Application
streamlit run app.py

Then open in browser:

http://localhost:8501/
📊 How It Works
User enters smartphone specifications
Data is processed and encoded
Random Forest model predicts price
System displays price range
Users can compare two smartphones
📈 Machine Learning Model
Algorithm Used: Random Forest Regressor
Input Features:
Brand
RAM
Storage
Camera
Battery
Display
Age
Output:
Predicted resale price range
🧪 Testing
Test prediction with different inputs
Verify comparison results
Check UI responsiveness
Ensure dataset is properly loaded
🌍 Applications
Online resale platforms (OLX, Cashify)
E-commerce websites
Mobile retail stores
Price comparison tools
Consumer decision support
🔮 Future Enhancements
Real-time data integration (APIs/Web scraping)
Deep learning models for improved accuracy
Mobile app development
User authentication and personalization
Visualization dashboards
🤝 Contribution

Contributions are welcome! Feel free to fork the repository and submit pull requests.

📜 License

This project is for academic and educational purposes.

👨‍💻 Author
Your Name
Final Year Project
⭐ Acknowledgement

Special thanks to open-source libraries and datasets that made this project possible.

✅ One-Line Description

“A machine learning-based web application for predicting and comparing used smartphone resale prices in real time.”
