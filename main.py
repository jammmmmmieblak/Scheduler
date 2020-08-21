import wx
list = []

class elem:
    def __init__(self, _priority, _description, _order):
        self.priority = _priority
        self.description = _description
        self.order = _order
    

#app = wx.App(False)
#frame = wx.Frame(None, wx.ID_ANY, "Scheduler")
#frame.Show(True)
#app.MainLoop()

def new_task():
    description = input("Task: ")
    priority = int(input("Priority: "))
    i = 0
    while(priority <= list[i].priority):
        i = i + 1
    new_task = elem(priority, description, i)
    list.insert(new_task.order, new_task)
    for elem in list:
        print(elem.description)
new_elem = elem(0, "", 0)
list.append(new_elem)

new_task()
new_task()
new_task()

for elem in list:
    print(elem.description)
