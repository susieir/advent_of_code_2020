import pandas as pd

with open('day2', "r") as fp:
    inputs = [str(x) for x in fp.read().splitlines()]

item = inputs[0]

column_names = ['password', 'character', 'lower_b', 'upper_b']  # Set up column names
df = pd.DataFrame(columns=column_names)  # Set up empty dataframe
df['password'] = item[item.find(":") + 1:].strip()  # Extracts all characters to right of ':' and removes spaces
df['character'] = item[item.find(':') - 1: item.find(':')]  # Extracts the single character before the ':'
df['lower_b'] = int(item[: item.find('-')])  # Extracts the number before the '-'
df['upper_b'] = int(item[item.find('-') + 1: item.find(':') - 1])  # Extracts  number between the '-' and character



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(item)
    print(df['password'])
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
