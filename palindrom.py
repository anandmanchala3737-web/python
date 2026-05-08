# def is_sorted(lst):
#     if len(lst)<=1:
#         return True
#     for i in range(len(lst)-1):
#         if lst[i] > lst[i+1]:
#             return False
#     return True

# input_list1=[1,2,3,4,5]
# input_list2=[5,4,3,2,1]
# input_list3=[1,3,2,4,5]
    
# result1=is_sorted(input_list1)
# result2=is_sorted(input_list2)
# result3=is_sorted(input_list3)
    
# print("Input list1 is sorted:",result1)
# print("Input list2 is sorted:",result2)
# print("Input list3 is sorted:",result3)

# def has_duplicate(lst):
#     unique_element=set()
#     for element in lst:
#         if element in unique_element:
#             return True
#         else:
#             unique_element.add(element)
#     return False
        
# input_list1=[1,2,3,4,5]
# input_list2=[1,2,3,4,5,5]
# input_list3=[1,2,3,3,4,5]

# result1=has_duplicate(input_list1)
# result2=has_duplicate(input_list2)
# result3=has_duplicate(input_list3)

# print("Input list1 has duplicates:",result1)
# print("Input list1 has duplicates:",result2)
# print("Input list1 has duplicates:",result3)

def remove_duplicate(lst):
    unique_element=set()
    unique_list=[]
    for element in lst:
        if element not in unique_element:
            unique_element.add(element)
            unique_list.append(element)
    return unique_list

input_list=[1,2,3,3,4,5,5,6,6,6,7,8,8,9]
unique_list=remove_duplicate(input_list)
print("Input list:",input_list)
print("unique list:",unique_list)