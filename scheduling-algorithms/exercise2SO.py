import os

path = os.getcwd()
entryPath = path + "\\entry.txt"
numOfTasks = 0
tasksInfo = []
metrics = []

def getTasksInfo():
    file = open(entryPath,'r')

    for line in file:
        line2 = line.strip()
        lineList = line2.split(' ')
        tasksInfo.append(list(map(int,lineList)))
    file.close()

def createInicialQueue(alg):

    arriveTime = tasksInfo[1]
    tasksDuration = tasksInfo[2].copy()
    tasksPriority = tasksInfo[3].copy()
    queue = []
    i = 0
        
    for time in arriveTime:
        if (time == 0):
            queue.append(i)
        i+=1

    if(alg == 3):
        tasksDurCurr = [tasksDuration[elem] for elem in queue]
        mapQueueSorted = sorted(zip(tasksDurCurr, queue))
        queue = [x for y,x in mapQueueSorted]

    elif(alg == 4):
        tasksPriorityCurr = [tasksPriority[elem] for elem in queue]
        mapQueueSorted = sorted(zip(tasksPriorityCurr, queue), reverse = True)
        queue = [x for y,x in mapQueueSorted]
                
    return queue

def calculateMetrics(arriveTime, tasksDuration, endTime):
    sumExe = 0
    sumWait = 0

    for i in range(0,numOfTasks):
        sumExe += endTime[i] - arriveTime[i]
        sumWait += endTime[i] - arriveTime[i] - tasksDuration[i]

    return sumExe/numOfTasks, sumWait/numOfTasks

def fcfs(queue):
    t = 0
    tasksDuration = tasksInfo[2].copy()
    arriveTime = tasksInfo[1].copy()
    endTime = [0] * numOfTasks
    
    
    while(len(queue) != 0):
        task = queue.pop(0)
        #print("A tarefa " + str(task) + " começou a executar no tempo " + str(t))
        
        while(tasksDuration[task] != 0):
            tasksDuration[task] -= 1
            t +=1
            if (t in arriveTime):
                newTask = arriveTime.index(t)
                queue.append(newTask)
                #print("A tarefa " + str(newTask) + " chegou no tempo " + str(t))
        #print("A tarefa " + str(task) + " terminou no tempo " + str(t))
        endTime[task] = t

    fcfsMetrics = []
    avgExeT, avgWaitT = calculateMetrics(arriveTime, tasksInfo[2], endTime)
    fcfsMetrics.append(avgExeT)
    fcfsMetrics.append(avgWaitT)
    fcfsMetrics.append(numOfTasks-1)

    metrics.append(fcfsMetrics)
    
def rr (queue, quantum):
    t = 0
    numOfChanges = 0
    tasksDuration = tasksInfo[2].copy()
    arriveTime = tasksInfo[1].copy()
    endTime = [0] * numOfTasks
    
    while(len(queue) != 0):
        task = queue.pop(0)
        numOfChanges += 1
        q = quantum
        #print("A tarefa " + str(task) + " começou a executar no tempo " + str(t))
        
        while(tasksDuration[task] != 0):
            tasksDuration[task] -= 1
            q -=1
            t +=1
            if (t in arriveTime):
                newTask = arriveTime.index(t)
                queue.append(newTask)
                #print("A tarefa " + str(newTask) + " chegou no tempo " + str(t))

            if(q == 0 and tasksDuration[task] != 0):
                #print("A tarefa " + str(task) + " foi interrompida pelo quantum e" +
                #      " não tinha terminado, voltou pra fila")
                queue.append(task)
                
                break
                        
        if(tasksDuration[task] == 0):
            endTime[task] = t
            #print("A tarefa " + str(task) + " terminou no tempo " + str(t))

    rrMetrics = []
    avgExeT, avgWaitT = calculateMetrics(arriveTime, tasksInfo[2], endTime)
    rrMetrics.append(avgExeT)
    rrMetrics.append(avgWaitT)
    rrMetrics.append(numOfChanges-1)
    metrics.append(rrMetrics)
    #print(metrics)

