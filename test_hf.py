from transformers import pipeline

pipe = pipeline("text2text-generation", model="google/flan-t5-base")
out = pipe("Extract horsepower from: 203 hp engine")
print(out)
