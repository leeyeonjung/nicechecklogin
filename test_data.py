import utilities.ExcelUtils

file_path = './/testData//data.xlsx'

data=['sign_phone','sign_kakao','merchant_biz_no','agency_biz_no']

def makeDataList(rownum1, rownum2, columnnum1, columnnum2, sheetname):
    return [[(utilities.ExcelUtils.readData(file_path,sheetname,j,i+2)) for i in range(columnnum1-1,columnnum2-1)] for j in range(rownum1,rownum2)]
    
sign_phone=makeDataList(2,5,1,4,data[0])
sign_kakao=makeDataList(2,4,1,3,data[1])
merchant_biz_no=makeDataList(2,5,1,4,data[2])
agency_biz_no=makeDataList(2,4,1,3,data[3])

# print(sign_phone)
# print(sign_kakao)
# print(merchant_biz_no)
# print(agency_biz_no)


# a=6
# try:
#     정상 구문
# except Exception as e:
#     fail 구문
#     pass