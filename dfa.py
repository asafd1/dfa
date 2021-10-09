import pandas

def filter_by_color(df):
    color = df['Dye Color']
    size = df['Size']

    margins = {
        'B' : 1,
        'Y' : 3,
        'R' : 2
    }

    df['valid'] = size > margins[color]
    return df

def filter_and_sum(df):
    df = df.apply(filter_by_color, axis=1).query('valid == True')
    df = pandas.DataFrame(df, columns = ['A', 'B', 'C']).sum()
    return df

def panda_file():
    dfa = pandas.read_csv("./a.csv")
    r = dfa.groupby(["Sample File Name","Dye Color"]).apply(filter_and_sum)
    print(r)


panda_file()
