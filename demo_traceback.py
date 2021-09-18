import sys
import traceback

dict_a = {0:'hello', 1:'hi'}

def run():
   try:
       print ("Hello, this is demo.\n")
       print (dict_a[2])
       print ("End")
   except Exception as err:
       err_type = err.__class__.__name__ # 取得錯誤的class 名稱
       info = err.args[0] # 取得詳細內容
       detains = traceback.format_exc() # 取得完整的tracestack
       n1, n2, n3 = sys.exc_info() #取得Call Stack
       lastCallStack =  traceback.extract_tb(n3)[-1] # 取得Call Stack 最近一筆的內容
       fn = lastCallStack [0] # 取得發生事件的檔名
       lineNum = lastCallStack[1] # 取得發生事件的行數
       funcName = lastCallStack[2] # 取得發生事件的函數名稱
       errMesg = f"FileName: {fn}, lineNum: {lineNum}, Fun: {funcName}, reason: {info}, trace:\n {traceback.format_exc()}"
       print(errMesg)

run()