def sjf(queue):
    t = 0
    tasksDuration = tasksInfo[2].copy()
    tasksDurationFix = tasksInfo[2].copy()
    arriveTime = tasksInfo[1].copy()
    endTime = [0] * numOfTasks
    
    
    while(len(queue) != 0):
        task = queue.pop(0)
        #print("A tarefa " + str(task) + " começou a executar no tempo " + str(t))
        
        while(tasksDuration[task] != 0):
            tasksDuration[task] -= 1
            t +=1
            if (t in arriveTime):
                newTask = arriveTime.index(t)
                queue.append(newTask)
                #print("A tarefa " + str(newTask) + " chegou no tempo " + str(t))
                tasksDurCurr = [tasksDurationFix[elem] for elem in queue]
                mapQueueSorted = sorted(zip(tasksDurCurr, queue))
                queue = [x for y,x in mapQueueSorted]
        
        #print("A tarefa " + str(task) + " terminou no tempo " + str(t))
        endTime[task] = t

    sjfMetrics = []
    avgExeT, avgWaitT = calculateMetrics(arriveTime, tasksInfo[2], endTime)
    sjfMetrics.append(avgExeT)
    sjfMetrics.append(avgWaitT)
    sjfMetrics.append(numOfTasks-1)
    metrics.append(sjfMetrics)
    #print(metrics)

def srtf(queue):
    t = 0
    numOfChanges = 0
    tasksDuration = tasksInfo[2].copy()
    tasksDurationFix = tasksInfo[2].copy()
    arriveTime = tasksInfo[1].copy()
    endTime = [0] * numOfTasks
    
    
    while(len(queue) != 0):
        task = queue.pop(0)
        numOfChanges += 1
        #print("A tarefa " + str(task) + " começou a executar no tempo " + str(t))
        
        while(tasksDuration[task] != 0):
            tasksDuration[task] -= 1
            t +=1
            if (t in arriveTime):
                newTask = arriveTime.index(t)
                queue.append(newTask)
                #print("A tarefa " + str(newTask) + " chegou no tempo " + str(t))
                tasksDurCurr = [tasksDurationFix[elem] for elem in queue]
                mapQueueSorted = sorted(zip(tasksDurCurr, queue))
                queue = [x for y,x in mapQueueSorted]

                if(queue[0] == newTask and tasksDuration[task] > tasksDuration[newTask]):
                    #print("A tarefa " + str(queue[0]) + " tem tempo de duração menor que todas " +
                    #      "inclusive a tarefa " + str(task) + " logo ela vai ser executada e a " +
                    #      "q estava sendo executada volta p fila")
                    queue.append(task)
                    tasksDurCurr = [tasksDurationFix[elem] for elem in queue]
                    mapQueueSorted = sorted(zip(tasksDurCurr, queue))
                    queue = [x for y,x in mapQueueSorted]
                    
                    break
                
        if (tasksDuration[task] == 0):
            endTime[task] = t
            #print("A tarefa " + str(task) + " terminou no tempo " + str(t))

    srtfMetrics = []
    avgExeT, avgWaitT = calculateMetrics(arriveTime, tasksInfo[2], endTime)
    srtfMetrics.append(avgExeT)
    srtfMetrics.append(avgWaitT)
    srtfMetrics.append(numOfChanges-1)
    metrics.append(srtfMetrics)
    #print(metrics)

