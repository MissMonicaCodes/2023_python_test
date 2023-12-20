def sort_data(origin_data):

    list_data1=list(origin_data)

    if not origin_data.isnumeric():
        print("Hi 我是阿發，請輸入數字")
        return None

    #取奇數降冪
    odd_list = [i for i in list_data1 if int(i) % 2 != 0]
    sort_odd_list_desc=sorted(odd_list,reverse=True)
    
    #取偶數升冪
    even_list = [i for i in list_data1 if int(i) % 2 == 0]
    sort_even_list_asc=sorted(even_list,reverse=False)
    
    new_list= sort_odd_list_desc + sort_even_list_asc
    numeric_string = ''.join(map(str, new_list))
    return numeric_string

if __name__ == "__main__":
    n = input('請輸入一串數字:')
    result=sort_data(n)
    print("最後輸出:",result)
