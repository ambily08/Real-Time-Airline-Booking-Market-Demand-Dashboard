import pandas as pd

def process_flight_data(raw_data):
    if not raw_data:
        return pd.DataFrame()

    df = pd.DataFrame(raw_data)
    df = df[[
        'airline', 'flight', 'departure', 'arrival', 'flight_status'
    ]]

    df['airline_name'] = df['airline'].apply(lambda x: x['name'] if isinstance(x, dict) else None)
    df['flight_number'] = df['flight'].apply(lambda x: x['iata'] if isinstance(x, dict) else None)
    df['dep_airport'] = df['departure'].apply(lambda x: x.get('airport') if isinstance(x, dict) else None)
    df['arr_airport'] = df['arrival'].apply(lambda x: x.get('airport') if isinstance(x, dict) else None)
    df['status'] = df['flight_status']

    return df[['airline_name', 'flight_number', 'dep_airport', 'arr_airport', 'status']]
