import csv
import random

# Sabit değerler
TEAM_ID = 'ULGAN'
MODES = ['FLIGHT', 'TEST', 'CALIBRATION', 'DEBUG']
STATES = ['IDLE', 'ASCENDING', 'DESCENDING', 'LANDED', 'RECOVERED']

# CSV dosyasını oluştur
with open('telemetry_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    
    # Başlıkları yaz
    writer.writerow(['TEAM_ID', 'MODE', 'STATE', 'TEMPERATURE', 'ALTITUDE', 'PRESSURE', 'VOLTAGE'])
    
    # 100 adet rastgele veri oluştur
    for _ in range(100):
        temperature = round(random.uniform(-10.0, 40.0), 2)
        altitude = round(random.uniform(0, 1500.0), 2)
        pressure = round(random.uniform(900.0, 1050.0), 2)
        voltage = round(random.uniform(3.0, 9.0), 2)
        
        # Her bir satırı yaz
        writer.writerow([
            TEAM_ID,
            random.choice(MODES),
            random.choice(STATES),
            temperature,
            altitude,
            pressure,
            voltage
        ])

print('CSV dosyası oluşturuldu: telemetry_data.csv') 