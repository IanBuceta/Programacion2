try:
    print(2/0)
except Exception as ex:
    errorMsg = "Error: {}"
    print(errorMsg.format(ex))
    