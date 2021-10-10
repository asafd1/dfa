import pandas

def filter_rows(df):
    return (df['Height']>150) & (df['Dye Color'] != 'O')

def tag_rows(df):
    color = df['Dye Color']
    size = df['Size']

    margins = {
        'B' : [497,86],
        'G' : [295,174],
        'R' : [295,121],
        'Y' : [497,411]
    }

    df['valid'] = False
    df['Group'] = 0

    if (size >= margins[color][0]-10 and size <= margins[color][0]+10):
        df['Group'] = margins[color][0]
        df['valid'] = True
    if (size >= margins[color][1]-10 and size <= margins[color][1]+10):
        df['Group'] = margins[color][1]
        df['valid'] = True    

    return df

def panda_file():
    df = pandas.read_csv("./dfa.csv")
    df = pandas.DataFrame(df, columns = ['Sample File Name','Dye Color','Size', 'Height', 'Area in Point'])
    print(df)
    df = df.loc[filter_rows]
    print(df)
    df = df.apply(tag_rows, axis=1).query('valid == True')
    df = df.groupby(['Sample File Name','Dye Color','Group'])
    df.sum().reset_index()[['Sample File Name','Dye Color','Group', 'Area in Point']].sort_values(by=['Sample File Name','Dye Color']).to_csv('out.csv', index=False, sep='\t')

panda_file()
