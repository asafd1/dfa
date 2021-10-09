import pandas

def tag_rows(df):
    color = df['Dye Color']
    size = df['Size']
    area = df['Area in Point']

    margins = {
        'B' : [497,86],
        'G' : [295,174],
        'R' : [295,121],
        'Y' : [497,411],
        'O' : [0,0]
    }

    df['valid'] = False
    df['Group'] = 0
    if (area < 150):
        return df
    if (color == 'O'):
        return df

    if (size >= margins[color][0]-10 and size <= margins[color][0]+10):
        df['Group'] = margins[color][0]
        df['valid'] = True
    if (size >= margins[color][1]-10 and size <= margins[color][1]+10):
        df['Group'] = margins[color][1]
        df['valid'] = True    

    return df

# def filter_and_sum(df):
#     df = df.apply(filter_by_color, axis=1).query('valid == True')
#     df = pandas.DataFrame(df, columns = ['A', 'B', 'C']).sum()
#     return df

def panda_file():
    df = pandas.read_csv("./dfa.csv")
    df = pandas.DataFrame(df, columns = ['Sample File Name','Dye Color','Group', 'Size', 'Area in Point'])
    print(df.head())
    df = df.apply(tag_rows, axis=1).query('valid == True')
    df = df.groupby(['Sample File Name','Dye Color','Group'])
    df.sum().reset_index()[['Sample File Name','Dye Color','Group', 'Area in Point']].sort_values(by=['Sample File Name','Dye Color']).to_csv('out.csv', index=False, sep='\t')
    # df.to_csv('out.csv', index=False)
    print(df)


panda_file()
