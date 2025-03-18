# Demonstrate List Slicing 

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original List:", list)
extracted_list = list[:5]
print("Extracted first five elements:", extracted_list)
# print("Reversed extracted elements:", list[4::-1])  # -1>-10, 0->9, 1->8, 2->7, 3->6 and 4 is not included in range 
reversed_extracted_list = extracted_list[::-1]
print("Reversed extracted elements:", reversed_extracted_list)
 