import main as mainScript


def main():

    path = "templates/markdown.md"

    markdown = mainScript.get_markdown()

    # writing markdown
    with open(path , "w") as file:
        file.write(markdown)

if __name__ == "__main__":
    main()