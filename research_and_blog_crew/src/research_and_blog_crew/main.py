from research_and_blog_crew.crew import ResearchAndBlogCrew

def run():
    topic = input("Enter a topic: ")
    result = ResearchAndBlogCrew().crew().kickoff(inputs={"topic": topic})
    print(result)

if __name__ == "__main__":
    run()
