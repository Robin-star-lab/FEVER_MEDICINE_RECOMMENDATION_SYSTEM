# Fever Medicine Recommendation System

This system provides recommendations for fever medicine, suggesting either paracetamol or ibuprofen, based on relevant health factors. 

The system is trained on a dataset containing these recommendation factors. Data preprocessing steps were implemented to address common issues, including:

* **Missing values:** Appropriate imputation or removal techniques were used.
* **Class imbalance:** Techniques such as oversampling or undersampling were applied to ensure balanced representation of both medicine types.

The developed model demonstrates strong performance on the test set, indicating no signs of overfitting. All training parameters are dynamically configurable, allowing for fine-tuning to potentially enhance model performance.

Model performance is evaluated using the following metrics:

* Accuracy
* Precision
* Recall

The test set achieved an accuracy of 100%. Performance scores for each metric are saved in separate files within the `model_training` and `model_evaluation` directories. Visualizations of the results are also included.


