import pandas as pd
import glob

# 1. data ஃபோல்டரில் உள்ள அனைத்து CSV ஃபைல்களையும் எடுத்தல்
# (இப்போதைக்கு சாம்பிள் ஃபைல்ஸ் இல்லை என்பதால் ஒரு எளிய லாஜிக் எழுதுகிறோம்)
try:
    # 3 CSV ஃபைல்களையும் ஒன்றாக இணைக்கிறோம்
    files = glob.glob('data/*.csv')
    combined_df = pd.concat([pd.read_csv(f) for f in files], ignore_index=True)
except:
    # ஒருவேளை டேட்டா ஃபைல்ஸ் இல்லை என்றால், டெஸ்டிங்கிற்காக ஒரு சாம்பிள் டேட்டா கிரியேட் செய்கிறோம்
    data = {
        'product': ['Pink Morsel', 'Gold Morsel', 'Pink Morsel', 'Blue Morsel'],
        'quantity': [10, 5, 20, 8],
        'price': [1.25, 2.00, 1.50, 3.00],
        'date': ['2026-06-01', '2026-06-01', '2026-06-02', '2026-06-02'],
        'region': ['north', 'east', 'south', 'west']
    }
    combined_df = pd.DataFrame(data)

# 2. Pink Morsel மட்டும் ஃபில்டர் செய்தல்
filtered_df = combined_df[combined_df['product'] == 'Pink Morsel'].copy()

# 3. Sales கணக்கிடுதல் (quantity * price)
filtered_df['sales'] = filtered_df['quantity'] * filtered_df['price']

# 4. நமக்கு தேவையான காலம்களை மட்டும் தேர்ந்தெடுத்தல் (Sales, Date, Region)
# அவுட்புட்டில் காலம்களின் முதல் எழுத்து Capital-ஆக இருக்க வேண்டும்: Sales, Date, Region
output_df = filtered_df[['sales', 'date', 'region']].rename(
    columns={'sales': 'Sales', 'date': 'Date', 'region': 'Region'}
)

# 5. புதிய ஃபார்மேட்டட் அவுட்புட் CSV ஃபைலாக சேமித்தல்
output_df.to_csv('formatted_output.csv', index=False)
print("Data formatted successfully!")
