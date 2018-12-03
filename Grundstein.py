
# coding: utf-8

# In[41]:


import random
game = list(range(1,19))
game = game*2
random.shuffle(game)

memory = []

for i in range(0,36,6):
    memory.append(game[i:i+6])
       
print(memory)        


# In[37]:


for i in range(2):
    x1 = int(input("Bitte x1 eingeben: "))
    y1 = int(input("Bitte y1 eingeben: "))
    print(memory[x1][y1])
    x2 = int(input("Bitte x2 eingeben: "))
    y2 = int(input("Bitte y2 eingeben: "))
    print(memory[x2][y2])
    if memory[x1][y1] == memory[x2][y2]:
        print("richtig")
        memory[x1][y1] = 0
        memory[x2][y2] = 0
        print(memory)
            


# In[15]:





# In[ ]:





# In[ ]:




