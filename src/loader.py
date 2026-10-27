import os

def load_documents(folder_path="../docs"):

    documents = []

    if not os.path.exists(folder_path):
        print(f"Folder not found: {folder_path}")
        return documents

    for file_name in os.listdir(folder_path):

        file_path = os.path.join(folder_path, file_name)

        try:

            with open(
                file_path,
                "r",
                encoding="utf-8"
            ) as file:

                content = file.read()

                documents.append(
                    {
                        "source": file_name,
                        "content": content
                    }
                )

        except Exception as e:

            print(
                f"Error loading {file_name}: {e}"
            )

    return documents