with (
    open("file1.txt") as f1,
    open("file2.txt") as f2
):
    # Process files
    content1 = f1.read()
    content2 = f2.read()

    print(content1)
    print(content2) 