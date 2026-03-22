import pandas as pd

def clean_titanic_data(file_path):
    df = pd.read_csv(file_path)
    # Fill missing values [cite: 33]
    df['Age'] = df['Age'].fillna(df['Age'].median())
    df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])
    # Drop or transform columns [cite: 35]
    df['Has_Cabin'] = df['Cabin'].apply(lambda x: 0 if pd.isna(x) else 1)
    return df

if __name__ == "__main__":
    cleaned_df = clean_titanic_data('../data/train.csv')
    cleaned_df.to_csv('../data/train_cleaned.csv', index=False)
    print("Data cleaning script executed successfully.")