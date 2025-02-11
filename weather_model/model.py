def predict_weather(city, date, data):
    # قم بتصفية البيانات الخاصة بالمدينة
    city_data = data[data['City'] == city]
    
    # إذا كانت المدينة موجودة في البيانات
    if not city_data.empty:
        # هنا يمكن استخدام نموذج التعلم الآلي أو طريقة حسابية لتنبؤ درجة الحرارة
        # على سبيل المثال، يمكننا التنبؤ بناءً على تاريخ المدينة.
        predicted_temp = city_data['Temperature'].iloc[0]  # استخدم درجة الحرارة في ذلك التاريخ
        return predicted_temp
    else:
        return "City not found"
