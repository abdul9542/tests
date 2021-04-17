def TreeConstructor(strArr):
  list={}
  item={}
  # count=0
  output="true"
  for i in (strArr):
    count = 0
    if i[3] in list.keys():
       count+=1
       item[i[3]]=item[i[3]]+1
       # print(item)
       # list[i[3]]=[list]
       # list[i[3]].append(i[1])
    else:
        item[i[3]]=1
        list[i[3]] = [i[1]]
  # code goes here
  for i in item:
      if (item[i]>2):
          output = "false"
          # print("not true")
    # print(item[i])
  return output

# keep this function call here
print(TreeConstructor(["(1,2)", "(2,4)", "(5,7)", "(7,2)", "(9,5)","(3,2)"]))