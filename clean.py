import pandas as pd


def clean(contact_info_file, other_info_file):
    a = pd.read_csv("respondent_contact.csv")
    b = pd.read_csv("respondent_other.csv")
    b.rename(columns={'id': 'respondent_id'}, inplace=True)
    merged = a.merge(b, on='respondent_id')
    merged = merged.dropna()
    merged = merged[merged['job'].str.contains('insurance|Insurance') == False]

    return merged


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('contact_info_file', help='The path to the respondent_contact.csv file')
    parser.add_argument('other_info_file', help='The path to the respondent_other.csv file')
    parser.add_argument('output_file', help='The path to the output file')
    args = parser.parse_args()

    cleaned = clean(args.contact_info_file, args.other_info_file)
    print(cleaned.shape)
    cleaned.to_csv(args.output_file, index=False)