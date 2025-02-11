from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# تحميل البيانات
base_path = r'C:\Users\zico2m\Desktop\projectzico'
df = pd.read_csv(f'{base_path}/merged_data.csv')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city = request.form['city']
        date = request.form['date']
        
        # فلترة البيانات بناءً على المدينة والتاريخ
        filtered_data = df[(df['City'] == city) & (df['datetime'].str.startswith(date))]
        
        if not filtered_data.empty:
            # تصفية الأعمدة التي تحتوي على NaN فقط
            filtered_data_cleaned = filtered_data.dropna(axis=1, how='all')  # حذف الأعمدة التي تحتوي فقط على NaN
            
            # تحويل البيانات إلى قائمة لعرضها في القالب
            weather_data = filtered_data_cleaned.to_dict(orient='records')
            return render_template('index.html', weather_data=weather_data, city=city, date=date)
        else:
            return render_template('index.html', error="No data found for the given city and date.", city=city, date=date)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
