from collections import defaultdict
import heapq
def groupingDishes(dishes):
    groups = defaultdict(set)
    for d in dishes:
        for x in d[1:]:
            groups[x].add(d[0])
    ans = []
    for k in sorted(groups):
        if len(groups[k]) >= 2:
            ans.append([k]+sorted(groups[k]))
    return ans


dishes = [["Salad", "Tomato", "Cucumber", "Salad", "Sauce"],
          ["Pizza", "Tomato", "Sausage", "Sauce", "Dough"],
          ["Quesadilla", "Chicken", "Cheese", "Sauce"],
          ["Sandwich", "Salad", "Bread", "Tomato", "Cheese"]]

for x in groupingDishes(dishes):
  print(x) 

