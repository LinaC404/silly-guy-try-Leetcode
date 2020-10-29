import numpy as np
import os
import openpyxl
import pandas as pd
import re
from openpyxl import Workbook

"""
                                  _oo8oo_
                                 o8888888o
                                 88" . "88
                                 (| -_- |)
                                 0\  =  /0
                               ___/'==='\___
                             .' \\|     |// '.
                            / \\|||  :  |||// \
                           / _||||| -:- |||||_ \
                          |   | \\\  -  /// |   |
                          | \_|  ''\---/''  |_/ |
                          \  .-\__  '-'  __/-.  /
                        ___'. .'  /--.--\  '. .'___
                     ."" '<  '.___\_<|>_/___.'  >' "".
                    | | :  `- \`.:`\ _ /`:.`/ -`  : | |
                    \  \ `-.   \_ __\ /__ _/   .-` /  /
                =====`-.____`.___ \_____/ ___.`____.-`=====
                                  `=---=`


               ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

                        佛祖保佑       永无bug
"""


def all_path(dirname):
    filelistlog =  'filelistlog.txt'  # 保存文件路径
    # print(filelistlog)
    if os.path.exists(filelistlog):
        print("File filelistlog.txt existed, if you want to update,please delete!\n")
        return
    postfix = set(['md'])  # 设置要保存的文件格式
    for maindir, subdir, file_name_list in os.walk(dirname):
        # print( maindir, subdir, file_name_list)
        for filename in file_name_list:
            apath = os.path.join(maindir, filename)
            # if True:        # 保存全部文件名。若要保留指定文件格式的文件名则注释该句
            if apath.split('.')[-1] in postfix:   # 匹配后缀，只保存所选的文件格式。若要保存全部文件，则注释该句
                try:
                    # 打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
                    with open(filelistlog, 'a+') as fo:	
                        fo.writelines(apath)
                        fo.write('\n')
                except:
                    pass    # 所有异常全部忽略即可
    

def md_to_df(filepath):
    content_file = []
    md_contents = pd.read_table(filepath, skip_blank_lines=True)
    # table_head = re.findall(r"(?<=>).*?(?=<)",md_contents.iloc[0].to_string())
    # table_head = [i for i in table_head if i is not '|']
    table_head = md_contents.iloc[0].to_string().split('|')[1:-1]   # 头尾截取的值舍去
    for i in range(len(table_head)-1,-1,-1):
        if 'div' in table_head[i]:
            # print(table_head[i])
            table_head[i] = re.findall(r"(?<=>).*?(?=<)",table_head[i])[0]
        if  table_head[i] == ':-' or  table_head[i].isspace() == True:
            table_head.pop(i)

    # print(md_contents.iloc[0].to_string())
    # print(table_head)
    len_head = len(table_head)+1

    for i in range(1,md_contents.shape[0]):
        row = md_contents.iloc[i].values.tolist()[0]

        if isinstance(row,float):
            continue

        # """
        # print(type(row))
        length = 0
        for j in row:
            if j == '|':
                length = length + 1
        if length > len_head:
            # print(len_head,length)
            row_contents = row.rsplit('|',length-len_head)
            # row = row[:-(length-len_head)]
            row = row_contents[0]
            print("Index: %d" % i,row) 
        # """
        
        row = row.split('|')[1:-1]
        if row[0] == 'Comiru信息' or row[0] == '测试执行信息':
            break
        content_file.append(row)

    df = pd.DataFrame(content_file,columns=table_head)
    # print(df)
    return df

def sheet_count(name0,name1,name2,role,temp_menu,temp_submenu):
    Res = []
    for i in temp_menu:
        for j in  temp_submenu:
            cou1 = df[(df[name0] == role) & (df[name1] == i) & (df[name2] == j)]
            if cou1.shape[0] > 0:
                # print(i,j,cou1.shape[0])
                # print(cou1)
                Res.append([i,j,cou1.shape[0]])
    for p in range(len(Res)):
        Res[p].insert(0, role)
    return Res

