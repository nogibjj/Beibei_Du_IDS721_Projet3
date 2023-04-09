# Beibei_Du_IDS721_Projet3
Cloud-based Big Data Systems Project: Use a major Big Data system to perform a Data Engineering related task

## Big Idea & Plan
I am trying to see if I can replicate the work similar to this: https://huggingface.co/andite/pastel-mix
<img width="832" alt="Screen Shot 2023-02-26 at 9 17 51 PM" src="https://user-images.githubusercontent.com/60382493/221456579-79a179b7-a7a6-41b2-b629-bce7c412e576.png">

> I found out this is not too feasible and decide to preprocess dataset using Rust Language. Instead, I decide to do food image classification. Here is the reference of data: https://www.kaggle.com/datasets/dansbecker/food-101. I will pre-train the model in python and implement in Rust. However, my Macbook doesn't support pytorch and I am do it on Github Codespaces. I decided to save this idea for my final project. 

> I found another dataset about the college enrollment and decided to do analysis on this: https://www.kaggle.com/datasets/michaelbryantds/university-enrollments-dataset

## Flowchart of this project
<img width="407" alt="Screen Shot 2023-04-09 at 3 20 15 AM" src="https://user-images.githubusercontent.com/60382493/230759856-d6be282f-675a-494a-bea4-a845e14c8a24.png">


## Rust Setup
```
curl --proto '=https' --tlsv1.2 https://sh.rustup.rs -sSf | sh
source "$HOME/.cargo/env"
cargo new ids721-project3-0322
```
## Process
#### 1. Getting data from Kaggle:
- Mavigate to the dataset on Kaggle
- Download the data in a format that can be easily read by SageMaker in a CSV format
- Store the data in an S3 bucket that can be accessed by SageMaker
#### 2. Using SageMaker to do machine learning:
- Set up an instance of a Jupyter Notebook in SageMaker.
- Load the data from your S3 bucket into the notebook.
- Explore and preprocess the data as necessary.
- Train a machine learning model using SageMaker's built-in algorithms or by bringing your own algorithm.
- Evaluate the model's performance and adjust as necessary.
#### 3. Presenting your work on GitHub using LaTeX:

## Modeling Results
1. Scatterplot
<img width="567" alt="Screen Shot 2023-04-09 at 3 47 53 AM" src="https://user-images.githubusercontent.com/60382493/230760799-a78ff960-2d4c-4971-8183-f843ab59373c.png">

2. Residual Plot
<img width="603" alt="Screen Shot 2023-04-09 at 3 48 03 AM" src="https://user-images.githubusercontent.com/60382493/230760809-e54040c8-fa7d-456d-8771-362263b85459.png">


## Reference
[1]. https://www.kaggle.com/code/odednir/multiclass-food-classification-using-tensorflow

[2]. https://github.com/nogibjj/rust-mlops-template/blob/main/pytorch-rust-example/src/main.rs


[3]. https://www.kaggle.com/datasets/michaelbryantds/university-enrollments-dataset
