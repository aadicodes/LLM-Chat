from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from langchain.chains import SQLDatabaseChain
from langchain.sql_database import SQLDatabase
from sqlalchemy import create_engine

# Step 1: Load lightweight LLM (Mistral or Phi-2)
model_name = "mistralai/Mistral-7B-Instruct-v0.1"  # Or try "microsoft/phi-2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto")

# Step 2: Create a text generation pipeline
llm_pipeline = pipeline("text-generation", model=model, tokenizer=tokenizer, max_new_tokens=256)

# Step 3: Wrap pipeline in LangChain-compatible interface
from langchain.llms import HuggingFacePipeline
llm = HuggingFacePipeline(pipeline=llm_pipeline)

# Step 4: Connect to SQLite test database
engine = create_engine("sqlite:///enterprise_data.db")
db = SQLDatabase(engine)

# Step 5: Create SQL chain
db_chain = SQLDatabaseChain.from_llm(llm, db, verbose=True)

# Step 6: Interactive loop
print("🔍 Enterprise Data Assistant (Type 'exit' to quit)")
while True:
    user_query = input("\n🧑‍💼 Ask a question: ")
    if user_query.lower() in ["exit", "quit"]:
        print("👋 Goodbye!")
        break
    try:
        response = db_chain.run(user_query)
        print(f"🤖 Answer: {response}")
    except Exception as e:
        print(f"⚠️ Error: {e}")
