#!/usr/bin/env python
# coding: utf-8

# In[16]:


import pythoncom, time, win32api
from win32com.taskscheduler import taskscheduler
# Meridiem=AM/PM
def schedule(schedule_type,Day,Hour,Minute,Meridiem):
    if(Meridiem=='AM'):
        if(Hour=='12'):
            Hour='0'
    else:
        if(Hour=='12'):
            Hour='12'
        else:
            Hour=str(int(Hour)+int(12))
    test_task_name='dtoxd.job'
    ts=pythoncom.CoCreateInstance(taskscheduler.CLSID_CTaskScheduler,None,
                              pythoncom.CLSCTX_INPROC_SERVER,taskscheduler.IID_ITaskScheduler)
    tasks=ts.Enum()
    if test_task_name in tasks:
        ts.Delete(test_task_name)
    new_task=pythoncom.CoCreateInstance(taskscheduler.CLSID_CTask,None,
                              pythoncom.CLSCTX_INPROC_SERVER,taskscheduler.IID_ITask)
    ts.AddWorkItem(test_task_name,new_task)  ## task object is modified in place
    new_task.SetFlags(taskscheduler.TASK_FLAG_INTERACTIVE|taskscheduler.TASK_FLAG_RUN_ONLY_IF_LOGGED_ON)
    new_task.SetIdleWait(1,10000)
    new_task.SetComment('DTOXD Automatic Trigger')
    new_task.SetApplicationName('C:\\Program Files\\Sublime Text 3\\sublime_text.exe')
    new_task.SetPriority(taskscheduler.REALTIME_PRIORITY_CLASS)
    new_task.SetCreator('dtoxd')
    new_task.SetAccountInformation(win32api.GetUserName(),None)
    tr_ind, tr=new_task.CreateTrigger()
    tt=tr.GetTrigger()
    
    if(schedule_type=='Daily'):
        tt.TriggerType=taskscheduler.TASK_TIME_TRIGGER_DAILY
        tt.Flags=taskscheduler.HIGH_PRIORITY_CLASS
        tt.StartMinute=int(Minute)
        tt.StartHour=int(Hour)
        
    if(schedule_type=='Weekly'):
        if(Day=='Sunday'):
            tt.TriggerType=taskscheduler.TASK_TIME_TRIGGER_WEEKLY
            tt.Flags=taskscheduler.HIGH_PRIORITY_CLASS
            tt.Weekly_DaysOfTheWeek=int(1)
        if(Day=='Monday'):
            tt.TriggerType=taskscheduler.TASK_TIME_TRIGGER_WEEKLY
            tt.Flags=taskscheduler.HIGH_PRIORITY_CLASS
            tt.Weekly_DaysOfTheWeek=int(2)
        if(Day=='Tuesday'):
            tt.TriggerType=taskscheduler.TASK_TIME_TRIGGER_WEEKLY
            tt.Flags=taskscheduler.HIGH_PRIORITY_CLASS
            tt.Weekly_DaysOfTheWeek=int(4)
        if(Day=='Wednesday'):
            tt.TriggerType=taskscheduler.TASK_TIME_TRIGGER_WEEKLY
            tt.Flags=taskscheduler.HIGH_PRIORITY_CLASS
            tt.Weekly_DaysOfTheWeek=int(8)
        if(Day=='Thursday'):
            tt.TriggerType=taskscheduler.TASK_TIME_TRIGGER_WEEKLY
            tt.Flags=taskscheduler.HIGH_PRIORITY_CLASS
            tt.Weekly_DaysOfTheWeek=int(16)
        if(Day=='Friday'):
            tt.TriggerType=taskscheduler.TASK_TIME_TRIGGER_WEEKLY
            tt.Flags=taskscheduler.HIGH_PRIORITY_CLASS
            tt.Weekly_DaysOfTheWeek=int(32)
        if(Day=='Saturday'):
            tt.TriggerType=taskscheduler.TASK_TIME_TRIGGER_WEEKLY
            tt.Flags=taskscheduler.HIGH_PRIORITY_CLASS
            tt.Weekly_DaysOfTheWeek=int(64)
        tt.StartMinute=int(Minute)
        tt.StartHour=int(Hour)
        
    if(schedule_type=='Monthly'):
        if(Day=='First_day'):
            tt.TriggerType=taskscheduler.TASK_TIME_TRIGGER_MONTHLYDATE
            tt.Flags=taskscheduler.HIGH_PRIORITY_CLASS
            tt.MonthlyDate_Days=int(1)
        if(Day=='Fifteenth_day'):
            tt.TriggerType=taskscheduler.TASK_TIME_TRIGGER_MONTHLYDATE
            tt.Flags=taskscheduler.HIGH_PRIORITY_CLASS
            tt.MonthlyDate_Days=int(16384)

        if(Day=='Last_day'):
            tt.TriggerType=taskscheduler.TASK_TIME_TRIGGER_MONTHLYDATE
            tt.Flags=taskscheduler.HIGH_PRIORITY_CLASS
            tt.MonthlyDate_Days=int(1073741824)
        tt.MonthlyDate_Months=int(4095)
        tt.StartMinute=int(Minute)
        tt.StartHour=int(Hour)
    tr.SetTrigger(tt)
#     print(new_task.GetTriggerString(tr_ind))
    pf=new_task.QueryInterface(pythoncom.IID_IPersistFile)
    pf.Save(None,1)
            
            
        


# In[17]:


schedule('Monthly','First_day','11','48','AM')


# In[ ]:




