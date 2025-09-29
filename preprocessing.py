from transformers import pipeline

# Create the pipeline directly with the model name
# This will handle tokenizer and model initialization internally
classifier = pipeline(
    task="zero-shot-classification",
    model="joeddav/xlm-roberta-large-xnli",
    device=-1  # Use CPU, change to 0 for GPU if available
)

def function_out(review):
  review = review

  candidate_labels = [
      "worst experience",  
      "bad experience",       
      "average experience", 
      "good experience",     
      "excellent experience"  
  ]

  dict_candidate = {
      "worst experience": 1,
      "bad experience":  2,
      "average experience": 3,
      "good experience": 4,
      "excellent experience": 5,
  }

 
  result = classifier(review, candidate_labels, multi_label=False)
  result =  result["labels"][0]
  if result in dict_candidate.keys():
    return [dict_candidate[result] , result]

# @app.post("/")
# async def output(review: str):
#   my_output = function_out(review)
#   return my_output


# print(function_out("got another gift from the product"))
