name = input("File Name: ")
extension = name.rpartition(".")
extension = extension[2]
extension = extension.lower().strip()
match extension:
    case "jpeg" | "gif" | "png":
        print(f"image/{extension}")
    case "jpg":
        print("image/jpeg")
    case "pdf":
        print(f"application/{extension}")
    case "txt":
        print("text/plain")
    case "zip":
        print(f"application/{extension}")
    case _:
        print("application/octet-stream")