if __name__ == "__main__":
    """
    flag_path:???
    flag: mark language. 0:Chinese; 1:Japanese
    temp_role : the role in excel file.
    temp_menu : the main menu in excel file.
    temp_submenu : the submenu in excel file
    sheet_data : new a empty dataframe (the details about the number of summenu)
    """
    count = pd.DataFrame(columns=['Filepath','Role','Numeber'])
    count_path = 'count.xlsx'
    count_writer =  pd.ExcelWriter(count_path, engine='xlsxwriter')
    
    all_path(r'E:\ComiruTestRes\test\ComiruTestTree')
    filepath = open("filelistlog.txt")
    apath = filepath.readline()[:-1]
    flag_path = 0
    while apath:
        # apath = '.\zh-Cn\PCApplaction\ComiruWeb\Staging\ComiruWeb测试白名单(校方).md'
        flag = -100
        temp_role = []
        temp_menu = []
        temp_submenu = []
        sheet_data = pd.DataFrame()
        print(apath)

        flag = apath.find('japan')
        if flag == -1:
            flag = 0
            print('匹配中文')
        else:
            flag = 1
            print('匹配日语')

        if flag == 0:
            df = md_to_df(apath)
            values = {'角色':'0','菜单': '0', '子菜单': '0'}
            df = df.fillna(value=values)
            role = df['角色'].drop_duplicates()
            menu = df['菜单'].drop_duplicates()
            submenu = df['子菜单'].drop_duplicates()
        elif flag == 1:
            df = md_to_df(apath)
            values = {'権限':'0','大項目': '0', '小項目': '0'}
            df = df.fillna(value=values)
            role = df['権限'].drop_duplicates()
            menu = df['大項目'].drop_duplicates()
            submenu = df['小項目'].drop_duplicates()

        for i, v in role.items():
            temp_role.append(v)
        for i, v in menu.items():
            temp_menu.append(v)
        for i, v in submenu.items():
            temp_submenu.append(v)

        if len(temp_role)==0 and len(temp_menu)==0 and len(temp_submenu)==0:
            """empty dataframe, pass"""
            # count = count.append([{'Filepath':apath,'Role':np.NaN,'Numeber': np.NaN}], ignore_index=True)
            apath = filepath.readline()[:-1]
            flag_path = flag_path + 1 
            continue    
        
        for i in range(len(temp_role)):
            if flag == 0:
                Res = sheet_count('角色','菜单', '子菜单',temp_role[i],temp_menu,temp_submenu)
                insert_data = pd.DataFrame(Res, columns=['角色','菜单(中)', '子菜单(中)', '数量(中)'])
                number = insert_data['数量(中)'].tolist()
            elif flag == 1:
                Res = sheet_count('権限','大項目', '小項目',temp_role[i],temp_menu,temp_submenu)
                insert_data = pd.DataFrame(Res, columns=['権限','大項目(日)', '小項目(日)', '数量(日)'])
                number = insert_data['数量(日)'].tolist()

            number = [int(j)for j in number]
            total = 0
            for j in number:
                total = total + j
            count = count.append([{'Filepath':apath,'Role':temp_role[i],'Numeber':total}], ignore_index=True)
            # print('Filepath: ',apath,'; Role: ',temp_role[i],'; Numeber: ',total)

            if flag == 0:
                total = pd.Series({'角色':'Total '+temp_role[i], '数量(中)':total})
            elif flag == 1:
                total = pd.Series({'権限':'Total '+temp_role[i], '数量(日)':total})

            insert_data = insert_data.append(total,ignore_index=True)
            sheet_data = pd.concat([sheet_data, insert_data],sort=False)

        sheet_data = sheet_data.append({'Source file':apath},ignore_index=True)
        print(sheet_data)
        print('\n')

        name_contents = apath.split('\\')
        mark = ('Zh_' if flag == 0  else 'Ja_')
        savepath = mark + name_contents[6] + '.xlsx'
        # writer =  pd.ExcelWriter(savepath, engine='openpyxl')
        # sheet_data.to_excel(writer, sheet_name = name_contents[-1].split('.')[0])

        
        if not os.path.exists(savepath):
            wb = Workbook()
            wb.save(filename = savepath)

        if sheet_data.empty:
            pass
        else:
            writer = pd.ExcelWriter(savepath,engine='openpyxl')
            book = openpyxl.load_workbook(writer.path)
            writer.book = book
            sheet_data.to_excel(writer,sheet_name = name_contents[-1].rsplit('.',1)[0],index=False)
            writer.save()
            print('Insert data successfully!')

        # exit()
        apath = filepath.readline()[:-1]
        flag_path = flag_path + 1 
    
    count.to_excel(count_writer, sheet_name = 'Count')
    count_writer.save()
