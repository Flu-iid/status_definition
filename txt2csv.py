with open("fa.txt", "r") as fin:
    with open("output_fa.csv", "+a") as foo:
        foo.write("code, title, description\n")
        for line in fin.readlines():
            line = line.replace("(", "|", 1)
            line = line.replace(")", "|", 1)
            line_list = line.split("|")
            line_list = [i.strip() for i in line_list]
            output = ", ".join(line_list)
            foo.write(output)
            foo.write("\n")
