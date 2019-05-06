class Solution:
    def reorderLogFiles(self, logs):
        num_logs=[]
        word_logs=[]
        temp_list=[]
        def som_fun(e):
            return e.split(' ')[1:]
        def som_fun1(e):
            return e.split(' ')[0]
        for i in logs:
            if (i.split(' ')[1].isnumeric()):
                num_logs.append(i)
            else:
                word_logs.append(i)
        for i in range(0,len(word_logs)):
            temp_list.append(set(word_logs[i].split(" ")[1:]))
        i = 0
        while i < len(temp_list):
            j = i + 1
            while j < len(temp_list):
                if temp_list[i] == temp_list[j]:
                    del temp_list[j]
                else:
                    j += 1
            i += 1
        if(len(temp_list)) == 1:
            word_logs.sort(key = som_fun1)
        else:
            word_logs.sort(key = som_fun)
        return word_logs+num_logs

#Leetcode Solution
# def reorderLogFiles(self, logs: List[str]) -> List[str]:
#     def f(log):
#         id_, rest = log.split(" ", 1)
#         return (0, rest, id_) if rest[0].isalpha() else (1,)
#     return sorted(logs, key = f)