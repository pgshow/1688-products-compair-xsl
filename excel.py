import xlrd


"""获取excel数据"""
def get_data():
    """整理仓库数据"""
    data = xlrd.open_workbook('1688产品总表.xlsx')

    sheet = data.sheets()[0]

    row_num = sheet.nrows  # 总行数
    col_num = sheet.ncols  # 总列数

    data_tmp = []
    for i in range(0, row_num):
        data_tmp.append(sheet.row_values(i))

    return data_tmp


"""搜索产品信息, 型号, excel 数据"""
def search_by_id(model_id, data):
    for item in data:
        if str(item[1]) == model_id:
            return item
