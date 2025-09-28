from crewai_tools import SerperDevTool

#Search engine test

search_tool = SerperDevTool()
print(type(search_tool))

search_query = "Latest Breakthroughs in machine learning"
search_results =search_tool.run(query=search_query )

# Print the results
print(f"Search Results for '{search_results}':\n")