Introduction) Grammar! I.e. "The goal of this lab were ...".
Q1) * 'exercise', not 'exersie'.
Q2 a) The requested threshold was an accuracy of >95 %. Clarify that this is what you have reached in order to pass the exercise. (Fix the spelling mistake as well.)
Q3 a) Provide the average value for each network in order to pass the exercise. It should not be expected of the reader to check your claim.
For Q3 b) Can you see why a single node, as you found in a) should be the preferred choice?
Q3 b) Clarify what you mean by "the number of features used for the classification data"? The data points have three features each, two coordinates and a class label.
Q4)Explain why you prefer a higher correlation to a lower MSE. It is not obvious why you think that 10 nodes perform worse.
Q5 b) Well, since you did not choose 10 nodes in Q4, please explain why you now claim that 0.45 and 0.51 is "about the same". It could be argued that L2 increased the performance but then you could have picked 10 nodes in Q4 if MSE is the important performance measure.
Q6 a)Provide the requested validation performance in order to pass the exercise.
Torbjörn Lundberg , Jan 3 at 6:50pm
Q6 b) What is "this"?
Q8) Attempt to provide criteria on how to select the best model in this situation and rewrite the sentences to be grammatically correct in order to complete the exercise.
Torbjörn Lundberg , Jan 3 at 6:53pm
Q9 b) In your second sentence, what do you mean by "... made it worse"? What is 'it'?
Summary) Check grammar and spelling not only in this section but throughout the report in order to pass the exercise. Incomplete sentence structure to this extent makes it difficult to evaluate your understanding.



# The report!

### Name
Joel Bäcker (jo4383ba-s)

### Introduction
During this lab, the goal was to experiment with different hyperparameters in an MLP. The MLP is supposed to solve both classification and regression problems as well as perform model selection to optimize validation performance.

### Answers to questions
1. During the first exercise I got

| Run nr | Validation result|
| :----- | :--------------- |
| 1      | 0.8770           |
| 2      | 0.8690           |
| 3      | 0.8740           |
| 4      | 0.8780           |
| 5      | 0.8710           |
| avg    | 0.8738           |

2.

a) To reach a accuracy of more than 95% the following system was used:

```
'n_nod': [6]
'lr_rate' = 0.1

epochs = 400
bs = 28
```

b) The performance on the validation data set is

| Run nr | Validation result|
| :----- | :--------------  |
| 1      | 0.8320           |
| 2      | 0.8410           |
| 3      | 0.8370           |
| 4      | 0.8200           |
| avg    | 0.8325           |


3. Using the unchanged settings, i.e. same as in 1.

a) Best seems to be 1.

| Hidden nodes | Validation result (average of 5 runs)|
| :----- | :--------------- |
| 1      | 0.8742     |
| 2      | 0.8272     |
| 3      | 0.8368     |
| 4      | 0.8430     |
| 5      | 0.8390     |
| 6      | 0.8240     |
| 7      | 0.8180     |
| 8      | 0.8234     |
| 9      | 0.8216     |
| 10     | 0.8044     |
| 15     | 0.8036     |
| 20     | 0.8130     |
| 25     | 0.8222     |
| 30     | 0.8160     |
| 35     | 0.8102     |

b) The number of nodes in the hidden layer that seems to be the optimal for this exercise is 1. One cause of this is because the data set consists of two overlapping gaussian distributions which means that the boundary between the two is random. When more than 1 node is used the network start to become more and more overstrained and thus worse performance on validation data.

4. The average of 5 runs where new data was generated each iteration is seen in the table below. The best seems to be to use 10 hidden nodes.

| Hidden nodes | Average MSE     | Average corr   |
| :----------- | :-------------- | :------------- |
| 1            | 0.614257 | 0.678314 |
| 2            | 0.569219 | 0.709715 |
| 3            | 0.512025 | 0.739404 |
| 4            | 0.573919 | 0.704057 |
| 5            | 0.512680 | 0.747074 |
| 7            | 0.512990 | 0.741866 |
| 8            | 0.498558 | 0.760870 |
| 9            | 0.543918 | 0.738423 |
| 10           | 0.450265 | 0.779414 |
| 11           | 0.590104 | 0.705842 |
| 12           | 0.521836 | 0.751485 |
| 13           | 0.612119 | 0.710265 |
| 14           | 0.614734 | 0.703953 |
| 15           | 0.632821 | 0.707055 |


5.

a) I used 25 hidden nodes and found that lambda = 0.03 gave a result of 0.45 (MSE) on the validation.

b) The result is about the same as in Q4.

6.

a) Number of hidden nodes were 25 and the best drop out were 0.2. The performance on validation was 0.5219 (MSE).

b) The performance did not become better in regards to Q4/Q5, the opposite happened. If the network had been better than those before, a lower MSE score would be yielded.

7. The optimal model was the one below, it gave a result of about 0.89.

```
'inp_dim': x_trn.shape[1]         
'n_nod': [7]      
'drop_nod': 0.0                
'act_fun': 'tanh'             
'out_act_fun': 'softmax'
'opt_method': 'Adam'      
'cost_fun': 'mse'         
'lr_rate': 0.05
'metric': 'mse'              
'lambd' : 0.001
'num_out' : 9   

epochs = 500,     
batch_size=100,   
```

8. The phenomenon occur because the error is some sort of distance measurement. This implies that the distance can increase away from the correct classification and be falsely classified, i.e. the accuracy do not change but the error does.

If we have this situation I would opt to use early stopping when loss start to increase and validation stays constant. Early stopping allows us to cease the training when the loss have reached a minimum and is increasing again.

9.

a) The optimal MLP were the following. The performance were 0.65.

```
'n_nod': [9, 8, 2, 8, 9]                 
'drop_nod': 0.0          
'act_fun': 'tanh'             
'out_act_fun': 'softmax'
'opt_method': 'Adam'      
'cost_fun': 'mse'         
'lr_rate': 0.02
'metric': 'mse'              
'lambd' : 0.001
'num_out' : 3  

epochs = 600,
batch_size = 70
```

b) The relevant measures to select when finding the optimal model for this problem is accuracy for all the classes as well as the accuracy for the individual classes. By keeping track of them it will be easier to see which changed hyperparameters that made the model's performance better/worse, and in turn keep parameters accordingly.

10. The model used to get a MLP close zero classification error with as small as possible model is the following:

```
'n_nod': [50, 20, 15, 1, 15, 20, 50]
'drop_nod': 0.01
'act_fun': 'tanh',                 
'out_act_fun': 'sigmoid',          
'opt_method': 'Adam',             
'cost_fun': 'mse',
'lr_rate': 0.01,                 
'num_out' : 1

epochs = 2500,                
batch_size=100,
```

Which yielded (same as above):

```
 ########## STATISTICS for Training Data ##########

Accuracy        1.0000
Sensitivity     1.0000
Specificity     1.0000
Loss            0.0001

 ##################################################
```

### Summary
During this lab different methods of finding the optimal model were used. Many of them were based on trial and error, meaning that you change a variable and then seeing if the result became better or worse.

I also had to consider not to overtrain the model so that the model did not train on the notice of the data set.

In the lab data sets with more than two classes were handled, such as the Japanese vowels. This problem required a certain activation and optimization function.