def prioc(queue):
    t = 0
    tasksDuration = tasksInfo[2].copy()
    tasksPriority = tasksInfo[3].copy()
    arriveTime = tasksInfo[1].copy()
    endTime = [0] * numOfTasks
    
    
    while(len(queue) != 0):
        task = queue.pop(0)
        #print("A tarefa " + str(task) + " começou a executar no tempo " + str(t))
        
        while(tasksDuration[task] != 0):
            tasksDuration[task] -= 1
            t +=1
            if (t in arriveTime):
                newTask = arriveTime.index(t)
                queue.append(newTask)
                #print("A tarefa " + str(newTask) + " chegou no tempo " + str(t))
                tasksPriorityCurr = [tasksPriority[elem] for elem in queue]
                mapQueueSorted = sorted(zip(tasksPriorityCurr, queue), reverse = True)
                queue = [x for y,x in mapQueueSorted]
            
        #print("A tarefa " + str(task) + " terminou no tempo " + str(t))
        endTime[task] = t
    priocMetrics = []
    avgExeT, avgWaitT = calculateMetrics(arriveTime, tasksInfo[2], endTime)
    priocMetrics.append(avgExeT)
    priocMetrics.append(avgWaitT)
    priocMetrics.append(numOfTasks-1)
    metrics.append(priocMetrics)
    #print(metrics)

def priop(queue):
    t = 0
    numOfChanges = 0
    tasksDuration = tasksInfo[2].copy()
    tasksPriority = tasksInfo[3].copy()
    arriveTime = tasksInfo[1].copy()
    endTime = [0] * numOfTasks
    
    
    while(len(queue) != 0):
        task = queue.pop(0)
        numOfChanges += 1
        #print("A tarefa " + str(task) + " começou a executar no tempo " + str(t))
                
        while(tasksDuration[task] != 0):
            tasksDuration[task] -= 1
            t +=1
            if (t in arriveTime):
                newTask = arriveTime.index(t)
                queue.append(newTask)
                #print("A tarefa " + str(newTask) + " chegou no tempo " + str(t))
                tasksPriorityCurr = [tasksPriority[elem] for elem in queue]
                mapQueueSorted = sorted(zip(tasksPriorityCurr, queue), reverse = True)
                queue = [x for y,x in mapQueueSorted]
                
                if(queue[0] == newTask and tasksPriority[task] < tasksPriority[newTask]):
                        #print("A tarefa " + str(queue[0]) + " tem prioridade maior que todas " +
                        #  "inclusive a tarefa " + str(task) + " logo ela vai ser executada e a " +
                        #  "q estava sendo executada volta p fila")
                        queue.append(task)
                        tasksPriorityCurr = [tasksPriority[elem] for elem in queue]
                        mapQueueSorted = sorted(zip(tasksPriorityCurr, queue), reverse = True)
                        queue = [x for y,x in mapQueueSorted]
                        
                        break
                
        if (tasksDuration[task] == 0):
            endTime[task] = t
            #print("A tarefa " + str(task) + " terminou no tempo " + str(t))

    priopMetrics = []
    avgExeT, avgWaitT = calculateMetrics(arriveTime, tasksInfo[2], endTime)
    priopMetrics.append(avgExeT)
    priopMetrics.append(avgWaitT)
    priopMetrics.append(numOfChanges-1)
    metrics.append(priopMetrics)
    #print(metrics)
  
def priod(queue):
    t = 0
    numOfChanges = 0
    tasksDuration = tasksInfo[2].copy()
    tasksPriority = tasksInfo[3].copy()
    tasksPriorityCurr = tasksInfo[3].copy()
    arriveTime = tasksInfo[1].copy()
    endTime = [0] * numOfTasks
    
    
    while(len(queue) != 0):
        task = queue.pop(0)  
        numOfChanges += 1
        #print("A tarefa " + str(task) + " começou a executar no tempo " + str(t))
        tasksPriorityCurr = [x+1 for x in tasksPriorityCurr]
        tasksPriorityCurr[task] = tasksPriority[task]
        
        while(tasksDuration[task] != 0):
            tasksDuration[task] -= 1
            t +=1
            if (t in arriveTime):
                newTask = arriveTime.index(t)
                queue.append(newTask)
                #print("A tarefa " + str(newTask) + " chegou no tempo " + str(t))
                tasksPriorityCurr2 = [tasksPriorityCurr[elem] for elem in queue]
                mapQueueSorted = sorted(zip(tasksPriorityCurr2, queue), reverse = True)
                queue = [x for y,x in mapQueueSorted]
                
                if(queue[0] == newTask and tasksPriorityCurr[task] <= tasksPriorityCurr[newTask]):
                        #print("A tarefa " + str(queue[0]) + " tem prioridade maior que todas " +
                        #  "inclusive a tarefa " + str(task) + " logo ela vai ser executada e a " +
                        #  "q estava sendo executada volta p fila")
                        queue.append(task)
                        tasksPriorityCurr2 = [tasksPriorityCurr[elem] for elem in queue]
                        mapQueueSorted = sorted(zip(tasksPriorityCurr2, queue), reverse = True)
                        queue = [x for y,x in mapQueueSorted]
                        
                        break
                
        if (tasksDuration[task] == 0):
            endTime[task] = t
            #print("A tarefa " + str(task) + " terminou no tempo " + str(t))

    priodMetrics = []
    avgExeT, avgWaitT = calculateMetrics(arriveTime, tasksInfo[2], endTime)
    priodMetrics.append(avgExeT)
    priodMetrics.append(avgWaitT)
    priodMetrics.append(numOfChanges-1)
    metrics.append(priodMetrics)
    

def printMetrics():
    print("----------------- RESULTADOS ---------------------")
    print("--------------------------------------------------\n")

    print("Tempo médio de execução\n")
    print("First Come First Served(FCFS): " + str(metrics[0][0]))
    print("Round-Robin(RR): " + str(metrics[1][0]))
    print("Shortest Job First(SJF): " + str(metrics[2][0]))
    print("Shortest Remaining Time First(SRTF): " + str(metrics[3][0]))
    print("Prioridade Cooperativo(PRIOc): " + str(metrics[4][0]))
    print("Prioridade Preemptivo(PRIOp): " + str(metrics[5][0]))
    print("Prioridade Dinâmico(PRIOd): " + str(metrics[6][0]))

    print("--------------------------------------------------\n")
    
    print("Tempo médio de espera\n")
    print("First Come First Served(FCFS): " + str(metrics[0][1]))
    print("Round-Robin(RR): " + str(metrics[1][1]))
    print("Shortest Job First(SJF): " + str(metrics[2][1]))
    print("Shortest Remaining Time First(SRTF): " + str(metrics[3][1]))
    print("Prioridade Cooperativo(PRIOc): " + str(metrics[4][1]))
    print("Prioridade Preemptivo(PRIOp): " + str(metrics[5][1]))
    print("Prioridade Dinâmico(PRIOd): " + str(metrics[6][1]))

    print("--------------------------------------------------\n")
    
    print("Número de trocas de contexto\n")
    print("First Come First Served(FCFS): " + str(metrics[0][2]))
    print("Round-Robin(RR): " + str(metrics[1][2]))
    print("Shortest Job First(SJF): " + str(metrics[2][2]))
    print("Shortest Remaining Time First(SRTF): " + str(metrics[3][2]))
    print("Prioridade Cooperativo(PRIOc): " + str(metrics[4][2]))
    print("Prioridade Preemptivo(PRIOp): " + str(metrics[5][2]))
    print("Prioridade Dinâmico(PRIOd): " + str(metrics[6][2]))

    print("--------------------------------------------------")
    print("--------------------------------------------------")


getTasksInfo()
numOfTasks = tasksInfo[0][0]

fcfs(createInicialQueue(1))

rr(createInicialQueue(2), 2)

sjf(createInicialQueue(3))

srtf(createInicialQueue(3))

prioc(createInicialQueue(4))

priop(createInicialQueue(4))

priod(createInicialQueue(4))

printMetrics()



