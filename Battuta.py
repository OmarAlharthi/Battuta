#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system(' pip install cohere')


# In[3]:


import cohere  
co = cohere.Client('t0UzEUyWPoXfohjWL7LUqyI7XiinxY3DgiWwtsJu')


# In[4]:


from cohere.responses.classify import Example


examples=[
  Example("How do I find my insurance policy?", "Finding policy details"),
  Example("How do I download a copy of my insurance policy?", "Finding policy details"),
  Example("How do I find my policy effective date?", "Finding policy details"),
  Example("When does my insurance policy end?", "Finding policy details"),
  Example("Could you please tell me the date my policy becomes effective?", "Finding policy details"),
  Example("How do I sign up for electronic filing?", "Change account settings"),
  Example("How do I change my policy?", "Change account settings"),
  Example("How do I sign up for direct deposit?", "Change account settings"),
  Example("I want direct deposit. Can you help with that?", "Change account settings"),
  Example("Could you deposit money into my account rather than mailing me a physical cheque?", "Change account settings"),
  Example("How do I file an insurance claim?", "Filing a claim and viewing status"),
  Example("How do I file a reimbursement claim?", "Filing a claim and viewing status"),
  Example("How do I check my claim status?", "Filing a claim and viewing status"),
  Example("When will my claim be reimbursed?", "Filing a claim and viewing status"),
  Example("I filed my claim 2 weeks ago but I still haven’t received a deposit for it.", "Filing a claim and viewing status"),
  Example("I want to cancel my policy immediately! This is nonsense.", "Cancelling coverage"),
  Example("Could you please help my end my insurance coverage? Thank you.",
  "Cancelling coverage"),
  Example("Your service sucks. I’m switching providers. Cancel my coverage.", "Cancelling coverage"),
  Example("Hello there! How do I cancel my coverage?", "Cancelling coverage"),
  Example("How do I delete my account?", "Cancelling coverage")
]


# In[21]:


prompt = "user for their interests and location, and then generate a personalized plan for their trip based on their preferences. Your app will also provide recommendations for hotels, restaurants, and attractions in the destination."


# In[22]:


response = co.generate(  
    model='command-nightly',  
    prompt = prompt,  
    max_tokens=200,  
    temperature=0.750)
  


# In[23]:



intro_paragraph = response.generations[0].text


# In[24]:



print(intro_paragraph)


# In[ ]:





# In[25]:


print(response.classifications)


# In[ ]:


from cohere.responses.classify import Example


examples=[
  #Example("How do I find my insurance policy?", "Finding policy details"),
  #Example("How do I download a copy of my insurance policy?", "Finding policy details"),
  #Example("How do I find my policy effective date?", "Finding policy details"),
  #Example("When does my insurance policy end?", "Finding policy details"),
  #Example("Could you please tell me the date my policy becomes effective?", "Finding policy details"),
  #Example("How do I sign up for electronic filing?", "Change account settings"),
  #Example("How do I change my policy?", "Change account settings"),
  #Example("How do I sign up for direct deposit?", "Change account settings"),
  #Example("I want direct deposit. Can you help with that?", "Change account settings"),
  "how how transform to a robot", "how to toast a backbag"
  #Example("Could you deposit money into my account rather than mailing me a physical cheque?", "Change account settings"),
  #Example("How do I file an insurance claim?", "Filing a claim and viewing status"),
  #Example("How do I file a reimbursement claim?", "Filing a claim and viewing status"),
  #Example("How do I check my claim status?", "Filing a claim and viewing status"),
  #Example("When will my claim be reimbursed?", "Filing a claim and viewing status"),
  #Example("I filed my claim 2 weeks ago but I still haven’t received a deposit for it.", "Filing a claim and viewing status"),
  #Example("I want to cancel my policy immediately! This is nonsense.", "Cancelling coverage"),
  #Example("Could you please help my end my insurance coverage? Thank you.",
  #"Cancelling coverage"),
  #Example("Your service sucks. I’m switching providers. Cancel my coverage.", "Cancelling coverage"),
  #Example("Hello there! How do I cancel my coverage?", "Cancelling coverage"),
  #Example("How do I delete my account?", "Cancelling coverage")
]


# In[ ]:


intro_paragraph = response.generations[0].text


# In[ ]:


response = co.generate(  
    model='command-nightly',  
    prompt = prompt,  
    max_tokens=200,  
    temperature=0.750)


# In[ ]:


print(intro_paragraph)


# In[26]:


print(intro_paragraph)


# In[27]:


response = co.generate(  
    model='command-nightly',  
    prompt = prompt,  
    max_tokens=200,  
    temperature=0.750)


# In[28]:


intro_paragraph = response.generations[0].text


# In[29]:


print(intro_paragraph)


# In[ ]:




