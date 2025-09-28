from crewai import LLM

llm = LLM(
        model="watsonx/meta-llama/llama-3-3-70b-instruct",
        base_url="https://us-south.ml.cloud.ibm.com",
        project_id="9dfca46e-8a32-49a9-a6cb-699f75dc3aa7",
        max_tokens=2000,
)