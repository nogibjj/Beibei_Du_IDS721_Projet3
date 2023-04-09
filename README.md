# Beibei_Du_IDS721_Projet3
Cloud-based Big Data Systems Project: Use a major Big Data system to perform a Data Engineering related task

## Big Idea & Plan
I am trying to see if I can replicate the work similar to this: https://huggingface.co/andite/pastel-mix
<img width="832" alt="Screen Shot 2023-02-26 at 9 17 51 PM" src="https://user-images.githubusercontent.com/60382493/221456579-79a179b7-a7a6-41b2-b629-bce7c412e576.png">

> I found out this is not too feasible and decide to preprocess dataset using Rust Language. Instead, I decide to do food image classification. Here is the reference of data: https://www.kaggle.com/datasets/dansbecker/food-101. I will pre-train the model in python and implement in Rust. However, my Macbook doesn't support pytorch and I am do it on Github Codespaces. I decided to save this idea for my final project. 

> I found another dataset about the college enrollment and decided to do analysis on this: https://www.kaggle.com/datasets/michaelbryantds/university-enrollments-dataset

## Rust Setup
```
curl --proto '=https' --tlsv1.2 https://sh.rustup.rs -sSf | sh
source "$HOME/.cargo/env"
cargo new ids721-project3-0322
```

## Reference
[1]. https://www.kaggle.com/code/odednir/multiclass-food-classification-using-tensorflow

[2]. https://github.com/nogibjj/rust-mlops-template/blob/main/pytorch-rust-example/src/main.rs


[3]. https://www.kaggle.com/datasets/michaelbryantds/university-enrollments-dataset
