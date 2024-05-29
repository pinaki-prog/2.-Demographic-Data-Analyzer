import pandas as pd

def load_data():
    return pd.read_csv('adult.data.csv', header=None, names=[
        'age', 'workclass', 'fnlwgt', 'education', 'education-num', 'marital-status',
        'occupation', 'relationship', 'race', 'sex', 'capital-gain', 'capital-loss',
        'hours-per-week', 'native-country', 'salary'
    ])

def race_count(df):
    return df['race'].value_counts()

def average_age_of_men(df):
    return round(df[df['sex'] == 'Male']['age'].mean(), 1)

def percentage_bachelors(df):
    total_count = len(df)
    bachelors_count = len(df[df['education'] == 'Bachelors'])
    return round((bachelors_count / total_count) * 100, 1)

def percentage_advanced_education_more_50k(df):
    advanced_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    advanced_education_more_50k = df[advanced_education & (df['salary'] == '>50K')]
    return round((len(advanced_education_more_50k) / len(df[advanced_education])) * 100, 1)

def percentage_non_advanced_education_more_50k(df):
    non_advanced_education = ~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    non_advanced_education_more_50k = df[non_advanced_education & (df['salary'] == '>50K')]
    return round((len(non_advanced_education_more_50k) / len(df[non_advanced_education])) * 100, 1)

def min_work_hours(df):
    return df['hours-per-week'].min()

def percentage_min_hours_more_50k(df):
    min_hours = min_work_hours(df)
    min_hours_workers = df[df['hours-per-week'] == min_hours]
    min_hours_more_50k = min_hours_workers[min_hours_workers['salary'] == '>50K']
    return round((len(min_hours_more_50k) / len(min_hours_workers)) * 100, 1)

def highest_earning_country_percentage(df):
    countries = df[df['salary'] == '>50K']['native-country'].value_counts()
    total_countries = df['native-country'].value_counts()
    country_percentage = (countries / total_countries) * 100
    highest_earning_country = country_percentage.idxmax()
    highest_percentage = round(country_percentage.max(), 1)
    return highest_earning_country, highest_percentage

def top_IN_occupation(df):
    india_high_earners = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    top_occupation = india_high_earners['occupation'].value_counts().idxmax()
    return top_occupation

def calculate_demographic_data(print_data=False):
    df = load_data()
    
    # Calculations
    race_counts = race_count(df)
    average_age_men = average_age_of_men(df)
    percentage_bachelor = percentage_bachelors(df)
    percentage_adv_edu_gt_50k = percentage_advanced_education_more_50k(df)
    percentage_non_adv_edu_gt_50k = percentage_non_advanced_education_more_50k(df)
    min_hours_worked = min_work_hours(df)
    percentage_min_hours_gt_50k = percentage_min_hours_more_50k(df)
    highest_earning_country, highest_earning_country_percentage_value = highest_earning_country_percentage(df)
    top_occupation_in_india = top_IN_occupation(df)
    
    # Compile the results into a dictionary
    result = {
        'race_count': race_counts,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelor,
        'higher_education_rich': percentage_adv_edu_gt_50k,
        'lower_education_rich': percentage_non_adv_edu_gt_50k,
        'min_work_hours': min_hours_worked,
        'rich_percentage': percentage_min_hours_gt_50k,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage_value,
        'top_IN_occupation': top_occupation_in_india
    }
    
    if print_data:
        for key, value in result.items():
            print(f"{key}: {value}")

    return result

if __name__ == "__main__":
    calculate_demographic_data(print_data=True)
